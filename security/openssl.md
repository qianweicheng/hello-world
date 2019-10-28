# Openssl
分三大块:
- 标准命令 如: ca,gendsa,genpkey,genrsa,pkcs8,req,rsa,x509等
- 数字签名(dgst快捷方式) 如: md5,sha256等
- 对称加密(enc快捷方式) 如: aes-256-cbc,base64,des,des3等
## 签名与验证
Linux Only: `sha512sum,md5sum`
`openssl ciphername or openssl enc -ciphername`
- 签名
  `openssl md5 -out 1.md5 a.txt` = `openssl dgst -md5  -out a.txt.md5 a.txt`
- 密钥签名
  - 密钥签名: `openssl dgst -md5 -out md5_nohex.sign -sign server.key a.txt`
  - 私钥验证: `openssl dgst -md5 -prverify server.key -signature md5_nohex.sign a.txt`
  - 公钥验证:`openssl dgst -md5 -verify server.pub -signature md5_nohex.sign a.txt`
## 对称加密解密
base只是一种编码，可以结合加密解密一起用
- Base64编/解码:
  - `openssl base64 -in a.txt` = `openssl enc -A -base64 -in a.txt`
  - `openssl base64 -d -in a.base64`
- 加密
`openssl enc -aes-128-cbc -in a.txt -out out.txt -pass pass:123456`
`openssl enc -aes-128-cbc -in a.txt -out out.txt -pass file:passwd.txt`
`openssl enc -aes-128-cbc -in a.txt -out out.txt -pass env:passwd`
`openssl enc -aes-128-cbc -in a.txt -out out.txt -pass stdin`
- 解密: 在加密的命令上加`-d`
## 非对称加解密:
主要命令: `openssl rsautl`. 其中`openssl rsa`主要用来管理证书
#### 公钥加密，私钥解密
- 公钥加密
`openssl rsautl -encrypt -in a.txt -inkey server.key -out a-rsa-enc.txt`
`openssl rsautl -encrypt -in a.txt -inkey server.pub -pubin -out a-rsa-enc.txt`
- 私钥解密
`openssl rsautl -decrypt -in a-rsa-enc.txt -inkey server.key -out a-rsa-replain.txt`
#### 私钥加密，公钥解密
- 私钥加密
`openssl rsautl -sign -in a.txt -inkey server.key -out sign.txt`
- 公钥解密
`openssl rsautl -verify -in sign.txt -inkey server.key -out replain.txt`
#### SSL/TLS客户端程序
- s_client
`openssl s_client -connect localhost:2009 -crlf -debug -key clientprikey.pem -cert client.pem -ssl3 -cipher EXP-KRB5-RC4-MD5 -msg `
`openssl s_client -connect localhost:2009 -crlf -debug -starttls smtp`
- s_server
`openssl s_server -cert sm22.cer -key sm22.key -dcert sm21.cer -dkey sm21.key -Verify 1 -CAfile sm2root.cer -port 443`
- 参数
  - -host
  - -port
  - -connect host:port
  - -key 私钥文件
  - -pass 私钥保护口令
  - -crlf 把在终端输入的换行回车转化成/r/n送出去
  - -starttls protocol：protocol可以为smtp或pop3，用于邮件安全传输

## 生成私钥
无加密:`openssl genrsa -out rsa_private.key 2048` 
DES3加密:`openssl genrsa -des3 -out rsa_des3_private.key 2048`
AES256加密:`openssl genrsa -aes256 -passout pass:123456 -out rsa_aes_private.key 2048` 
#### 对已有私钥加密解密
可以删除密码，否则每次使用都提示
解密: `openssl rsa -in rsa_aes_private.key -out rsa_private.key` or `openssl rsa -in rsa_private.key -passin pass:123456 -out rsa_aes_private.key`
加密: `openssl rsa -in rsa_aes_private.key -des3 -passout pass:123456 -out rsa_des3.key`
>在创建私钥的过程中可以指定一个密码。而这个密码会带来一个副作用，那就是在每次Apache启动Web服务器时，都会要求输入密码
## 生成公钥
`openssl rsa -in rsa_private.key -pubout -out rsa_public.key`
## 生成自签名证书
-nodes 表示私钥不加密
-newkey -keyout private_key.pem: 生成新的私钥
-subj选项可以证书信息
-x509 表示直接输出证书
-key 指定私钥文件
-pass:12345直接注入密码，否则提示输入
- 直接生成Key和根证书: 
    `openssl req -x509 rsa:2048 -nodes -newkey -keyout server.key -out cert.crt -subj "/C=CN/ST=GD/L=SZ/O=devops/OU=dev/CN=edison.tech/emailAddress=qweic@126.com"`
- 用现有Key生成根证书
    `openssl req -x509 rsa:2048 -in server.csr -signkey server.key -out cert.crt -days 365`
## 生成签名请求
-new 指生成证书请求
- 根据现有key生成csr
    `openssl req -new -key server.key -out server.csr` 
- 一键生成key和csr
    `openssl req –new rsa:2048 –nodes –newkey –keyout server.key –out server.csr -days 365`
    > 需要依次输入国家，地区，城市，组织，组织单位，Common Name和Email。其中Common Name，可以写自己的名字或者域名, 如果要支持https，Common Name应该与域名保持一致，否则会引起浏览器警告
## 格式转换
注解: -inform和-outform 参数制定输入输出格式，由der转pem格式同理
- 私钥PEM转DER: `openssl rsa -in rsa_private.key -outform der-out rsa_aes_private.der`
- X509->pfx
`openssl pkcs12 -export -out server.pfx -inkey server.key -in server.crt`
- CER->PEM
`openssl x509 -inform der -in ***pds.cer -out certificate.pem`
- p12->pub/pri
    - 生成key文件
        `openssl pkcs12 -in demo.p12 -nocerts -nodes -out demo.key`
    - 导出私钥
        `openssl rsa -in demo.key -out demo_pri.pem`
    - 导出公钥
        `openssl rsa -in demo.key -pubout -out demo_pub.pem`