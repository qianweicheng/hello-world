## Authentication-Results
- ptypes
  - body
  - header
  - policy
  - smtp
### dkim result
- dkim=
  - none
  - pass
  - fail
  - policy
  - neutral
  - temperror
  - permerror
- header.i
- header.d
- header.a: algorithm version
- header.s:selector
### spf result
- spf=
  - 同dkim
- smtp.mailfrom
- smtp.helo
### iprev result
- iprev=
  - pass
  - fail
  - temperror
  - permerror
### auth result
  - auth=
    - none
    - pass
    - fail
    - temperror
    - permerror
  - smtp.auth
  - smtp.mailfrom
## 结论
1. 提取DKIM-Signature的d参数(域名，如果DKIM-Signature存在，则d参数一定存在)，`domain1`
2. 提取Authentication-Results
   1. dkim
     - header.i参数, `domain2`
     - header.d参数,可能是数组，分号分割,只要其中一个匹配就行, `domain2`,
   2. spf
     - smtp.mailfrom (or smtp.mail) `domain3`
     - 缺失或者非pass,neutral则直接提醒
   3. dmarc
     - header.from `domain4`
     - 缺失或者非pass,neutral则直接提醒
   4. compauth
     - Office 365中的客户读取compauth值直接判断就行
3. Return-Path: `domain5`，有些g suite 这类的代发，我们不处理inner-domain的攻击，这个依托各自的邮箱服务器的权限验证
4. Sender: `domain6`
5. Header.From: `domain7`
### 计算
```
公式1: resver-path: domain1=domain2 --根域名相等--> domain3(有可能是子域名)=domain5(有可能是子域名)。
公式2: header.from: domain4=domain7
公式3: resver-path = header.from
公式4: sender: 如果有则 domain6应该跟domain4/domain7同域名或子域名

结果: 
- 以上所有公式满足：则有header.sender就显示，没有就当正常内容
- 如果公式1不成立。显示警告，一般都是邮件被转发或者人为构造导致的错误。并考虑把错误原因显示
- 如果公式2不成立。显示警告，一般都是邮件被转发或者人为构造导致的错误。
- 如果公式3不成立。显示由resver-path代发，(这是正常的代发邮件)
- 如果公式4不成立。显示警告, 一般都是邮件被转发或者人为构造导致的错误。
```
## 特例:
QQ: 使用X-QQ-CSender和X-QQ-ORGSender, X-QQ-SPAM: true

