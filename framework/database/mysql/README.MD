# MYSQL
 参考地址：
https://dev.mysql.com/doc/refman/5.7/en/user-account-management.html
## Install
```Server
docker run \
--name mysql \
-p 3306:3306 \
-e MYSQL_ROOT_PASSWORD=A1234567 \
-d mysql:latest \
--character-set-server=utf8mb4 \
--collation-server=utf8mb4_unicode_ci
```
```
docker run 
-it
--rm
mysql
mysql -hsome-mysql -uroot -p
```
## 常用命令
- 启动/关闭: mysqld_safe
- 创建数据库: `mysqladmin create databasename;` or `mysql -u root -p databasename < db.sql`
- 导出数据: `mysqldump -uroot -p [--databases dbname] > db.sql`
  - 只导出结构: `mysqldump -uroot -p --no-data [--databases dbname] > db.sql`
  - 压缩版: `mysqldump -uedi_cp -p --databases ep | gzip > ep.sql.gz`
- 导入数据: `mysqlimport -uroot -p < mysql.sql`
- 优化(周期运行): `OPTIMIZE TABLE`
### Tips
- 遇到老的版本跟新的客户端不兼容的错误，可以添加一些flag关闭掉新特性, 比如: `--column-statistics=0`等
## 授权
- 创建用户: `CREATE USER 'username'@'host' IDENTIFIED BY 'password';`
- 授权: 
    `GRANT [privileges] ON dbname.tablename TO 'username'@'host'`
    `GRANT [privileges] ON dbname.tablename TO 'username'@'host' WITH GRANT OPTION;`
    - privileges: 用户的操作权限，如SELECT，INSERT，UPDATE等，如果要授予所的权限则使用ALL. 其中`USAGE` 代表空权限
    - db和tablename: 可以使用*代替,如: db.*, *.* 
- 刷新授权
    `FLUSH PRIVILEGES;`
- 撤销授权: `REVOKE [privileges] ON db.tablename FROM 'username'@'host';`
- 修改密码: 
  - 老版本`SET PASSWORD FOR 'username'@'host' = PASSWORD('newpassword');`
  - 新版本,去掉了PASSWORD字段和函数，使用authentication_string字段
    ```
    ALTER user 'root'@'%' IDENTIFIED BY '123456';
    FLUSH PRIVILEGES;
    select host,user,authentication_string from mysql.user;
    ```
- 删除用户: `DROP USER 'username'@'host';`
- 查看用户的权限: `SHOW GRANTS FOR 'username'@'%';`
> 废弃: GRANT 如果用户不存在，则会根据配置NO_AUTO_CREATE_USER直接创建用户[非常不安全]； 如果GRANT后面跟了IDENTIFIED BY，则会把所有的密码修改，包括登陆密码。
## 绑定端口
netstat -tulpen
bind-address = 0.0.0.0
## 复制数据库
#### 表结构
`CREATE TABLE 新表 SELECT * FROM 旧表 WHERE 1=2;`
#### 表数据
`INSERT INTO 新表 SELECT * FROM 旧表`
#### 表结构和数据
`CREATE TABLE 新表 SELECT * FROM 旧表`

