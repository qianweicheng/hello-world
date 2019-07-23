# Multipurpose Internet Mail Extensions(MIME-Type) 
也作:Content Type,扩展了电子邮件标准，使其能够支持非ASCII字符、二进制格式附件等多种格式的邮件消息。在万维网中使用的HTTP协议中也使用了MIME的框架，标准被扩展为互联网媒体类型
## Headers
正文跟着Header
- 在top-level header后面必须空两行
- 在multipart里面内容前必须空一行
#### X-***系列
自定义Header
#### Content-系列
- Content-ID
- Content-Description
- Content-Transfer-Encoding
    "7bit"(DEFAULT), "8bit", "base64", "quoted-printable" or "binary", 
- Content-Type
```
    Content-Type: multipart/mixed; 
          boundary=gc0p4Jq0M2Yt08jU534c0p
```
boundary+`--`作前缀开始, `--`+boundary+`--`结束
```
From: Moderator-Address 
MIME-Version: 1.0 
Subject:  Internet Digest, volume 42 
Content-Type: multipart/digest; 
     boundary="xxx" 


--xxx

From: someone-else 
Subject: my opinion 

...body goes here ... 
--xxx

From: someone-else-again 
Subject: my different opinion 

... another body goes here... 

--xxx--
```
## Content-Type详解
#### 目前主要的大类
- text: default to 'plain'
- multipart: default to 'mixed'
- message: default to 'rfc822'
- image: default to 'jpeg and gif.'
- audio: default to 'display'
- video: default to 'mpeg
- application: default to 'octet-stream'
   所有未知的都默认二进制: `application/octet-stream`
#### 容器类
- multipart/mixed
- multipart/alternative
- multipart/digest
    等同mixed，但语意不同，the default Content-Type value for a body part is changed from "text/plain" to "message/rfc822". 
- multipart/parallel
    等同mixed，但语意不同
- multipart/report
- message/delivery-status
- message/rfc822
- message/partial(TODO)
    将一封大邮件切分成几封邮件发送
    ```
    <!-- begins with 1, not 0. -->
    Content-Type: Message/Partial; 
          number=2; total=3; 
          id="oc=jpbe0M2Yt4s@thumper.bellcore.com"; 

    Content-Type: Message/Partial; 
          id="oc=jpbe0M2Yt4s@thumper.bellcore.com"; 
          number=2 
    Content-Type: Message/Partial; 
          number=3; total=3; 
          id="oc=jpbe0M2Yt4s@thumper.bellcore.com"; 
    ```
    ```
        Content-type: message/external-body; access- 
        type=local-file; 
            name=/u/nsb/Me.gif 

        Content-type:  image/gif 

        THIS IS NOT REALLY THE BODY! 
    ```
- message/External-Body(TODO)
  "FTP", "ANON-FTP", "TFTP", "AFS", "LOCAL-FILE", and "MAIL-SERVER"
#### 常见MIME
```
text/plain（纯文本）
text/html（HTML文档）
image/*
video/mpeg（MPEG动画）
application/octet-stream（任意的二进制数据）
application/xhtml+xml（XHTML文档）
application/pdf（PDF文档）
application/msword（Microsoft Word文件）
message/rfc822（RFC 822形式）
multipart/alternative（HTML邮件的HTML形式和纯文本形式，相同内容使用不同形式表示）
application/x-www-form-urlencoded（使用HTTP的POST方法提交的表单）
multipart/form-data（同上，但主要用于表单提交时伴随文件上传的场合)
```
## 实体Type
- Standards tree
>type "/" subtype ["+" suffix] *[";" parameter]
- Vendor tree
>type "/" "vnd." subtype ["+" suffix] *[";" parameter]
- Personal or vanity tree
>type "/" "prs." subtype ["+" suffix] *[";" parameter]
- Unregistered tree
>type "/" "x." subtype ["+" suffix] *[";" parameter]
- Suffix
+xml, +json, +ber, +der, +fastinfoset, +wbxml, +zip, +gzip