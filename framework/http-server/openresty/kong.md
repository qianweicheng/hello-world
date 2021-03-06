# Kong
一个插件平台，本身是一个Openstry的插件。
一个基于openrestry的app
官网: 
https://konghq.com/
https://hub.docker.com/_/kong/
https://github.com/PGBI/kong-dashboard
## 核心概念
- API(废弃)
    upstream_url: 后端url(http://192.168.2.109:8080)
    uris: 前端url(/abc)
- Service
- Router: service的入口
    这里的配置都是关于前端的，通过service_id关联入口
- Plugins: 可以关联API，Service或者Router
- Consumers:
    相当于一个账户组，里面可以有N个账户
- Upstreams:
## 启动
- docker的启动脚本
```
    kong prepare -p $PREFIX #生成nginx.conf
    exec /usr/local/openresty/nginx/sbin/nginx ...
```
- 直接启动: `kong start [-c /path/to/kong.conf]`
## 解析
kong也是个helper：`/usr/local/openresty/bin/resty xxx`
1. `/usr/local/kong`读取配置`/etc/kong/kong.conf`通过模版生成`/usr/local/kong/nginx.conf`
1. 启动openresty：`/usr/local/openresty/nginx/sbin/nginx -p /usr/local/kong -c nginx.conf`
## 插件加载路径
- luarocks包安装路径：`/usr/local/share/lua/5.1/`
    kong等第三方插件安装在此
- Openresty核心库:
    `/usr/local/openresty/lualib/resty/`
- Openresty插件
    ```
        /usr/local/share/lua/5.1/?.lua;
        /usr/local/share/lua/5.1/?/init.lua;
    ```
    Kong plugins:`/usr/local/share/lua/5.1/kong/plugins/`
- Jit相关
    ```
        /usr/local/openresty/luajit/share/luajit-2.1.0-beta3/?.lua;
        /usr/local/openresty/luajit/share/lua/5.1/?.lua;
        /usr/local/openresty/luajit/share/lua/5.1/?/init.lua
    ```
- 工作目录:`./?.lua;`
## 其他目录
包管理器: 
- opm: openresty自带
- luarocks: 通用的lua包管理器
## 插件开发
#### 参考文档
- kong 插件开发: https://docs.konghq.com/1.1.x/plugin-development/distribution/
- kong demo: https://github.com/Kong/kong-plugin
- 我的插件: https://github.com/qianweicheng/kong-redirect
- rock: https://github.com/luarocks/luarocks/wiki/Creating-a-rock
#### API
kong.log vs ngx.log
kong.log("hello ", "world") -- alias to kong.log.notice()
