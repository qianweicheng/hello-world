# MYSQL
 参考地址：
https://dev.mysql.com/doc/refman/5.7/en/user-account-management.html
## 常用命令
启动/关闭: mysqld_safe
创建数据库: `mysqladmin create databasename;` or `mysql -u root -p databasename < db.sql`
导出数据: `mysqldump -uroot -p [--databases dbname] > mysql.test`
导入数据: `mysqlimport -uroot -p < mysql.dbname`
优化(周期运行): `OPTIMIZE TABLE`
## 授权
- 创建用户: `CREATE USER 'username'@'host' IDENTIFIED BY 'password';`
- 授权: 
    `GRANT privileges ON db.tablename TO 'username'@'host'`
    `GRANT privileges ON db.tablename TO 'username'@'host' WITH GRANT OPTION;`
    - privileges：用户的操作权限，如SELECT，INSERT，UPDATE等，如果要授予所的权限则使用ALL
    - db和tablename：可以使用*代替,如: db.*, *.* 
- 刷新授权
    `FLUSH PRIVILEGES;`
- 撤销授权: `REVOKE privilege ON db.tablename FROM 'username'@'host';`
- 修改密码: `SET PASSWORD FOR 'username'@'host' = PASSWORD('newpassword');`
- 删除用户: `DROP USER 'username'@'host';`
> 废弃: GRANT 如果用户不存在，则会根据配置NO_AUTO_CREATE_USER直接创建用户[非常不安全]； 如果GRANT后面跟了IDENTIFIED BY，则会把所有的密码修改，包括登陆密码。
## 绑定端口
netstat -tulpen
bind-address = 0.0.0.0

