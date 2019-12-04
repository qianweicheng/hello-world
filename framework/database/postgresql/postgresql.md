# Postgrsql
http://www.postgres.cn/docs/9.6/index.html
## 窗口函数
## 表继承
    CREATE TABLE cities (
      name       text,
      population real,
      altitude   int     -- (in ft)
    );
    
    CREATE TABLE capitals (
      state      char(2)
    ) INHERITS (cities);
## 表定义
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

## 查询
    LIMIT和OFFSET
## 数据类型
::VARCHAR(n) 截取




