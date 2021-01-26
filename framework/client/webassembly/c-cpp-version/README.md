# WebAssembly
## Document
https://webassembly.org/
https://emscripten.org/
https://hub.docker.com/r/emscripten/emsdk
https://www.cntofu.com/book/150/readme.html

https://github.com/gorilla/websocket
https://github.com/novnc/websockify
https://github.com/novnc/websockify-other
https://github.com/novnc/websockify-js

## Install
```
git clone https://github.com/emscripten-core/emsdk.git

cd emsdk

# Download and install the latest SDK tools.
./emsdk install latest

# Make the "latest" SDK "active" for the current user. (writes .emscripten file)
./emsdk activate latest

# Activate PATH and other environment variables in the current terminal
source ./emsdk_env.sh
```
## 纯粹端口转发试验
开启本地端口9000，把所有流量纯粹的转发到python.org:443  整个过程本地只做隧道代理，没有涉及任何证书和协议转换，证书也不存在验证错误
```Shell 1
mkdir /tmp/fifo
cat fifo | nc python.org 443 | nc -l 9000 > fifo
```
```Shell 2
openssl s_client -connect localhost:9000 -crlf
GET / HTTP/1.1
HOST: python.org
<这里有个回车>
```
## Telnet 收邮件
前提：`git clone https://github.com/novnc/websockify` or `git clone https://github.com/novnc/websockify-js`
1. 打开代理: `./run 8001 imap.126.com:143`
2. 开启本地nginx服务器，配置好
3. 打开网页: `/ws/wstelnet.html`进行测试
## Telnet 聊天
1. 打开服务器: `nl -l 8080`
2. 打开代理: `./run 8001 localhost:8080`
3. 打开网页: `/ws/wstelnet.html`


## 说明
js库：https://github.com/mscdex/node-imap
rust库：https://github.com/jonhoo/rust-imap
原型代理服务器：https://github.com/novnc/websockify 或者 https://github.com/novnc/websockify-js
运行代理服务器：  ./websockify local-port  remote-host:remote-port