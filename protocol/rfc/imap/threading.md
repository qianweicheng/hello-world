# Thread
标准的Thread处理是通过In-Reply-To，References进行的，本章主要增加如下几种特殊情况的处理:
- Message-ID重新生成。部分邮件服务商(Gmail)对非法的Message-ID会进行重新创建，导致Thread分裂
- 同一人使用同一标题(Subject)在一段时间范围内发送了多封邮件
- Message-ID重复。部分邮件服务商/Email Client发送的邮件使用固定的Message-ID，对此类邮件进行回复和转发的处理
- Gmail邮件由于本身提供thread，直接使用gmail的Thread-ID进行聚合
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
- Thread-ID生成方案比较: 
  - MD5: 
    - 规则: `md5(account+正则后的subject+low(email)+处理后的date)`
      - 当我们按日聚合，就取`yyyy-MM-dd`
      - 当我们按周聚合，就取`yyyy-WW`
      - 当我们按月聚合，就取`yyyy-MM`
    - 优势: MD5方便完成案例2的聚合，可以不需要查询数据库，直接生成，Subject, Email, date三字段可以省略(但所有案例的聚合周期只能统一)。
    - 劣势: 理论上存在键值冲突，并且灵活性略低
  - UUID(推荐方案): 
    - 优势: 理论上不存在键值冲突，并且灵活性高
    - 劣势: 
      - 效率低.多了一次数据库查询
      - 必须有`Subject, Email, date`三个字段辅助，否则无法完成案例2的聚合
#### 操作逻辑
对于所有新收到的邮件，非Gmail账号，(Gmail直接帮我们计算好了Thread-ID)：
``` 
    # 举例数据1
    In-Peply-To: <001@edison.tech>
    References: <002@edison.tech> <003@edison.tech>
    Message-ID: <004@edison.tech>
```
```
    # 举例数据2
    MSG-ID THREAD-ID
    001      1
    001      2
    002      1
    004      1
```
- 确定Thread-ID: 
    通过`In-Peply-To，References，Message-ID`中的ID(举例数据1)
    - SQL查询：`SELECT * FROM table WHERE account=01 AND Message-ID in ('<001@edison.tech','<002@edison.tech>', '<003@edison.tech>','<004@edison.tech>')` 。 
    - （优化Optional，主要针对Message-ID重复的情况)如果`In-Peply-To，References`为空：`SELECT * FROM table WHERE account=01 AND Message-ID=<004@edison.tech> LIMIT 10 ORDER BY DATE DESC`
    
    具体逻辑：
    1. 如果返回条数>0
        1. thread-id都相同
          1. 检查返回的记录里面没有“Message-ID=当前Email的Message-ID且Email&Date不为空的”(表示Message-ID没有重复)，直接返回该thread-id，否则下进入下一条; 
          2. (Message-Id重复的情况发生了)从结果中寻找一个“规整后subject相等，并且date在一定时间内”的记录，找到则返回，否则生成一个新的
        2. thread-id有多个不同的值(Message-Id重复的情况发生了),找到同一message-id只有一个thread-id的组合（过滤掉Message-ID重复的数据，举例数据2符合条件的有两个002，004）
            1. 有1个: 则直接返回thread-id
            2. 有多个: thread-id相同，直接返回它; 否则寻找一个“规整后subject相等，并且date在一定时间内”返回; 寻找失败则进入下一步
            3. 有0个: (全部Message-ID重复)从结果中寻找一个“规整后subject相等，并且date在一定时间内”的记录，找到则返回，否则生成一个新的
    2. 如果返回条数=0, 
        1. 不是回复和转发邮件，则通过`Subject+low(email)+send date倒序(一定时间内)` 尝试提取Thread-ID，否则生成新的Thread-ID
        2. 是回复或转发邮件(倒序下载的情况下发生)，则通过`调整后的Subject+send data倒序(一定时间内)`，尝试提取Thread-ID， 否则生成新的Thread-ID
