# CERT
公钥和私钥存储有几个规范：http://blog.csdn.net/tuhuolong/article/details/42778945
- PKCS#8 私钥加密格式：-----BEGIN ENCRYPTED PRIVATE KEY-----  
- PKCS#8 私钥非加密格式：-----BEGIN PRIVATE KEY-----  
- Openssl ASN格式：-----BEGIN RSA PRIVATE KEY-----  

## 生成证书
1）ssh-keygen -t rsa -C "cy-weicheng"
2）openssl req -x509 -nodes -days 365 -sha256 -newkey rsa:2048 -keyout mycert.pem -out mycert.pem

## RSA私钥可以生成公钥
如下两个方式生成的公钥格式不一样
openssl rsa -in myprivate.pem -pubout > mypublic-key.pem
ssh-keygen -y [-f input_keyfile]