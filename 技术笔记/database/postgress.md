http://www.postgres.cn/docs/9.6/index.html
####窗口函数
####表继承
    CREATE TABLE cities (
      name       text,
      population real,
      altitude   int     -- (in ft)
    );
    
    CREATE TABLE capitals (
      state      char(2)
    ) INHERITS (cities);
####表定义
    写成一个列约束的语法是：
    CREATE TABLE products (
        --等价 product_no integer UNIQUE NOT NULL,
        product_no integer PRIMARY KEY,
        name text,
        price numeric CHECK (price > 0)
    );
    给约束起个名字：
    CREATE TABLE products (
        product_no integer,
        name text,
        price numeric CONSTRAINT positive_price CHECK (price > 0)
    );
    写成一个表约束的语法是：
    CREATE TABLE products (
        product_no integer,
        name text,
        price numeric CHECK (price > 0),
        discounted_price numeric CHECK (discounted_price > 0),
        CHECK (price > discounted_price)
    );

####查询
    LIMIT和OFFSET
####数据类型
::VARCHAR(n) 截取
####用户管理
[参考](http://www.postgres.cn/docs/9.6/sql-grant.html)
ROLE,USER
SCHEME相当于namespace
    创建role，并赋予属性
    CREATE ROLE joe LOGIN INHERIT;
    将admin角色添加到joe
    GRANT admin TO joe;

GRANT [ALL PRIVILEGES | SELECT | INSERT | UPDATE | DELETE | TRUNCATE | REFERENCES | TRIGGER] 
ON {[TABLE] table_name | ALL TABLES IN SCHEMA schema_name} 
TO   [ GROUP ] role_name
     | PUBLIC
     | CURRENT_USER
     | SESSION_USER
[ WITH GRANT OPTION ];

```
GRANT SELECT ON ALL TABLES IN SCHEMA public TO PUBLIC;
```
REVOKE xxx ON xxx FROM xxx;




