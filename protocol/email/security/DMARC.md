# Domain-based Message Authentication, Reporting & Conformance(DMARC)
基于域的邮件身份验证、报告和一致性 (DMARC),以验证邮件发件人并确保目标电子邮件系统信任从你的域发送的邮件。
在DKIM和SPF的基础上添加一个协调的机制。
规定如果DKIM，SPF没有验证通过怎么处理：是接受，决绝，报告
RFC: https://tools.ietf.org/html/rfc7489
白话版: https://postmarkapp.com/guides/dmarc
## 保存位置
和DKIM，SPF一样，放DNS里面.配置DMARC:
- 创建子域名: `_dmarc.yourdomain`
- 查询: `dig +short TXT _dmarc.yourdomain`
- 公钥存储在: `(selector)._domainkey.yourdomain`
    ```
    _dmarc.domain.com TXT v=DMARC1\; p=reject\; pct=100\; rua=mailto:dmarc-reports@domain.com\;
    ```
## 字段说明
Tag Name｜Purpose｜Sample
-｜- | - 
v   |   Protocol version   |   v=DMARC1
pct   |   Percentage of messages subjected to filtering   |   pct=20
ruf   |   Reporting URI for forensic reports   |   ruf=mailto:authfail@example.com
rua   |   Reporting URI of aggregate reports   |   rua=mailto:aggrep@example.com
p   |   Policy for organizational domain   |   p=quarantine,reject
sp   |   Policy for subdomains of the OD   |   sp=reject
adkim   |   Alignment mode for DKIM   |   adkim=s 或者r, 主要影响是否子域名匹配，默认r
aspf   |   Alignment mode for SPF   |   aspf=s 或者 r, 主要影响是否子域名匹配，默认r
fo  ｜  Failure reporting options   ｜  0,1,d,s
rf  |   Report Format   |   afrf
## 验证规则
怀疑： DKIM-Signature: c=relaxed/relaxed;
### Example
```
_dmarc.gmail.com	text = "v=DMARC1; p=none; sp=quarantine; rua=mailto:mailauth-reports@google.com"
_dmarc.hotmail.com	text = "v=DMARC1; p=none; rua=mailto:d@rua.agari.com;ruf=mailto:d@ruf.agari.com;fo=1:s:d"
_dmarc.office365.com	text = "v=DMARC1; p=reject; pct=100; rua=mailto:d@rua.agari.com; ruf=mailto:d@ruf.agari.com; fo=1"
_dmarc.yahoo.com	text = "v=DMARC1; p=reject; pct=100; rua=mailto:dmarc_y_rua@yahoo.com;"
_dmarc.hushmail.com	text = "v=DMARC1; p=quarantine; pct=100; rua=mailto:dmarc-rua@hushmail.com"
_dmarc.126.com	text = "v=DMARC1; p=none;"
_dmarc.qq.com	       text = "v=DMARC1; p=none; rua=mailto:mailauth-reports@qq.com"
_dmarc.aliyun.com	text = "v=DMARC1; p=quarantine; pct=5;rua=mailto:dmarc@service.aliyun.com;"
_dmarc.alipay.com	text = "v=DMARC1; p=quarantine; rua=mailto:dmarc_ay@service.alibaba.com; ruf=mailto:dmarc_ay@service.alibaba.com"
```
## 反馈
一个XML文件