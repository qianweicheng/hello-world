## HTTP网关协议
#### CGI
    Web服务器接收到请求后，启动CGI程序，每次处理一个请求都新建一个进程。CGI采用的是“fork-and-execute”的工作模式，其缺点在于：效率低下，每个请求都需要fork一个新的CGI进程去处理。当请求量增大时服务器很快将被压垮。
#### FastCGI
    详情分析,[参考这里](https://blog.csdn.net/hepangda/article/details/81560515)
    Web服务器启动时，初始化FastCGI执行环境，FastCGI进程管理器自身初始化，启动多个CGI解释器进程并等待来自Web服务器的连接
    与CGI“fork-and-execute”的工作模式不同，FastCGI像是一个常驻型的CGI，它使用持续的进程来处理一连串的请求。这些进程由FastCGI进程管理器管理，而不是Web服务器。当进来一个请求时，Web服务器把环境变量和这个页面请求通过一个unix domain socket（比如FastCGI进程与Web服务器都位于本地）或者一个TCP连接（FastCGI进程部署在远端）传递给FastCGI进程。
#### WSGI
    当Web服务器接收到一个请求后，可以通过Socket把环境变量和一个callback回调函数传递给后端Web应用程序，Web应用程序处理完成后，调用callback函数，把结果返回给WebServer。
#### scgi
它是FCGI在精简数据协议和响应过程后的产物。其设计目的是为了适应越来越多基于AJAX或REST的HTTP请求，而做出更快更简洁的应答。并且SCGI约定，当服务器返回对一个HTTP协议请求响应后，立刻关闭该HTTP连接。所以不难看出，SCGI更加适合于普遍意义上SOA所提倡的“请求-忘记”这种通信模式。
#### uwsgi
## Python如何与网关协议交互（Flask）
[参考文档](http://uwsgi-docs.readthedocs.io/en/latest/index.html)
pip install uwsgi
- WSGI接口: 调用__call__(environ, start_response)作为入口，Flask自带一个Webserber（werkzeug）只能做为开发使用
- FastCGI接口：flup
## 为什么不直接使用反向代理(proxy_pass)
- 好处：
    - 可阅读，容易调试，最熟悉HTTP协议
    - 成熟的工具多，生态好，整个链路都是HTTP协议
- 缺点：
    - 后端获取客户端的，IP， 本机的Host Name等没有那么直观（通过X-Forwarded-For)
    - 效率稍差