# SSH
## 服务端（/etc/ssh/sshd_config）
#### 开启密码登录
- PasswordAuthentication 改为 yes
- 添加/修改密码`passwd [username]`
- 重启生效 `service sshd restart`

#### 挂载远程目录
sshfs dev-stag:/home/ec2-user ./dev-stag
#### 端口转发
-   动态端口转发（在本机运行）,也叫：ssh socks代理
    >ssh -Nf -D local_A_port ssh-proxy-server
    Ex: ssh -fN -D 8080 ssh-proxy-server
    Ex: ssh -qTfnN -D 7070 username@xxxx.com
    ssh -i ~/bin/us-west-2.pem.pem -fqTnN -D 1080 ec2-user@aws-admin
-   本地端口转发-L （在本机运行）前提是远程可以连入
    >ssh -Nf -L [local_A_address]:local_A_port:target_C_server:target_C_port ssh-proxy-server
    Ex: ssh -fN -L 8080:target-host:80 ssh-proxy-server
-   远程端口转发（在跳板机运行）远程主机主动连接出来,主要运用于A不能主动连接B但反之可以
    >ssh -fNR [local_A_address]:local_A_port:target_C_server:target_C_port ssh-proxy-server
    Ex: ssh -fNR 52.43.115.194:8080:127.0.0.1:80  remote-host
    注1：此处的local_A_address 是相对于ssh-proxy-server的来说的，不是本机。
    注2: 由于安全性，sshd默认只能服务器本地转发。开启全局：`/etc/ssh/sshd_config`中修改`GatewayPorts yes`
    本地端口转发和远程端口转发，其实都可看着是动态端口转发(代理)的子集；
#### Banner
- 在登录前显示: 修改/etc/ssh/sshd_config `Banner /etc/issue.net`。 如果登录非常快，则可能不可见，并且对于nologin的用户不可见
- 在进入SHELL后显示: 添加脚本在 `/etc/update-motd.d/`, 并且修改:`PrintMotd no`
## 客户端配置（~/.ssh/config）：
    ControlMaster auto
    ControlPath ~/.ssh/%h-%p-%r
    ControlPersist yes
    keep alive
    ServerAliveInterval 60 
    ServerAliveCountMax 3 
    Host alias(注意缩进)
            IdentityFile ~/.ssh/us-west-2.pem.pem
            User ec2-user
            HostName 52.43.115.194
            Port            端口

## 免登录
把公钥拷贝到远程服务器：ssh-copy-id -i id_rsa.pub ec2-user@remote-server
其实就是把公要拷贝到远程机器的~/.ssh/authorized_keys中

## 登陆
ssh -i private.key user@remote
此处的private.key 可以是xxx.pem/id_rsa

## Tools使用如下：
- scp
    `scp alias src dst`
  -  -r 拷贝文件夹
  
## Log(/var/log/secure)
`sudo grep "Failed password for root" /var/log/secure | awk '{print $11}' | sort | uniq -c | sort -nr | more`
## 安全
- 禁止某个ip: /etc/hosts.deny
    ```/etc/hosts.deny
        sshd: 192.168.1.0/255.255.255.0
        sshd: 192.168.0.1
    ```
- 允许某个ip: /etc/hosts.allow
