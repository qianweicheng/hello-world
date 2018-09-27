##HTTP网关协议
####CGI
####FastCGI
####WSGI
####uwsgi
##Python如何与网关协议交互（Flask）
[参考文档](http://uwsgi-docs.readthedocs.io/en/latest/index.html)
pip install uwsgi
- WSGI接口: 调用__call__(environ, start_response)作为入口，Flask自带一个Webserber（werkzeug）只能做为开发使用
- FastCGI接口：flup