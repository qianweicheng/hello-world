####参考地址：
https://dev.mysql.com/doc/refman/5.7/en/user-account-management.html
####启动/关闭
mysqld_safe
####添加账号
    CREATE USER 'root'@'%' IDENTIFIED BY 'password';
    GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'password' WITH GRANT OPTION; 
    FLUSH PRIVILEGES;
####绑定端口
netstat -tulpen
bind-address = 0.0.0.0
