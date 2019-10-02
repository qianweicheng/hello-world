# Thread
## 建议处理方法
#### 表设计
thread表设计： `Account, Message-ID, Thread-ID, Subject, Email, Date`，
此表里面的数据随着Message的删除而删除, 其中Message-ID可以为空，也可以重复(Message-ID重复的情况比较常见，但为空的只是理论存在，真实情况没有case，望补充)
字段|说明
-|-
Account| 账号
Message-Id|这里存放的id来自三部分：In-Reply-To，References和Message-ID
Thread-ID|基于UUID规则生成.
Subject|需要统一规整化，比如去掉“RE:”,"FW:",空格等
From-Email|邮件的`From`字段
Date|邮件的收信时间，用来做通过subject做分组. 按天group则用`yyyy-MM-dd`, 按周group则用`yyyy-WW`等
#### 说明
- 如果没有`Subject, Email, date`三个字段，则无法完成案例2的聚合
#### Thread-ID生成方案比较: 
- `md5(account+正则后的subject+low(email)+处理后的date)`，其中date为邮件收件时
  - 当我们按日聚合，就取`yyyy-MM-dd`
  - 当我们按周聚合，就取`yyyy-WW`
  - 当我们按月聚合，就取`yyyy-MM`
- UUID
优劣比较
- MD5方便完成案例2的聚合，可以不需要查询数据库，直接生成。但理论上存在冲突，并且灵活性不够，比如调整聚合周期
- UUID需要多查一下数据库，效率低，但不存在冲突可能性.
#### 操作逻辑
对于所有新收到的邮件，非Gmail账号：
``` 举例数据
    In-Peply-To: <001@edison.tech>
    References: <002@edison.tech> <003@edison.tech>
    Message-ID: <004@edison.tech>
```
- 通过四个ID查询`SELECT * FROM table WHERE account=01 AND Message-ID in ('<001@edison.tech','<002@edison.tech>', '<003@edison.tech>','<004@edison.tech>')`
    - 如果返回条数=0, 并且不是回复和转发邮件，则通过`Subject+low(email)+send date倒序(一定时间内)` 尝试提取Thread-ID，否则生成新的Thread-ID
    - 如果返回条数=0, 并且是回复或转发邮件，则通过`调整后的Subject+send data倒序(一定时间内)`，尝试提取Thread-ID， 否则生成新的Thread-ID
    - 如果返回条数>0,并且每行的thread-id都相同(大多数正常情况)，直接返回该thread-id; 
    - 如果thread-id有多个不同的值（对于message-id重复的邮件进行回复）,我们找到同一message-id只有一个thread-id的返回；否则生成新的thread-id(回复的邮件都是Message-ID重复的)，例如:
    ```
    message-id: thread-id
    <001@edison.tech> 001
    <001@edison.tech> 002
    <002@edison.tech> 001
    <003@edison.tech> 001
    <004@edison.tech> 001
    这里就是message-id=002对应的thread-id=001为最后结果（找到第一个就退出）
    ```
- In-Reply-To，References,Message-ID里面的每一个item为一条记录，本例就必须有四条记录:
    - In-Peply-To，References中的每个ID的记录中如果有thread-id等于前一步返回的thread-id，则跳过; 否则生成一条新记录(其中Email，date为空)存入。
    - Message-ID的一个ID的记录中如果有thread-id等于前一步返回的thread-id，(在其他邮件中References或者In-Reply-To中存在过)，则跳过; 否则生成一条新的记录存入，区别于前者是email和date不为空。
说明：
- 规整化Subject：去除开头的`(RE:)+`, `(FW:)+`,`(回复:)+`,`(转发:)+`等，并且去除首尾的空白
- 通过此规则，不同的邮件到达顺序，可能导致插入的顺序不一样，但最后的处理结果在数据库留下的记录集合是一样的

