# Thread
## 126-QQ-Gmail 非法Message—ID案例
1. 126发送Gmail，QQ
```
Subject: Final Threading
Message-Id: 002@126.com
```
2. Gmail回复126,QQ
```
Subject: RE: Final Threading
References: <5d908c3f.1c69fb81.581bc.45daSMTPIN_ADDED_BROKEN@mx.google.com>
In-Reply-To: <5d908c3f.1c69fb81.581bc.45daSMTPIN_ADDED_BROKEN@mx.google.com>
Message-ID: <CA+dUs+kLKhMV2cYYJDYvRSfe0+Ncoq=iNF4ijg2NQUQTUZY5OQ@mail.gmail.com>
```
3. QQ回复126,Gmail
```
Subject: RE: Final Threading
In-Reply-To: 002@126.com
References: 002@126.com
Message-ID: <tencent_623AE4869FFED66D0222DC79608434648A09@qq.com>
```
4. 126->Gmail->126->Gmail
```
Subject: RE:RE: Final Threading
In-Reply-To: <CA+dUs+kLKhMV2cYYJDYvRSfe0+Ncoq=iNF4ijg2NQUQTUZY5OQ@mail.gmail.com>
References: <5d908c3f.1c69fb81.581bc.45daSMTPIN_ADDED_BROKEN@mx.google.com> <CA+dUs+kLKhMV2cYYJDYvRSfe0+Ncoq=iNF4ijg2NQUQTUZY5OQ@mail.gmail.com>
Message-ID: <5ad0a2e1.58e4.16d7cab1aeb.Coremail.edotest1@126.com>
```
5. 126->QQ->126->QQ
```
Subject: RE:RE: Final Threading
In-Reply-To: <tencent_623AE4869FFED66D0222DC79608434648A09@qq.com>
References: 002@126.com <tencent_623AE4869FFED66D0222DC79608434648A09@qq.com>
Message-ID: <7654b2a7.58e8.16d7cab8d38.Coremail.edotest1@126.com>
```
6. 126->QQ->126->QQ---FW--->126
```
References: <tencent_623AE4869FFED66D0222DC79608434648A09@qq.com> <7654b2a7.58e8.16d7cab8d38.Coremail.edotest1@126.com>
In-Reply-To: <7654b2a7.58e8.16d7cab8d38.Coremail.edotest1@126.com>
Message-ID: <CA+dUs+nmQdSetCfAUO0mnCVro6qGvRzPq1dTL_L_O8QmOKaA7g@mail.gmail.com>
```
> 普通处理: 1，3，5成一个thread，2，4成一个thread。 纯粹通过Message-ID, References,In-Reply-To计算获得
> 完美解决: 1，2，3，4，5，6组合成一个Thread。参照Gmail thread计算结果

## 同一个人在一段时间内(1天)连续发送多封同一个主题的邮件
1. xxx发送给yyy
```
Subject: Final Threading
From: weicheng@edison.tech
Message-Id: 001@mail.gmail.com
```
2. xxx发送给yyy
```
Subject: Final Threading
From: weicheng@edison.tech
Message-Id: 002@mail.gmail.com
```
2. zzz发送给yyy
```
Subject: Final Threading
From: jone@edison.tech
Message-Id: 003@mail.gmail.com
```
> 建议处理结果为: 1，2能够组合成一个thread, 3 构成另外一个thread

## 建议处理方法
使用EdoThread表，此表里面的数据随着EdoMessage的删除而删除, 其中Message-ID可以为空，也可以重复(Message-ID重复的情况比较常见，目前Message-ID为空的主要是什么情况？)
Table 字段： `account, Subject, Sender-Email, PID, Message-ID, date-yyyy-MM-dd, Thread-ID`, 其中Thread-ID生成的规则为: `md5(account+正则后的subject+sender_email+date-yyyy-MM-dd)`
对于所有新收到的邮件，非Gmail账号：
- 如果In-Reply-To，References为空(没有回复的情况)，则
  - 如果`Subject`是`回复(RE: ,回复: ,FW开头)`, 则通过`正则后的Subject+send data倒序(一定时间内)`，找到并提取Thread-ID， 否则生成新的Thread-ID，然后插入
  - 如果`Subject`不是`回复(RE: ,回复: 开头)`, 则通过`Subject+sender address+send date倒序(一定时间内)` 找到并提取Thread-ID，否则生成新的Thread-ID，并且插入
- 如果In-Reply-To，References不为空。 其实#2.1，#2.2不需要分开，这里分开讨论主要是为减少一次数据库查询。
  - `In-Reply-To`不是`xxxSMTPIN_ADDED_BROKEN@mx.google.com`结尾的，通过`In-Reply-To & References`在`EdoThread`查找`Message-ID`，找到则提取Thread-ID， 否则回到#1
  - `In-Reply-To`是`xxxSMTPIN_ADDED_BROKEN@mx.google.com`结尾的，当成#1处理：也就是`In-Reply-To，References`为空的情况。
- 在同一封邮件里面`In-Reply-To，References`只要第一个Message-ID获取到了Thread-ID，后续的Message-ID都直接使用同一个Thread—ID插入就OK
- 通过Message-IDs搜索有可能返回多条记录，这是由于Message-ID有可能重复的，当成#1处理
## 案例处理结果
- 案例1:
第1封邮件匹配规则#1.1, 插入EdoThread: `account, Final Threading, xx@126.com, 002@126.com, xxxx, 2019.01.01`
第2封邮件匹配规则#2.2, 插入EdoThread: `account, Final Threading, xx@gmail.com, <CA+dUs+kLKhMV2cYYJDYvRSfe0+Ncoq=iNF4ijg2NQUQTUZY5OQ@mail.gmail.com>, xxxx, 2019.01.01`
第3封邮件匹配规则#2.1, 插入EdoThread: `account, Final Threading, xx@qq.com, <tencent_623AE4869FFED66D0222DC79608434648A09@qq.com>, xxxx, 2019.01.01`
第4封邮件匹配规则#2.1, 插入EdoThread: `account, Final Threading, xx@126.com, <4.edotest1@126.com>, xxxx, 2019.01.01`
第5封邮件匹配规则#2.1, 插入EdoThread: `account, (This can be different, because it does not depend on this), xx@126.com, <7.edotest1@126.com>, xxxx, 2019.01.01`
到此可以通过`THREAD-ID=xxxx`搜索出整个THREAD列表
- 案例2: #1,#2两封邮件聚合，#3，另外一个Thread