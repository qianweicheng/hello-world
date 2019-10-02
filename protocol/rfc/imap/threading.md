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
Date|邮件的收信时间
#### 说明
- 如果没有`Subject, Email, date`三个字段，则无法完成案例2的聚合
- Thread-ID生成方案比较: 
  - MD5: 
    - 规则: `md5(account+正则后的subject+low(email)+处理后的date)`
      - 当我们按日聚合，就取`yyyy-MM-dd`
      - 当我们按周聚合，就取`yyyy-WW`
      - 当我们按月聚合，就取`yyyy-MM`
    - 优势: MD5方便完成案例2的聚合，可以不需要查询数据库，直接生成。
    - 劣势: 理论上存在冲突，并且灵活性不够
  - UUID: 
    - 优势: 理论上不存在冲突，并且灵活性高.
    - 劣势: 效率低.
#### 操作逻辑
对于所有新收到的邮件，非Gmail账号：
``` 举例数据
    In-Peply-To: <001@edison.tech>
    References: <002@edison.tech> <003@edison.tech>
    Message-ID: <004@edison.tech>
```
- 确定Thread-ID: 通过四个ID查询`SELECT * FROM table WHERE account=01 AND Message-ID in ('<001@edison.tech','<002@edison.tech>', '<003@edison.tech>','<004@edison.tech>')`
    - 如果返回条数>0
        - 每行的thread-id都相同(大多数正常情况)，直接返回该thread-id; 
        - 如果thread-id有多个不同的值(对于message-id重复的邮件进行回复),找到同一message-id只有一个thread-id的组合, 如果有
            - 1个: 则直接返回thread-id
            - 多个: thread-id相同，直接返回它; 否则根据subject和date挑选一个; 挑选失败则进入下一步
            - 0个: 进入下一步(回复的邮件都是Message-ID重复的)
    - 如果返回条数=0, 
        - 不是回复和转发邮件，则通过`Subject+low(email)+send date倒序(一定时间内)` 尝试提取Thread-ID，否则生成新的Thread-ID
        - 是回复或转发邮件，则通过`调整后的Subject+send data倒序(一定时间内)`，尝试提取Thread-ID， 否则生成新的Thread-ID
- 插入数据：In-Reply-To，References,Message-ID里面的每一个item为一条记录，本例就必须有四条记录。
    - In-Peply-To，References中的每个ID的记录中如果有thread-id等于前一步返回的thread-id，则跳过; 否则生成一条新记录(其中Email，date为空)存入。
    - Message-ID的一个ID的记录中如果有thread-id等于前一步返回的thread-id，(在其他邮件中References或者In-Reply-To中存在过)，则跳过; 否则生成一条新的记录存入，区别于前者是email和date不为空。
说明：
- 规整化Subject：去除开头的`(RE:)+`, `(FW:)+`,`(回复:)+`,`(转发:)+`等，并且去除首尾的空白
- 通过此规则，不同的邮件到达顺序，可能导致插入的顺序不一样，但最后的处理结果在数据库留下的记录集合是一样的
#### 优化
这个步骤只是为了更清楚的说明逻辑，在实际操作中应该进行优化，比如:
现在对于普通邮件基本上都需要进行两次查询: 
- 通过In-Reply-To，References,Message-ID查询
- 通过subject，date等字段查询


优化方式，realm是否需要？
- 一次性把数据查询出来:
`SELECT * FROM table WHERE account=01 AND (Message-ID in ('<001@edison.tech','<002@edison.tech>', '<003@edison.tech>','<004@edison.tech>') OR subject='Final Threading' AND date='xxx' AND email='xxx') `


