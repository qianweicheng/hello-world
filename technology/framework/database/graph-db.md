# 图形数据库
- Neo4j
- Oracle NoSQL数据库
- OrientDB，
- HypherGraphDB
- GraphBase
- InfiniteGraph
- AllegroGraph
## Neo4j
- Neo4j CQL vs SQL
- 通过使用Apache Lucence支持索引
- 支持UNIQUE约束
- 包含一个UI执行CQL指令：Neo4j的数据浏览器
- 支持完整的ACID（原子性，一致性，隔离性和持久性）规则
- 提供了REST API
## Run
```
docker run \
    --publish=7474:7474 --publish=7687:7687 \
    neo4j
```