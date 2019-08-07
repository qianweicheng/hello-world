# 邮件安全
- DMARC(2012)
- DKIM
- SPF
## 帮助工具
http://www.mail-tester.com/
只要给页面上的邮箱随便发一封邮件，然后点击按钮提交就可以看到测试结果，里面会有一些优化建议，非常好用。
# DMARC(Domain-based Message Authentication, Reporting & Conformance)
https://tools.ietf.org/html/rfc7489
DMARC是一种基于现有的SPF和DKIM协议的可扩展电子邮件认证协议，在邮件收发双方建立了邮件反馈机制，便于邮件发送方和邮件接收方共同对域名的管理进行完善和监督。当Mail Receiver方（其MTA需支持DMARC协议）收到该域发送过来的邮件时，则进行DMARC校验，若校验失败还需发送一封report到指定[URI]（常是一个邮箱地址）。
## 查询
`dig +short TXT _dmarc.paypal.com`
返回：`text = "v=DMARC1\; p=reject\; rua=mailto:d@rua.agari.com\; ruf=mailto:dk@bounce.paypal.com,mailto:d@ruf.agari.com"`
# DKIM（DomainKeys Identified Mail）
DKIM是一种防范电子邮件欺诈的验证技术，通过消息加密认证的方式对邮件发送域名进行验证。
## 例子：
```
DKIM-Signature: v=1; a=rsa-sha256; d=example.net; s=brisbane;
c=simple; q=dns/txt; i=@eng.example.net;
t=1117574938; x=1118006938;
h=from:to:subject:date;
z=From:foo@eng.example.net|To:joe@example.com|Subject:demo=20run|Date:July=205,=202005=203:44:08=20PM=20-0700;
bh=MTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTI=;
b=dzdVyOfAKCdLXdJOc9G2q8LoXSlEniSbav+yuU4zGeeruD00lszZVoG4ZHRNiYzR
```
## 解析：
```
v= 版本号（纯文本，必要的），值为1
       格式：v=1*DIGIT
a= 生成签名的算法（纯文本，必要的），验证者必须支持“rsa-sha1”和“rsa-sha256”两种算法，签名者使用“rsa-sha256”签名。
       格式：a=rsa-sha1或者a=rsa-sha256
b= 签名数据（base64，必要的）
       格式：b=base64string
bh= 消息的规范化主体的哈希值，受“l=”标签限制（base64，必要的）。
       格式：bh=base64string
c= 消息规范化算法（纯文本，可选的，默认为“simple/simple”）,"/"两边分别对应头部和主体的规范化算法，当“c=simple”或者“c=relaxed”时，表示头部规范化算法使用simple或者relaxed，而主体规范化算法默认为simple。
       格式：c=sig-c-tag-alg["/"sig-c-tag-alg]
              sig-c-tag-alg="simple"/"relaxed"
d= Signing Domain Identifier ，即SDID （纯文本，必要的）
       格式：d=domain-name
h= 签名的头字段（纯文本，必要的），提交给签名算法的头字段名称列表，用“:”分隔。
       格式：h=hdr-name*(":"hdr-name)
i= Agent or User Identifier ，即AUID，值为@domain
       格式：i=[Local-part]"@"domain-name
                     Local-part为空，domain-name与“d=”的值一样或者是其子域。
l= 主体长度数（纯文本无符号十进制整型，可选的，默认为整个主体）
       格式：l=1*76DIGIT
q= 一个查询方式的列表，以冒号分隔，用于检索公钥（纯文本，可选的，默认为“dns/txt”），每个查询方式的形式为“type[/options]”。
       格式：q=dns/txt
s= selector，（纯文本，必要的）
       格式：s=selector
t= 签名时间戳（纯文本无符号十进制整型；推荐的，默认为一个未知的创建时间）。
       格式：t=1*12DIGIT
x= 签名到期时间（纯文本无符号十进制整型；推荐的，默认永不过期）
       格式：x=1*12DIGIT
z= 复制的头字段（dkim-quoted-printable，可选的，默认为null）
       格式：z=sig-z-tag-copy*（"|"sig-z-tag-copy）
              sig-z-tag-copy= hdr-name":"qp-hdr-value

```

# SPF(Sender Policy Framework)
SPF是为了防范伪造发件人地址发送垃圾邮件而提出的一种开放式标准，是一种以IP地址认证电子邮件发件人身份的技术。域名所有者通过在DNS中发布SPF记录来授权合法使用该域名发送邮件的IP地址。
当在DNS中定义了域名的SPF记录后，为了确认邮件声称发件人不是伪造的，邮件接收方首先检查邮件域名的SPF记录，来确定发件人的IP地址是否被包含在SPF记录中，若包含，则认为是一封正确的邮件，否则认为是一封伪造的邮件并退回，或将其标记为垃圾/仿冒邮件。
设置正确的SPF记录可以提高邮件系统发送外域邮件的成功率，也可以一定程度上防止被假冒域名发送邮件。
# PTR(反向域名解析)