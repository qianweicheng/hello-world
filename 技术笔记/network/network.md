## 端口占用(Linux)
#### lsof
- 查看xxx文件的使用情况: lsof xxx
- 查看xxx文件夹的使用情况：lsof +d xxx
- 查看xxx文件夹的使用情况(递归)：lsof +D xxx
- 查看进程(名字开头的)使用的文件状况：lsof -c xxx 
- 查看进程(pid)使用的文件状况2:lsof -p xxx
- 查看所有打开端口：lsof -i
- 查看特定端口使用情况：lsof -i:xxx
    xxx格式 [46][protocol][@hostname|hostaddr][:service|port]
    lsof -i tcp@ohaha.ks.edu.tw:ftp -r 
#### netstat
- 列出所有监听状态的： -l 
- 列出所有tcp： -t
- 列出所有pid： -p
- 列出所有： -a
- 路由其信息： -r
- 持续输出：-c
- 统计信息：-s
- 显示网络接口： -i
- 禁止域名反查： -n
#### netcat(nc)
启动服务端： nc -l [port]
启动客户端： nc host port
- 端口扫描：
    nc -z hostname 80-90
    tips：可以指定-w和发送一个通用消息探测服务器类型
    Ex: echo "QUIT" | nc host.example.com 20-30
- 指定客户端端口： 
    -p xxx
    -r 随机
- 指定本机使用出口ip
    -s addr
- 指定udp协议： -u
- 指定超时秒： -w xxx
- 输出详情: -v
#### 域名解析 host/nslookup/dig
>nslookup和dig需要安装额外包：bind-utils
apt-get install -y bind-utils
yum install -y bind-utils
host domain 
 
dig [+short] domain
nslookup domain

#### telnet

## 端口转发
详情见ssh.md