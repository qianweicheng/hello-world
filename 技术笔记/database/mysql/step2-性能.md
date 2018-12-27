# 性能
## 索引
- HASH索引
    - 全值匹配（只有Memory引擎支持）
- B-Tree索引  
    B-Tree索引适合如下场景：
    - 全值匹配
    - 匹配最左边前缀
    - 匹配列前缀
    - 匹配范围值
    - 精确匹配某一列并范围匹配另外一列
    - 只访问索引的查询(覆盖索引)
- R-Tree(空间索引)
- 全文索引
- 其他
    - Fractal tree index
## 高性能索引策略
- 独立的列
    避免在查询的条件字段上做运算
- 前缀索引和索引的选择。
    CREATE INDEX xxx ON yyy (LEFT(8));
    通过如下方式分析合适的前缀长度
    ```
        SELECT COUNT(DISTINCT LEFT(city,3))/COUNT(*) AS sel3,
        COUNT(DISTINCT LEFT(city,4))/COUNT(*) AS sel4,
        COUNT(DISTINCT LEFT(city,5))/COUNT(*) AS sel5,
        COUNT(DISTINCT LEFT(city,6))/COUNT(*) AS sel6,
        COUNT(DISTINCT LEFT(city,7))/COUNT(*) AS sel7,
    ```
    缺点：无法做`order by`和`group by`
    >案例: 查找某个域名下的所有邮件,(MySQL不支持后缀索引)，可以把字符串反过来存储
- 多列索引
    列顺序非常重要
- 聚簇索引
    并不是一种单独的索引，而是一种数据存储的方式
    优点：
    - 可以把相关数据存放在一起，减少I/O次数
    - 索引和数据放在同一个B-Tree，查找更快
    - 使用覆盖索引查找的时候可以直接使用叶节点的主键值
    缺点：
    - 插入顺序严重影响插入速度，插入新记录时，如果插入的页已慢，则需要页分裂。一般使用自增主键避免(但上界会产生热点)。
    - 更新索引代价很高，需要移动数据。 一般不更新聚簇索引。
    - 主键稀疏导致表扫描慢
- 覆盖索引
- 冗余
    - 重复索引：在相同的列上以相同的顺序创建相同类型的索引，绝对避免
    - 索引(A,B)和(A)算冗余索引，看情况避免。比如`userinfo`表有大量如下查询:
        `SELECT COUNT(*) FROM userinfo WHERE state_id=?`
        `SELECT state_id,city FROM userinfo WHERE state_id=?`
        就可以用两个索引优化查询：
        - (state_id)
        - (state_id,city) 主要让其能覆盖查询
- 尽量避免NULL
    尽管对性能的提升有限，但可为NULL的设计会导致应用更容易出BUG，占用更多的存储空间(虽然微乎其微)
## 高性能查询策略
- 支持多种过滤条件
    - 对于选择性不高，但在搜索条件中非常频繁使用的列，添加进入索引，并放入前列。 原因：
        - 在查询的时候就可以通过前缀索引进行查询
        - 即使偶尔不需要通过该列搜索，也可以通过添加`AND field_1 IN (all-set)`这个小技巧优化。前提是`all-set`集合不大
        - 把范围搜索字段放索引最后
- 避免多个范围条件
- 优化排序: 可以考虑对
- 查询不必要的数据(SELECT *)
    - 节省服务器内存/CPU和带宽
    - (重点)利用覆盖索引
- 优化LIMIT分页，主要是精确id范围，然后加载其他数据，节省I/O
    `SELECT * FROM t1 INNER JOIN (SELECT id FROM t1 ORDER BY TITLE LIMIT 50,5) AS t2;`
- 一个复杂查询 VS 多个简单查询
    - 复杂度留给应用层
- 切分查询
    对于一个非常巨大的查询，需要切分成多个查询。常见于数据ETL
- 分解查询
    将关联查询分解到用层处理，不使用存储过程是一个道理, 尽量减少数据库的压力。好处：
    - 利用数据库缓存
    - 减少单个查询的锁竞争
    - 应用层的拓展性好于数据库，
    - 部分情况可以在用层使用Hash关联，而不是在数据库中使用嵌套循环关联
