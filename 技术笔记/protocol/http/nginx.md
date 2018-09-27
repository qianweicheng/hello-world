#### http://nginx.org/en/docs/
架设Nginx服务器(Docker)
docker run -d --name web1 -p 80:80 nginx
/usr/share/nginx/html
架设Nginx服务器(yum)
yum -y install gcc pcre pcre-devel zlib zlib-devel openssl openssl-devel
yum install -y nginx
#### 其他
避免触发后端的AUTH
proxy_set_header Authorization "";
add_header X-Upstream weicheng always;
####rewrite重定向
- last: 本条规则匹配完成后，继续向下匹配新的location. URI规则相当于Apache里的(L)标记. 浏览器地址栏URL地址不变
- break；本条规则匹配完成后，终止匹配，不再匹配后面的规则. 浏览器地址栏URL地址不变
- redirect：返回302临时重定向，浏览器地址会显示跳转后的URL地址 
- permanent：返回301永久重定向，浏览器地址栏会显示跳转后的URL地址 
  Ex: rewrite  ^/(.*)$  http://abc.com/$1  permanent;
####Nginx Location
以=开头表示精确匹配
^~ 开头表示uri以某个常规字符串开头
~ 开头表示区分大小写的正则匹配;
~* 开头表示不区分大小写的正则匹配
/ 通用匹配, 如果没有其它匹配,任何请求都会匹配到
顺序 no优先级：
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

location ~ /documents/Abc {
  >匹配任何以 /documents/ 开头的地址，匹配符合以后，还要继续往下搜索
  >只有后面的正则表达式没有匹配到时，这一条才会采用这一条
  [ configuration CC ] 
}
 
location ^~ /images/ {
  >匹配任何以 /images/ 开头的地址，匹配符合以后，停止往下搜索正则，采用这一条。
  [ configuration D ] 
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
 
location ~ /images/abc/ {
   >只有去掉 config D 才有效：先最长匹配 config G 开头的地址，继续往下搜索，匹配到这一条正则，采用
   [ configuration H ] 
}

####反向代理
location 的路径带后缀/ 表示精确匹配
proxy_pass  反向代理， 如果带后缀/，表示代理路径会去掉location里面的值，否则会把location里面的值也带入
location /api {
    proxy_pass http://someserver/
}
前端访问->后端访问：http://localhost/api/a  -> http://someserver/a
前端访问->后端访问：http://localhost/apixxx  -> http://someserver/xxx
前端访问->后端访问：http://localhost/api  -> Nginx 会发起一个301跳转到http://localhost/api/

location /api {
    proxy_pass http://someserver
}
前端访问->后端访问：http://localhost/api/a  -> http://someserver/api/a
前端访问->后端访问：http://localhost/apixxx  -> http://someserver/apixxx
前端访问->后端访问：http://localhost/api  -> Nginx 会发起一个301跳转到http://localhost/api/

location /api/ {
    proxy_pass http://someserver/;
}
前端严格匹配 /api/,其他同上
如果需要省略'/'，可以前面加'='
location = /api {
    proxy_pass http://someserver/;
}