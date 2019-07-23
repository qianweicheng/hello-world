# 代理
## HTTP Proxy
- 第一种是 RFC 7230 - HTTP/1.1: Message Syntax and Routing（即修订后的 RFC 2616，HTTP/1.1 协议的第一部分）描述的普通代理。这种代理扮演的是「中间人」角色，对于连接到它的客户端来说，它是服务端；对于要连接的服务端来说，它是客户端。它就负责在两端之间来回传送 HTTP 报文。
- 第二种是 Tnneling TCP based protocols through Web proxy servers（通过 Web 代理服务器用隧道方式传输基于 TCP 的协议）描述的隧道代理。它通过 HTTP 协议正文部分（Body）完成通讯，以 HTTP 的方式实现任意基于 TCP 的应用层协议代理。这种代理使用 HTTP 的 CONNECT 方法建立连接，但 CONNECT 最开始并不是 RFC 2616 - HTTP/1.1 的一部分，直到 2014 年发布的 HTTP/1.1 修订版中，才增加了对 CONNECT 及隧道代理的描述，详见 RFC 7231 - HTTP/1.1: Semantics and Content。实际上这种代理早就被广泛实现。
## Socks5

## 常见软件代理设置方法
#### 环境变量法 
**brew, wget, curl, pip**等很多软件默认会根据系环境变量`all_proxy`(**推荐**),`http_proxy`,`https_proxy`或`ftp_proxy`决定是否使用代理(并使用`no_proxy`忽略指定Host).
all_proxy可以为socks5或者http。 http(s)_proxy**只能**使用http(s)代理, 有无`s`没有什么影响.HTTP代理需要shadowsocks-ng开启(默认开启)，因此我们可以设置如下其中之一的环境变量
- socks5代理(推荐):  export all_proxy=socks5://127.0.0.1:1086
- http代理:         export http_proxy=http://127.0.0.1:1087
- https代理:        export https_proxy=$http_proxy  # 可以跟http一样
- ftp_proxy代理:    export http_proxy=$http_proxy
- all_proxy代理:    export all_proxy=$http_proxy

步骤:
1. 编辑:`~/.bash_profile`,添加上`export all_proxy=socks5://127.0.0.1:1086`:
2. 使之生效: `source ~/.bash_profile`
#### npm
如下方法之一:
- `npm config set proxy http://server:port`
- `npm config set https-proxy http://username:pawword@server:port`
#### 浏览器, IDE, Postman等
可以通过自身设置页面配置