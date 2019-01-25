# CERT
公钥和私钥存储有几个规范：http://blog.csdn.net/tuhuolong/article/details/42778945
- PKCS#8 私钥加密格式：-----BEGIN ENCRYPTED PRIVATE KEY-----  
- PKCS#8 私钥非加密格式：-----BEGIN PRIVATE KEY-----  
- Openssl ASN格式：-----BEGIN RSA PRIVATE KEY-----  

## 生成证书
1）ssh-keygen -t rsa -C "your_email@example.com"
2）openssl req -x509 -nodes -days 365 -sha256 -newkey rsa:2048 -keyout mycert.pem -out mycert.pem

## 免登录
把公钥拷贝到远程服务器：ssh-copy-id -i id_rsa.pub ec2-user@remote-server
其实就是把公要拷贝到远程机器的~/.ssh/authorized_keys中

## RSA私钥可以生成公钥
如下两个方式生成的公钥格式不一样
openssl rsa -in myprivate.pem -pubout > mypublic-key.pem
ssh-keygen -y [-f input_keyfile]  

## 登陆
ssh -i private.key user@remote
此处的private.key 可以是xxx.pem/id_rsa

通过配置~/.ssh/config简化登陆，添加一节
Host    alias(注意缩进)
    HostName        主机名
    Port            端口
    User            用户名
    IdentityFile    密钥文件的路径
使用如下：
ssh alias [cmd]
scp alias src dst

ssh -i ~/.ssh/id_rsa_aws ec2-user@ec2-34-214-36-232.us-west-2.compute.amazonaws.com
ssh -i ~/.ssh/id_rsa_k8s ec2-user@ec2-34-214-36-232.us-west-2.compute.amazonaws.com
ssh -i ~/.ssh/id_rsa admin@34.213.212.68

