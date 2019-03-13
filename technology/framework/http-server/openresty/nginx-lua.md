# nginx lua
![流程图](流程图.png)
## 常见函数
- init_by_lua
- init_worker_by_lua            
- set_by_lua             流程分支处理判断变量初始化(server, server if, location, location if)
- ssl_certificate_by_lua
- rewrite_by_lua         转发、重定向、缓存等功能(例如特定请求代理到外网)(http, server, location, location if)
- access_by_lua          IP准入、接口权限等情况集中处理(例如配合iptable完成简单防火墙)(http, server, location, location if)
- content_by_lua         内容生成(location, location if)
- balancer_by_lua
- header_filter_by_lua   应答HTTP过滤处理(例如添加头部信息)(http, server, location, location if)
- body_filter_by_lua     应答BODY过滤处理(例如完成应答内容统一成大写)(http, server, location, location if)
- log_by_lua             会话完成后本地异步完成日志记录(日志可以记录在本地，还可以同步到其他机器)(http, server, location, location if)
- echo_location