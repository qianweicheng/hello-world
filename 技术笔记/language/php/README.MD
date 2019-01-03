# PHP
## 部署方式
- apache+php:
    PHP 使用Apache相对方便些，但MacOS里面只能使用自带的php库，无法替换
- nginx+php-fpm+php
    可以自行安装任意版本，必须手动额外启动php-fpm(php自带)
    如：`brew install php56`
    查看PHP加载的配置文件:`php --ini`,或`phpinfo()`
## ThinkPHP URL Rewirte
值为0   叫做普通模式。如：http://localhost/index.php?m=模块&a=方法
值为1   叫做pathinfo模式。如：http://localhost/index.php/模块/方法
值为2   叫做rewrite重写（伪静态） 可以自己写相关的rewrite规则，也可以使用系统为我们提供的rewrite规则隐藏掉index.php，生成：http://localhost/模块/方法
值为3   叫做兼容模式。当服务器上面不支持pathinfo模式的时候，但是你又在之前的路径访问格式上面，全部用的是pathinfo格式。那么它会提示你路径格式不正确。那么，你就可以用标号为3的兼容模式来处理。它的路径访问类似于http://localhost/index.php?s=模块/方法 