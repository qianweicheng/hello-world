# Postgresql
## Install
TODO
## 用户管理
### Concept
[参考](http://www.postgres.cn/docs/9.6/sql-grant.html)
- ROLE,USER: 两者之间可以相互转换，区别在于是否可登录
- SCHEME相当于namespace
### 授权
- 创建role，并赋予角色
    ```
    CREATE ROLE joe LOGIN INHERIT;
    将admin角色添加到joe
    GRANT admin TO joe;
    ```
- 授权
    ```
    GRANT [ALL PRIVILEGES | SELECT | INSERT | UPDATE | DELETE | TRUNCATE | REFERENCES | TRIGGER] 
    ON {[TABLE] table_name | ALL TABLES IN SCHEMA schema_name} 
    TO   [ GROUP ] role_name
        | PUBLIC
        | CURRENT_USER
        | SESSION_USER
    [ WITH GRANT OPTION ];
    GRANT SELECT ON ALL TABLES IN SCHEMA public TO PUBLIC;
    GRANT SELECT,INSERT,UPDATE,DELETE ON ALL TABLES IN SCHEMA public TO edi_dba;
    ```
- 撤销授权
    `REVOKE xxx ON xxx FROM xxx;`
### 授权管理
在scheme的管理页面可以统一管理