## 126-QQ-Gmail 非法Message—ID案例
#### 测试数据
1. 126发送Gmail，QQ
```
Subject: Final Threading
Message-Id: 001@126.com
```
2. Gmail回复126,QQ
```
Subject: RE: Final Threading
References: <001@mx.google.com>
In-Reply-To: <001@mx.google.com>
Message-ID: <002@mail.gmail.com>
```
3. QQ回复126,Gmail
```
Subject: RE: Final Threading
In-Reply-To: 001@126.com
References: 001@126.com
Message-ID: <003@qq.com>
```
4. 126->Gmail->126->Gmail
```
Subject: RE:RE: Final Threading
In-Reply-To: <002@mail.gmail.com>
References: <001@mx.google.com> <002@mail.gmail.com>
Message-ID: <004@126.com>
```
5. 126->QQ->126->QQ
```
Subject: RE:RE: Final Threading(I can change.)
In-Reply-To: <003@qq.com>
References: 001@126.com <003@qq.com>
Message-ID: <005@126.com>
```
6. 126->QQ->126->QQ---FW-By-Gmail-->126
```
Subject: RE:RE: Final Threading(I can change.)
References: 001@126.com(本来有这项，但因为非法，被Gmail去掉了) <003@qq.com> <005@126.com>
In-Reply-To: <005@126.com>
Message-ID: <006@mail.gmail.com>
```
#### 案例数据库记录
- 案例1（不同的邮件到达顺序，可能导致插入顺序不一样，但结果是一样的）:
    - 第1封邮件匹配规则#1.2
      - 插入: `01, Final Threading, xx@126.com, pid1, 001@126.com, ABC, 2019.01.01`
    - 第2封邮件匹配规则#2.2
      - 插入: `01, Final Threading, xx@gmail.com, pid2, <002@mail.gmail.com>, ABC, 2019.01.01`
      - 插入: `01, Final Threading, '', '', <001@mx.google.com>, ABC, ''`
    - 第3封邮件匹配规则#2.1
      - 插入: `01, Final Threading, xx@qq.com, 'pid3', <003@qq.com>, ABC, 2019.01.01`
    - 第4封邮件匹配规则#2.1
      - 插入: `01, Final Threading, xx@126.com, 'pid4', <004@126.com>, ABC, 2019.01.01`
    - 第5封邮件匹配规则#2.1
      - 插入: `01, Final Threading(I can change.), xx@126.com, 'pid5',<005@126.com>, ABC, 2019.01.01`
    - 第6封邮件匹配规则#2.1
      - 插入: `01, Final Threading(I can change.), xx@gmail.com, 'pid6', <006@mail.gmail.com>, ABC, 2019.01.01`
- 案例1（邮件倒序到达）:
    - 第6封邮件匹配规则#2.1
      - 插入:`01, Final Threading(I can change.), '', '', <003@qq.com>, ABC, ''`
      - 插入:`01, Final Threading(I can change.), '', '', <005@126.com>, ABC, ''`
      - 插入:`01, Final Threading(I can change.), 'pid6', <006@mail.gmail.com>, ABC, 2019.01.01`
    - 第5封邮件匹配规则#2.1 
      - 插入:`01, Final Threading(I can change.), '', '', 001@126.com , ABC, ''`
    - 第4封邮件匹配规则#2.2
      - 插入:`01, Final Threading, '', '', <001@mx.google.com> , ABC, ''`
      - 插入:`01, Final Threading, '', '', <002@mail.gmail.com>, ABC, ''`
      - 插入:`01, Final Threading, xx@126.com, 'pid4', <004@126.com>, ABC, 2019.01.01`
    - 第3封邮件匹配规则#2.1
      - 无
    - 第2封邮件匹配规则#2.1:
      - 无
    - 第1封邮件匹配规则#2.1:
      - 无
#### 处理结果
1，2，3，4，5，6组合成一个Thread。参照Gmail thread计算结果
> 普通处理: 1，3，5成一个thread，2，4成一个thread。 纯粹通过Message-ID, References,In-Reply-To计算获得

## 同一个人在一段时间内(1天)连续发送多封同一个主题的邮件
#### 测试数据
1. xxx发送给yyy
```
Subject: Final Threading
From: weicheng@edison.tech
Message-Id: <001@mail.gmail.com>
```
2. xxx发送给yyy
```
Subject: Final Threading
From: weicheng@edison.tech
Message-Id: <002@mail.gmail.com>
```
3. zzz发送给yyy
```
Subject: Final Threading
From: jone@edison.tech
Message-Id: <003@mail.gmail.com>
```
#### 案例数据库记录
- 第1封邮件匹配规则#1.1
    - 插入: `01, Final Threading, weicheng@edison.tech, pid1, <001@mail.gmail.com>, ABC, 2019.01.01`
- 第2封邮件匹配规则#1.1
    - 插入: `01, Final Threading, weicheng@edison.tech, pid1, <001@mail.gmail.com>, ABC, 2019.01.01`
- 第3封邮件匹配规则#1.1
    - 插入: `01, Final Threading, jone@edison.tech, pid1, <001@mail.gmail.com>, DEF, 2019.01.01`
#### 处理结果
三封邮件的subject一样，但#3的`From`不一样，所以处理结果为:`#1,#2两封邮件聚合，#3另外一个Thread`
## 案例3
对于两个写死Message-ID的邮件客户端互发邮件
