# Apache
## 管理
`apachctl start/stop/restart`
## 配置
- ServerRoot
    Apache的安装路径
- DocumentRoot
    它的作用是指定网站文件在服务器存放路径。DocumentRoot代表根目录
- Document
    每个目录下的配置
    代表该目录的基本属性
- Options，参考[这里](http://www.clusting.com/Apache/ApacheManual/mod/core.html#options)
    命令|说明
    -|-
    Indexes|允许目录浏览.当客户仅指定要访问的目录，但没有指定要访问目录下的哪个文件，而且目录下不存在默认文档时，Apache以超文本形式返回目录中的文件和子目录列表（虚拟目录不会出现在目录列表中
    MultiViews|允许内容协商的多重视图. MultiViews其实是Apache的一个智能特性。当客户访问目录 中一个不存在的对象时，如访问/a，则Apache会按顺序查找这个目录下所有a.*文件。
    All|All包含了除MultiViews之外的所有特性，如果没有Options语句，默认为All
    ExecCGI|允许在该目录下执行CGI脚本
    FollowSymLinks|可以在该目录中使用符号连接
    Includes|允许服务器端包含功能
    IncludesNoExec|允许服务器端包含功能，但禁用执行CGI脚本
    SymLinksIfOwnerMatch|当使用符号连接时，只有当符号连接的文件拥有者与实际文件的拥有者相同时才可以访问。
    
- 别名设置,对于不在DocumentRoot指定的目录内的页面，既可以使用符号连接，也可以使用别名。
    ```
        Alias /download/ "/var/www/download/"
        ScriptAlias /cgi-bin/ "/var/www/cgi-bin/"  
        <Directory "/usr/local/apache2/cgi-bin"> #设置目录属性 
            AllowOverride None 
            Options None 
            Order allow,deny 
            Allow from all 
        </Directory>
        <Directory "/var/www/download"> #对该目录进行访问控制设置 
            Options Indexes MultiViews 
            AllowOverride AuthConfig 
            Order allow,deny 
            Allow from all 
        </Directory>
        # case 2 网站的根目录
        DocumentRoot /www
        <Directory / > 
            Options FollowSymLinks 
            AllowOverride All 
            Order deny,allow
            Allow from all 
        </Directory> 
        <Directory /admin > 
            Options FollowSymLinks 
            AllowOverride None 
            Order allow,deny 
            Allow from all 
        </Directory> 
        <IfModule prefork.c>
            StartServers 5 #启动apache时启动的httpd进程个数。
            MinSpareServers 5 #服务器保持的最小空闲进程数。
            MaxSpareServers 10 #服务器保持的最大空闲进程数。
            MaxClients 150 #最大并发连接数。
            MaxRequestsPerChild 1000 #每个子进程被请求服务多少次后被kill掉。0表示不限制，推荐设置为1000。
        </IfModule>
    ```
- 个人主页的设置(主要在mac下开发)
    ```
    UserDir public_html 
    # 用户的主页存储在用户主目录下的public_html目录下URL 
    # http://www.clusting.com/~bearzhang/file.html 
    # 将读取 /home/bearzhang/public_html/file.html 文件
    
    chmod 755 /home/bearzhang 
    # 使其它用户能够读取该文件。 
    
    UserDir /var/html 
    # URL http://www.clusting.com/~bearzhang/file.html 
    # 将读取 /var/html/bearzhang/file.html
    
    UserDir /var/www/*/docs 
    # URL http://www.clusting.com/~bearzhang/file.html 
    # 将读取 /var/www/bearzhang/docs/file.html
    ```
## 插件
最新的Max自带的apache不能更换模块
Apache默认的模块放置在:/usr/libexec/apache2,我们可以替换
```
    # LoadModule php7_module libexec/apache2/libphp7.so
```