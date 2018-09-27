##Mongodb使用注意事项
- 唯一索引必须建在分片键上(如果有), 不能建立在hash索引上
    可以对已有的表建，但必须是无冲突
- db.collection.count() 不准确
- 分片键建立之后不能修改
- upset 查询必须用在unique index上，否则可能重复
- Create an Index on Embedded Document
    在内嵌的文档整体上建索引的话，查询的时候必须严格字节匹配
- Hash 索引在float的字段上会做截断处理，[参考](https://docs.mongodb.com/manual/core/index-hashed/)