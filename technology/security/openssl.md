# Openssl命令
分三大块:
- 标准命令 如: ca,gendsa,genpkey,genrsa,pkcs8,req,rsa,x509等
- 数字签名 如: md5,sha256等
- 对称加密 如: aes-256-cbc,base64,des,des3等
## 生成私钥
无加密:`openssl genrsa -out rsa_private.key 2048` 
DES3加密:`openssl genrsa -des3 -out rsa_des3_private.key 2048`
AES256加密:`openssl genrsa -aes256 -passout pass:111111 -out rsa_aes_private.key 2048` 
(pass:111111直接注入密码，否则提示输入)
## 私钥加密解密
可以删除密码，否则每次使用都提示
解密: `openssl rsa -in rsa_aes_private.key -out rsa_private.key`
加密: `openssl rsa -in rsa_private.key -passin pass:111111 -out rsa_aes_private.key`
>在第1步创建私钥的过程中，由于必须要指定一个密码。而这个密码会带来一个副作用，那就是在每次Apache启动Web服务器时，都会要求输入密码
## 生成公钥
`openssl rsa -in rsa_private.key -pubout -out rsa_public.key`
## 生成自签名证书
-nodes 表示私钥不加密
-newkey -keyout private_key.pem: 生成新的私钥
-subj选项可以证书信息
-x509 表示直接输出证书
-key 指定私钥文件
`openssl req -x509 rsa:2048 -nodes -newkey -keyout rsa_private.key -out cert.crt -subj "/C=CN/ST=GD/L=SZ/O=vihoo/OU=dev/CN=vivo.com/emailAddress=qweic@126.com"`
`openssl req -x509 rsa:2048 -in server.csr -signkey server.key -out cert.crt -days 365 `(用现有Key)
## 生成签名请求以及CA签名
-new 指生成证书请求
`openssl req -new -key server.key -out server.csr`
`openssl req –new rsa:2048 –nodes –newkey –keyout rsa_private.key –out server.csr -days 365`
> 需要依次输入国家，地区，城市，组织，组织单位，Common Name和Email。其中Common Name，可以写自己的名字或者域名, 如果要支持https，Common Name应该与域名保持一致，否则会引起浏览器警告
## 格式转换
注解: -inform和-outform 参数制定输入输出格式，由der转pem格式同理
- 私钥PEM转DER: `openssl rsa -in rsa_private.key -outform der-out rsa_aes_private.der`
