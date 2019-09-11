# SMTP&Submission
消息投送协议有几个:
- SMTP(RFC5321)
- EMSD(RFC2524)
- Message Submission for Mail(RFC6409)
  - 我们平时所用的SMTP其实是这个，它是基于RFC5321
## 名词解释
- Message Transfer Agents (MTAs)
  - 只能添加'Received', 'Return-Path'
  - 使用SMTP协议RFC5321
- Message User Agents (MUAs)
  - 可以理解为邮件客户端
- Message Submission Agent (MSA)
  - Add Sender, Date, Message-ID
  - Transfer Encode
  - Sign the Message
  - Encrypt the Message
  - Resolve Aliases
  - Header Rewriting
  - Message-ID如果不存在/无效格式，则生成Message-ID,有效的`<001@google.com>`
  - 使用RFC6409
- Mail Service Provider(MSP)
  - An operator of Mail Access Servers and/or Mail Submission Servers
## MX vs SMTP
- mx 纯粹的SMTP协议
  -  `openssl s_client -connect 126mx02.mxmail.netease.com:25 -crlf -debug -starttls smtp`
- smtp服务器(对MUA开放的)
  - 很多算是MSA了范畴了
  - `openssl s_client -connect smtp.126.com:25 -crlf -debug -starttls smtp`
## Implicit TLS vs STARTTLS
- Implicit TLS FOR IMAP: 993
- Implicit TLS FOR POP: 995
- Implicit TLS FOR SMTP: 465
- STARTTLS FOR SMTP: 587
