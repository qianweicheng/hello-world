# Domainkeys Identified Mail(DKIM)
域密钥识别邮件 (DKIM)
- 防止修改
- ISP添加评级
       DKIM is that ISPs use this information to build a reputation on your domain. If you have great sending practices (low spam, bounces, high engagement) this can help improve trust and reputation with the ISPs.
DKIM: https://tools.ietf.org/html/rfc6376
DKIM-THREATS: https://tools.ietf.org/html/rfc4686
白话版本: https://postmarkapp.com/guides/dkim
## 为啥有了DKIM之后还需要SPF
- 邮件头没有DKIM-Signature信息，就无法启动DKIM验证。 
- 验证DKIM里面声明的domain是否在SPF中
## DKIM(DKIM-Signature字段)
```
DKIM-Signature: v=1; a=rsa-sha256; d=example.net; s=s110527;
c=simple; q=dns/txt; i=@eng.example.net;
t=1117574938; x=1118006938;
h=from:to:subject:date;
z=From:foo@eng.example.net|To:joe@example.com|Subject:demo=20run|Date:July=205,=202005=203:44:08=20PM=20-0700;
bh=MTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTI=;
b=dzdVyOfAKCdLXdJOc9G2q8LoXSlEniSbav+yuU4zGeeruD00lszZVoG4ZHRNiYzR
```
- 公钥存储在`s`指定的selector+`_domainkey`+`d`指定的domain中
`s110527._domainkey.126.com	text = "v=DKIM1; k=rsa; p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCp9JpS7EORNjwIntXII17mJuwob+hJoVmHr2h2HPpSE7QYgh815kHdYC4JbxXgcP0mNZOY3R1Vk6dUDR8NQiL+xB9fRNWFS36Tq7CzPE/UI/+PxWhPzPnvABr4gbQcres8ee9cgEMPFDpck4O7ULNJNxH003Ofcmh1K+xDGyqPWQIDAQAB"`
#### 信头参数详解
```
v= 版本号（纯文本，必要的），值为1
       格式：v=1*DIGIT
a= 生成签名的算法（纯文本，必要的），验证者必须支持“rsa-sha1”和“rsa-sha256”两种算法，签名者使用“rsa-sha256”签名。
       格式：a=rsa-sha1或者a=rsa-sha256
b= 签名数据（base64，必要的）
       格式：b=base64string
bh= 消息的规范化主体的哈希值，受“l=”标签限制（base64，必要的）。
       格式：bh=base64string
c= 消息规范化算法（纯文本，可选的，默认为“simple/simple”）,"/"两边分别对应头部和主体的规范化算法，当“c=simple”或者“c=relaxed”时，表示头部规范化算法使用simple或者relaxed，而主体规范化算法默认为simple。simple 不允许任何变动，relaxed允许空格和换行等
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