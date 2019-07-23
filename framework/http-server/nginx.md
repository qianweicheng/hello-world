# Nginx(http://nginx.org/en/docs/)
架设Nginx服务器(Docker)
docker run -d --name web1 -p 8080:80 nginx
/usr/share/nginx/html
架设Nginx服务器(yum)
yum -y install gcc pcre pcre-devel zlib zlib-devel openssl openssl-devel
yum install -y nginx
## Nginx Location
- 以=开头表示精确匹配
- ^~ 开头表示uri以某个常规字符串开头, 普通字符匹配，如果该选项匹配，只匹配该选项，不匹配别的选项，一般用来匹配目录
- ~ 开头表示区分大小写的正则匹配;
- ~* 开头表示不区分大小写的正则匹配
- / 通用匹配, 如果没有其它匹配,任何请求都会匹配到
顺序 no优先级:
(location =) > (location 完整匹配，直接终止匹配) > (location ^~ 路径) > (location ~,~* 正则顺序，直接终止匹配) > (location 部分起始路径，继续寻找最长匹配) > (/)

location  = / {
  >精确匹配 / ，主机名后面不能带任何字符串
  [ configuration A ] 
}
 
location  / {
  >因为所有的地址都以 / 开头，所以这条规则将匹配到所有请求
  >但是正则和最长字符串会优先匹配
  [ configuration B ] 
}

location /documents/ {
  >匹配任何以 /documents/ 开头的地址，匹配符合以后，还要继续往下搜索
  >只有后面的正则表达式没有匹配到时，这一条才会采用这一条
  [ configuration C ] 
}

location ~ /documents/ {
  >匹配任何以 /documents/ 开头的地址，匹配符合以后，还要继续往下搜索
  >只有后面的正则表达式没有匹配到时，这一条才会采用这一条
  [ configuration CC ] 
}
 
location ~* \.(gif|jpg|jpeg)$ {
  >匹配所有以 gif,jpg或jpeg 结尾的请求
  >然而，所有请求 /images/ 下的图片会被 config D 处理，因为 ^~ 到达不了这一条正则
  [ configuration E ] 
}
 
location /images/ {
  >字符匹配到 /images/，继续往下，会发现 ^~ 存在
  [ configuration F ] 
}
 
location /images/abc {
  >最长字符匹配到 /images/abc，继续往下，会发现 ^~ 存在
  >F与G的放置顺序是没有关系的
  [ configuration G ] 
}

location ^~ /images/ {
  >匹配任何以 /images/ 开头的地址，匹配符合以后，停止往下搜索正则，采用这一条。
  [ configuration D ] 
}

location ~ /images/abc/ {
   >只有去掉 config D 才有效:先最长匹配 config G 开头的地址，继续往下搜索，匹配到这一条正则，采用
   [ configuration H ] 
}

## 反向代理
location 的路径带后缀/ 表示精确匹配
proxy_pass  反向代理则有两种情况:
- 带后缀/表示绝对路径。表示代理路径会去掉location里面的值
```
  location /api {
      proxy_pass http://someserver/
  }
```
http://localhost/api/a  -> http://someserver/a
http://localhost/apixxx  -> http://someserver/xxx
- 不带后缀/表示相对路径，会把location里面的值也带入
  ```
  location /api {
      proxy_pass http://someserver
  }
  ```
  http://localhost/api/a  -> http://someserver/api/a
  http://localhost/apixxx  -> http://someserver/apixxx

前端访问->后端访问:http://localhost/api  -> Nginx 会发起一个301跳转到http://localhost/api/