## 非法Message—ID案例
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
Subject: RE:RE: Final Threading
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
    - 第1封邮件，Thread-ID匹配规则#2.1
      - 插入: `01, Final Threading, xx@126.com, pid1, 001@126.com, ABC, 2019.01.01`
    - 第2封邮件，Thread-ID匹配规则#2.2
      - 插入: `01, Final Threading, xx@gmail.com, pid2, <002@mail.gmail.com>, ABC, 2019.01.01`
      - 插入: `01, Final Threading, '', '', <001@mx.google.com>, ABC, ''`
    - 第3封邮件，Thread-ID匹配规则#1.1
      - 插入: `01, Final Threading, xx@qq.com, 'pid3', <003@qq.com>, ABC, 2019.01.01`
    - 第4封邮件，匹配规则#1.1
      - 插入: `01, Final Threading, xx@126.com, 'pid4', <004@126.com>, ABC, 2019.01.01`
    - 第5封邮件，匹配规则#1.1
      - 插入: `01, Final Threading, xx@126.com, 'pid5',<005@126.com>, ABC, 2019.01.01`
    - 第6封邮件，匹配规则#1.1
      - 插入: `01, Final Threading(I can change.), xx@gmail.com, 'pid6', <006@mail.gmail.com>, ABC, 2019.01.01`
- 案例1（邮件倒序到达）:
    - 第6封邮件，匹配规则#2.2
      - 插入:`01, Final Threading(I can change.), '', '', <003@qq.com>, ABC, ''`
      - 插入:`01, Final Threading(I can change.), '', '', <005@126.com>, ABC, ''`
      - 插入:`01, Final Threading(I can change.), 'pid6', <006@mail.gmail.com>, ABC, 2019.01.01`
    - 第5封邮件，匹配规则#1.1
      - 插入:`01, Final Threading, '', '', 001@126.com , ABC, ''`
    - 第4封邮件，匹配规则#2.2
      - 插入:`01, Final Threading, '', '', <001@mx.google.com> , ABC, ''`
      - 插入:`01, Final Threading, '', '', <002@mail.gmail.com>, ABC, ''`
      - 插入:`01, Final Threading, xx@126.com, 'pid4', <004@126.com>, ABC, 2019.01.01`
    - 第3封邮件，匹配规则#1.1
      - 无
    - 第2封邮件，匹配规则#1.1
      - 无
    - 第1封邮件，匹配规则#1.1
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
- 第1封邮件，匹配规则#2.1
    - 插入: `01, Final Threading, weicheng@edison.tech, pid1, <001@mail.gmail.com>, ABC, 2019.01.01`
- 第2封邮件，匹配规则#2.1
    - 插入: `01, Final Threading, weicheng@edison.tech, pid2, <001@mail.gmail.com>, ABC, 2019.01.01`
- 第3封邮件，匹配规则#2.1
    - 插入: `01, Final Threading, jone@edison.tech, pid3, <001@mail.gmail.com>, DEF, 2019.01.01`
#### 处理结果
三封邮件的subject一样，但#3的`From`不一样，所以处理结果为:`#1,#2两封邮件聚合，#3另外一个Thread`
## 固定的Message-ID案例
对于两个写死Message-ID的邮件客户端互发邮件
1. xxx发送给yyy
```
Subject: Final Threading
From: jone@edison.tech
Message-Id: <001@mail.gmail.com>
```
2. xxx发送给yyy
```
Subject: Another Final Threading
From: jone@edison.tech
Message-Id: <001@mail.gmail.com>
```
3. yyy回信给xxx
```
Subject: RE: Final Threading
From: <mikel@edison.tech>
References: <001@mail.gmail.com>
In-Reply-To: <001@mail.gmail.com>
Message-Id: <001@mail.gmail.com>
```
#### 案例数据库记录
- 第1封邮件，匹配规则#2.1
    - 插入: `01, Final Threading, jone@edison.tech, pid1, <001@mail.gmail.com>, ABC, 2019.01.01`
- 第2封邮件，匹配规则#2.1
    - 插入: `01, Another Final Threading, jone@edison.tech, pid2, <001@mail.gmail.com>, DEF, 2019.01.01`
- 第3封邮件，匹配规则#1.2.2
    - 插入: `01, Final Threading, mikel@edison.tech, pid3, <001@mail.gmail.com>, ABC, 2019.01.01`