## 性能分析
#### EXPLAIN  
字段|注释
:-:|-
id|SELECT的查询序列号
select_type|SIMPLE：简单SELECT(不使用UNION或子查询等)<br>PRIMARY：最外面的SELECT<br>UNION：UNION中的第二个或后面的SELECT语句.<br> DEPENDENT UNION：UNION中的第二个或后面的SELECT语句，取决于外面的查询<br>UNION RESULT：UNION的结果。<br>SUBQUERY：子查询中的第一个SELECT<br>DEPENDENT SUBQUERY：子查询中的第一个SELECT，取决于外面的查询<br>DERIVED：导出表的SELECT(FROM子句的子查询)
table|显示这一行的数据是关于哪张表的
type(重要)|显示了连接使用了哪种类别,有无使用索引<br>system > const(主键跟常量比) > eq_ref(primary key 或 unique key 索引的所有部分被连接使用 ，最多只会返回一条符合条件的记录) > ref(同前，不使用唯一索引，而是使用普通索引或者唯一性索引的部分前缀) > fulltext > ref_or_null(同ref，允许null) > index_merge(or条件，union等) > unique_subquery(in查询) > index_subquery(同前，子查询查的不是主键而是非唯一索引) > range(between) > index(在index上全表扫描) > ALL(全表扫描)<br>一般来说，得保证查询至少达到range级别，最好能达到ref，否则就可能会出现性能问题。<br>当type 显示为 “index” 时，并且Extra显示为“Using Index”， 表明使用了覆盖索引。
possible_keys|列指出MySQL可能使用哪个索引在该表中找到行。可能出现 possible_keys 有列，而 key 显示 NULL 的情况，这种情况是因为表中数据不多，mysql认为索引对此查询帮助不大，选择了全表查询。
key|显示MySQL实际决定使用的键（索引）。如果没有选择索引，键是NULL
key_len|显示MySQL决定使用的键长度。如果键是NULL，则长度为NULL。使用的索引的长度。在不损失精确性的情况下，长度越短越好。<br>字符串类型按照本身的长度来，但最大长度是768字节，当字符串过长时，mysql会做一个类似左前缀索引的处理，将前半部分的字符提取出来做索引<br>INT:4 bytes数值类型和日期类型都是按照本身的长度来
ref|显示使用哪个列或常数与key一起从表中选择行
rows|显示MySQL认为它执行查询时必须检查的行数。
Extra(重要)|包含MySQL解决查询的详细信息，也是关键参考项之一<br>Distinct,一旦MYSQL找到了与行相联合匹配的行，就不再搜索了<br>Not exists一旦它找到了匹配LEFT JOIN标准的行，就不再搜索了<br>Range checked for each<br>Record（index map:#）没有找到理想的索引，因此对于从前面表中来的每一 个行组合，MYSQL检查使用哪个索引，并用它来从表中返回行。这是使用索引的最慢的连接之一<br>Using filesort:看到这个的时候，查询就需要优化了。MYSQL需要进行额外的步骤来发现如何对返回的行排序。它根据连接类型以及存储排序键值和匹配条件的全部行的行指针来 排序全部行<br>Using index: 列数据是从仅仅使用了索引中的信息而没有读取实际的行动的表返回的，这发生在对表的全部的请求列都是同一个索引的部分的时候<br>Using temporary:看到这个的时候，查询需要优化了。这里，MYSQL需要创建一个临时表来存储结果，这通常发生在对不同的列集进行ORDER BY上，而不是GROUP BY上<br>Using where:使用了WHERE从句来限制哪些行将与下一张表匹配或者是返回给用户。如果不想返回表中的全部行，并且连接类型ALL或index， 这就会发生，或者是查询有问题
partions|TODO

#### 剖析SQL查询
- 打开性能分析器：SET PROFILING=1;
- SHOW PROFILES:查看历史SQL性能: 
    最近一条: SHOW PROFILE;
    具体某条: SHOW PROFILE FOR QUERY XXX;
- SHOW STATUS
    搜索: `SHOW STATUS WHERE Variable_name LIKE 'xxx%';`
- SHOW GLOBAL STATUS;

- SHOW PROCESSLIST\G;