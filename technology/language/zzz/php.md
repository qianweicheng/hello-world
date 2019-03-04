# PHP
## 安装
Mac下目前并存了3个版本的PHP
- PHP7.1：Mac自带，存放在`/usr/bin/php`,`/usr/sbin/php-fpm`，默认从`/etc/php.ini`和`/etc/php-fpm.conf`中读取配置信息
- PHP5.6: 
    brew安装，`brew install php56`.
    存放在`/usr/local/Cellar/php@5.6/...`, 默认在`/usr/local/etc/`下读取配置信息
- PHP7.3: 
    brew安装，`brew install php`.
    存放在`/usr/local/Cellar/php/...`
## 部署方式
- 直接运行
    root path 为当前文件夹: `php -S 0.0.0.0:9000`
    注意选择php的版本号,查看PHP加载的配置文件:`php --ini`,或`phpinfo()`
- apache+php:
    * MacOS里面只能使用自带的php库，无法替换
- nginx+php-fpm
    * 可以自行安装任意版本php，必须手动额外启动php-fpm(php自带)
- uWSGI
    [参考](https://uwsgi-docs-zh.readthedocs.io/zh_CN/latest/PHP.html)
    `UWSGICONFIG_PHPDIR=/opt/php51 python uwsgiconfig.py --plugin plugins/php default php56`
## ThinkPHP URL Rewirte
值为0   叫做普通模式。如：http://localhost/index.php?m=模块&a=方法
值为1   叫做pathinfo模式。如：http://localhost/index.php/模块/方法
值为2   叫做rewrite重写（伪静态） 可以自己写相关的rewrite规则，也可以使用系统为我们提供的rewrite规则隐藏掉index.php，生成：http://localhost/模块/方法
值为3   叫做兼容模式。当服务器上面不支持pathinfo模式的时候，但是你又在之前的路径访问格式上面，全部用的是pathinfo格式。那么它会提示你路径格式不正确。那么，你就可以用标号为3的兼容模式来处理。它的路径访问类似于http://localhost/index.php?s=模块/方法 