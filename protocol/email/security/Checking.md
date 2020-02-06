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
resver-path: domain1=domain2 --根域名相等--> domain3(有可能是子域名)=domain5(有可能是子域名)。
header.from: domain4=domain7
resver-path = header.from
sender: domain6 应该跟domain4/domain7同域名或子域名
如上公式不满足，则邮件有被伪造或者代发风险
显示代发内容: 
1. 如果domain6=resver-path代发，则显示由header.sender代发
2. 如果不相等，可能是伪造，否则不应该出现这种情况，提示警告，则显示由resver-path代发。
## 特例:
QQ: 使用X-QQ-CSender和X-QQ-ORGSender, X-QQ-SPAM: true

