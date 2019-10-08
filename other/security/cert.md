# Certificate(CERT)
## Public-Key Cryptography Standards(PKCS)标准.
PKCS目前共发布过15个标准。常用的有：
- PKCS#1
- PKCS#7: 这种主要是用于签名或者加密。
- PKCS#8
- PKCS#12: 这种含有私钥，同时也含有公钥，但是有口令保护
## 证书存储格式
X509,pfx/p12
#### x509
X.509是常见通用的证书格式
X.509 DER 编码(ASCII/二进制)的后缀是： .DER .CER .CRT(选择何种系平台风格)
X.509 PAM 编码(Base64)的后缀是： .PEM .CER .CRT
这种证书只有公钥，不包含私钥。X.509证书包含三个文件：key，csr，crt。
- key是服务器上的私钥文件，用于对发送给客户端数据的加密，以及对从客户端接收到数据的解密
- csr是证书签名请求文件，用于提交给证书颁发机构（CA）对证书签名
- crt,cer是由证书颁发机构（CA）签名后的证书，或者是开发者自签名的证书，包含证书持有人的信息，持有人的公钥，以及签署者的签名等信息
#### pfx/p12
用于存放个人证书/私钥
## 公钥和私钥存储有几个规范
http://blog.csdn.net/tuhuolong/article/details/42778945