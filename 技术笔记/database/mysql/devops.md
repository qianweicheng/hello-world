#### 参考地址：
https://dev.mysql.com/doc/refman/5.7/en/user-account-management.html
#### 启动/关闭
mysqld_safe
#### 添加账号
    CREATE USER 'root'@'%' IDENTIFIED BY 'password';
    GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'password' WITH GRANT OPTION; 
    FLUSH PRIVILEGES;
#### 绑定端口
netstat -tulpen
bind-address = 0.0.0.0
####
mysqladmin create databasename;
mysql -u root -p databasename < db.sql 


grant all privileges on solrclient.* to suse@localhost identified by 'suse‘;
grant select,update on phplampDB.* to phplamp@localhost identified by '1234';  
FLUSH PRIVILEGES;

source /opt/openfire/resources/database/openfire_mysql.sql;
grant all on openfire.* to admin@"%" identified by 'admin';

1. 导出数据：

mysqldump --opt test > mysql.test

即将数据库test数据库导出到mysql.test文件，后者是一个文本文件

如：mysqldump -u root -p123456 --databases dbname > mysql.dbname

就是把数据库dbname导出到文件mysql.dbname中。

2. 导入数据:

mysqlimport -u root -p123456 < mysql.dbname。