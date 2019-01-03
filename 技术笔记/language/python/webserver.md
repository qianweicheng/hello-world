# Python Web Server
## uwsgi
[文档](https://uwsgi-docs.readthedocs.io/en/latest/Nginx.html)
1. 在项目里面`uwsgi --ini xxx.ini`
2. 在nginx配置反向代理
```
    uwsgi_pass unix:///tmp/uwsgi.sock;
    include uwsgi_params;
```
## gunicorn