## Rewirte重定向
rewrite指令执行顺序:
1.执行server块的rewrite指令(这里的块指的是server关键字后{}包围的区域，其它xx块类似)
2.执行location匹配
3.执行选定的location中的rewrite指令
如果其中某步URI被重写，则重新循环执行1-3(具体依赖Flag)，直到找到真实存在的文件
如果循环超过10次，则返回500 Internal Server Error错误
#### flag指令
- last: 本条规则匹配完成后，重头开始走一遍新的location匹配. URI规则相当于Apache里的(L)标记. 浏览器地址栏URL地址不变
- break: 本条规则匹配完成后，终止匹配，不再匹配后面的rewrite规则，但会继续执行本指令块后面的非rewrite指令. 浏览器地址栏URL地址不变
  作用域:server,location,if
- redirect: 返回302临时重定向，浏览器地址会显示跳转后的URL地址 
- permanent:返回301永久重定向，浏览器地址栏会显示跳转后的URL地址 
  Ex: rewrite  ^/(.*)$  http://abc.com/$1  permanent;
- return 作用域: server,location,if
## FastCGI
fastcgi_params
```
  fastcgi_pass   127.0.0.1:9000;
  fastcgi_index  index.php;
  include        fastcgi_params;
  #定义变量 $path_info ，用于存放pathinfo信息
  set $path_info "";
  #定义变量 $real_script_name，用于存放真实地址
  set $real_script_name $fastcgi_script_name;
  #如果地址与引号内的正则表达式匹配
  if ($fastcgi_script_name ~ "^(.+?\.php)(/.+)$") {
        #将文件地址赋值给变量 $real_script_name
        set $real_script_name $1;
        #将文件地址后的参数赋值给变量 $path_info
        set $path_info $2;
  }
  #配置fastcgi的一些参数
  fastcgi_param SCRIPT_FILENAME $document_root$real_script_name;
  fastcgi_param SCRIPT_NAME $real_script_name;
  fastcgi_param PATH_INFO $path_info;
  fastcgi_param X-HEADER  Weicheng;
```
## 其他
避免触发后端的AUTH
proxy_set_header Authorization "";
add_header X-Upstream weicheng always;
## [内置变量](http://nginx.org/en/docs/http/ngx_http_core_module.html#location)

## Cache
https://linux.cn/article-5945-1.html
Expires: 最原始的配置策略，即设置过期时间，但使用效率低下，目前绝大部分使用Cache-Control
Cache-Control:定义缓存资源属性是private或者是public
X-Accel-Expires: 只有nginx能识别的缓存特性header，优先级大于上面两个header
Etag和Last-Modified是捆绑生成的:有些场景下，你希望client端的浏览器长时间缓存，而缓存服务器只短时间缓存文件，以至于当后端服务器更新后，缓存服务器会及时同步

#### 代理上的缓存设置
默认不开启
- proxy_cache_path
- proxy_cache_key
- proxy_cache_min_uses
- proxy_cache_methods
- proxy_cache_valid 绝对缓存时间，不管inactive是否到期，即使访问很频繁，也会被删除
- proxy_cache_revalidate:指示NGINX在刷新来自服务器的内容时使用GET请求。如果客户端的请求项已经被缓存过了，但是在缓存控制头部中定义为过期
- proxy_cache_bypass
- proxy_no_cache
- proxy_cache_purge 缓存清除时间
- proxy_set_header
- proxy_intercept_errors(fastcgi_intercept_errors)
#### 浏览器上的缓存
对于静态资源来说，浏览器不会缓存html页面的，所以你每次改完html的页面的时候，html都是改完立即生效的。浏览器缓存的东西有图片，css和js。这些资源将在缓存失效前调用的时候调用浏览器的缓存内容, 200(From memory) or 200(From disk). expires到期则发送携带If-Modified-Since/If-no-match头的请求(很可能304回来)
- expires   3d;
- add_header Cache-Control no-store;
## error_page
```
error_page  404 403 500 502 503 504  /404.html;
error_page 502 503 =200 /50x.html;#加了code
location = /404.html {
}
```
## HTTP to HTTPS
- rewrite
- error_page 497  https://$host$uri?$args; 
- HTML
```
<html> 
<meta http-equiv="refresh" content="0;url=https://dev.wangshibo.com/"> 
</html>
```
## 内部跳转，外部无法直接访问
- 添加internal
  ```
    location ~ \.png$ {
        internal
    }
  ```