- 插入数据：In-Reply-To，References,Message-ID里面的每一个item为一条记录，本例就必须有四条记录。
    - In-Peply-To，References中的每个ID的记录中如果有thread-id等于前一步返回的thread-id，则跳过; 否则生成一条新记录(其中Email，date为空)存入。
    - Message-ID的一个ID的记录中如果有thread-id等于前一步返回的thread-id，(在其他邮件中References或者In-Reply-To中存在过)，则跳过; 否则生成一条新的记录存入，区别于前者是email和date不为空。
说明：
- 规整化Subject：去除开头的`(RE:)+`, `(FW:)+`,`(回复:)+`,`(转发:)+`等，并且去除首尾的空白
- 通过此规则，不同的邮件到达顺序，可能导致插入的顺序不一样，但最后的处理结果在数据库留下的记录集合是一样的
- 优化。上述的步骤只是为了更清楚的说明逻辑，在实际操作中应该进行优化，现在对于普通邮件很多都需要进行两次查询: 
  1. 通过In-Reply-To，References,Message-ID查询(大部分时候是不需要的)
  2. 通过subject，date等字段查询
- 优化方式，realm是否需要？
  - 一次性把数据查询出来:
    `SELECT * FROM table WHERE account=01 AND (Message-ID in ('<001@edison.tech','<002@edison.tech>', '<003@edison.tech>','<004@edison.tech>') OR subject='Final Threading' AND date='xxx' AND email='xxx')`
  - 对于不需要支持乱序处理的情况下,也就是严格按照UID升序拉下来邮件
    - 当In-Reply-To，References为空，跳过Message-ID查询
    - 当In-Reply-To，References唯一个是`xxxSMTPIN_ADDED_BROKEN@mx.google.com`结尾的，跳过Message-ID查询
    - 这样就SQL就简化成:
    `SELECT * FROM table WHERE account=01 AND subject='Final Threading' AND date='xxx' AND email='xxx'`

## 案例
### 非法Message—ID重新生成
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
    - 第3封邮件，Thread-ID匹配规则#1.1.1
      - 插入: `01, Final Threading, xx@qq.com, 'pid3', <003@qq.com>, ABC, 2019.01.01`
    - 第4封邮件，匹配规则#1.1.1
      - 插入: `01, Final Threading, xx@126.com, 'pid4', <004@126.com>, ABC, 2019.01.01`
    - 第5封邮件，匹配规则#1.1.1
      - 插入: `01, Final Threading, xx@126.com, 'pid5',<005@126.com>, ABC, 2019.01.01`
    - 第6封邮件，匹配规则#1.1.1
      - 插入: `01, Final Threading(I can change.), xx@gmail.com, 'pid6', <006@mail.gmail.com>, ABC, 2019.01.01`
- 案例1（邮件倒序到达）:
    - 第6封邮件，匹配规则#2.2
      - 插入:`01, Final Threading(I can change.), '', '', <003@qq.com>, ABC, ''`
      - 插入:`01, Final Threading(I can change.), '', '', <005@126.com>, ABC, ''`
      - 插入:`01, Final Threading(I can change.), 'pid6', <006@mail.gmail.com>, ABC, 2019.01.01`
    - 第5封邮件，匹配规则#1.1.1
      - 插入:`01, Final Threading, '', '', 001@126.com , ABC, ''`
    - 第4封邮件，匹配规则#2.2
      - 插入:`01, Final Threading, '', '', <001@mx.google.com> , ABC, ''`
      - 插入:`01, Final Threading, '', '', <002@mail.gmail.com>, ABC, ''`
      - 插入:`01, Final Threading, xx@126.com, 'pid4', <004@126.com>, ABC, 2019.01.01`
    - 第3封邮件，匹配规则#1.1.1
      - 无
    - 第2封邮件，匹配规则#1.1.1
      - 无
    - 第1封邮件，匹配规则#1.1.1
      - 无
