# uwsgi
- 在项目里面`uwsgi --ini xxx.ini`
- 在nginx配置反向代理
`
uwsgi_pass unix:///tmp/uwsgi.sock;
include uwsgi_params;
## https://uwsgi-docs.readthedocs.io/en/latest/Nginx.html