- Named Location,只能被Nginx内部配置指令所访问(@)
  ```
    location @abc {
        internal
    }
  ```
## alias vs root
```
location /i/ {
  alias /data/w3/;
}
```
```
location /i/ {
  root /data/w3;
}
```
- alias 只能作用在location中，而root可以存在server、http和location中。
- alias 后面必须要用 “/” 结束，否则会找不到文件，而 root 则对 ”/” 可有可无。

## Nginx 内部11个阶段
参考:
https://www.cnblogs.com/lidabo/p/4171664.html
- NGX_HTTP_POST_READ_PHASE = 0, // 接收到完整的HTTP头部后处理的阶段
- NGX_HTTP_SERVER_REWRITE_PHASE, // URI与location匹配前，修改URI的阶段，用于重定向
- NGX_HTTP_FIND_CONFIG_PHASE, // 根据URI寻找匹配的location块配置项
- NGX_HTTP_REWRITE_PHASE, // 上一阶段找到location块后再修改URI
- NGX_HTTP_POST_REWRITE_PHASE, // 防止重写URL后导致的死循环
- NGX_HTTP_PREACCESS_PHASE, // 下一阶段之前的准备
- NGX_HTTP_ACCESS_PHASE, // 让HTTP模块判断是否允许这个请求进入Nginx服务器
- NGX_HTTP_POST_ACCESS_PHASE, // 向用户发送拒绝服务的错误码，用来响应上一阶段的拒绝
- NGX_HTTP_TRY_FILES_PHASE, // 为访问静态文件资源而设置
- NGX_HTTP_CONTENT_PHASE, // 处理HTTP请求内容的阶段，大部分HTTP模块介入这个阶段
- NGX_HTTP_LOG_PHASE // 处理完请求后的日志记录阶段
## Nginx 模块
- ngx_http_core_module
- ngx_http_headers_module
  ```
    add_header
    add_trailer
    expires
  ```
- ngx_http_index_module: 根据设置显示首页
- ngx_http_autoindex_module: 目录显示
- ngx_http_random_index_module: 随机挑选一个显示
- ngx_http_log_module:设置日记
- ngx_http_map_module:只在使用了该变量的location计算
  ```
    map $url $myvar {
      ~^/hello/(.*)   greet
    }
  ```
- ngx_http_proxy_module
- ngx_http_rewrite_module

## status
stub_status
## 其他网络配置
- tcp_nopush sendfile
- tcp_nodelay 反向代理的时候不缓存，直接发送
## IF 
- 没有else
- ==:等值比较;
- ~：与指定正则表达式模式匹配时返回“真”，判断匹配与否时区分字符大小写；
- ~*：与指定正则表达式模式匹配时返回“真”，判断匹配与否时不区分字符大小写；
- !~：与指定正则表达式模式不匹配时返回“真”，判断匹配与否时区分字符大小写；
- !~*：与指定正则表达式模式不匹配时返回“真”，判断匹配与否时不区分字符大小写；
- -f, !-f：判断指定的路径是否为存在且为文件；
- -d, !-d：判断指定的路径是否为存在且为目录；
- -e, !-e：判断指定的路径是否存在，文件或目录均可；
- -x, !-x：判断指定路径的文件是否存在且可执行；
## 正向代理
1. 增加dns解析resolver
2. 增加无server_name名的server
3. proxy_pass指令
4. nginx代理服务不支持正向代理HTTPS站点。
```
server {
  resolver 192.168.1.1; #指定DNS服务器IP地址
	listen 8080;
	location / {
		proxy_pass http://$http_host$request_uri; #设定代理服务器的协议和地址
  }
}
```