#### 处理结果
1，2，3，4，5，6组合成一个Thread。参照Gmail thread计算结果
> 普通处理: 1，3，5成一个thread，2，4成一个thread。 纯粹通过Message-ID, References,In-Reply-To计算获得

### 同一个人在一段时间内(1天)连续发送多封同一个主题的邮件
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
    - 插入: `01, Final Threading, weicheng@edison.tech, pid2, <002@mail.gmail.com>, ABC, 2019.01.01`
- 第3封邮件，匹配规则#2.1
    - 插入: `01, Final Threading, jone@edison.tech, pid3, <003@mail.gmail.com>, DEF, 2019.01.01`
#### 处理结果
倒序处理结果一样，这里省略
三封邮件的subject一样，但#3的`From`不一样，所以处理结果为:`#1,#2两封邮件聚合，#3另外一个Thread`
### 固定的Message-ID案例
部分邮件发送端或者邮件客户端会把Message-ID固定成一个值，比如QQ通知邮件的Message-ID:<10000@qq.com>
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
4. (第二天)xxx发送给yyy
```
Subject: A new day
From: jone@edison.tech
Message-Id: <001@mail.gmail.com>
```
5. yyy发送给xxx
```
Subject: Another thing
From: mikel@edison.tech
Message-Id: <001@mail.gmail.com>
```
6. (第二天)yyy回信给xxx
```
Subject: RE: A new day
From: <mikel@edison.tech>
References: <001@mail.gmail.com>
In-Reply-To: <001@mail.gmail.com>
Message-Id: <001@mail.gmail.com>
```
#### 案例数据库记录
- 顺序处理
  - 第1封邮件，匹配规则#2.1
      - 插入: `01, Final Threading, jone@edison.tech, pid1, <001@mail.gmail.com>, ABC, 2019.01.01`
  - 第2封邮件，匹配规则#1.1.2
      - 插入: `01, Another Final Threading, jone@edison.tech, pid2, <001@mail.gmail.com>, DEF, 2019.01.01`
  - 第3封邮件，匹配规则#1.2.3
      - 插入: `01, Final Threading, mikel@edison.tech, pid3, <001@mail.gmail.com>, ABC, 2019.01.01`
  - 第4封邮件，匹配规则#1.2.3
      - 插入: `01, A new day, jone@edison.tech, pid4, <001@mail.gmail.com>, GHI, 2019.01.02`
  - 第5封邮件，匹配规则#1.2.3
      - 插入: `01, Another thing, mikel@edison.tech, pid5, <001@mail.gmail.com>, JKL, 2019.01.02`
  - 第6封邮件，匹配规则#1.2.3
      - 插入: `01, A new day, mikel@edison.tech, pid6, <001@mail.gmail.com>, GHI, 2019.01.02`
- 倒序处理
  - 第6封邮件，匹配规则#2.2
      - 插入: `01, A new day, mikel@edison.tech, pid6, <001@mail.gmail.com>, ABC, 2019.01.02`
  - 第5封邮件，匹配规则#1.1.2
      - 插入: `01, Another thing, mikel@edison.tech, pid5, <001@mail.gmail.com>, DEF,2019.01.02`
  - 第4封邮件，匹配规则#1.2.3
      - 插入: `01, A new day, jone@edison.tech, pid4, <001@mail.gmail.com>, ABC, 2019.01.02`
  - 第3封邮件，匹配规则#1.2.3
      - 插入: `01, Final Threading, mikel@edison.tech, pid3, <001@mail.gmail.com>, GHI, 2019.01.01`
  - 第2封邮件，匹配规则#1.2.3
      - 插入: `01, Another Final Threading, jone@edison.tech, pid2, <001@mail.gmail.com>, JKL, 2019.01.01`
  - 第1封邮件，匹配规则#1.2.3
      - 插入: `01, Final Threading, jone@edison.tech, pid1, <001@mail.gmail.com>, GHI, 2019.01.01`
#### 处理结果
所以处理结果为:#1和#3，#4和#6两两聚合，#2/#5单独Thread