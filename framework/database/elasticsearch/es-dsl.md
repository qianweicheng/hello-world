# Elasticsearch
Refer: https://www.elastic.co/guide/en/elasticsearch/reference/current/
## DSL查询语句：
1. Query Context: 带权重
2. Filter Context: 不带权重
### 基于词：term,terms
基于全文:match系列，query_string等
1. Full-Text query: 
    match_all|
    match|
    match_phrase|
    match_phrase_prefix|
    multi_match:#底层查询使用match|match_phrase等，通过type控制
    common| 会把term分词高频和低频两组进行查询然后合并
    query_string|simple_query_string
2. Term level query: 
    term:#term是代表完全匹配，即不进行分词器分析
    terms,terms_set,
    range,exists,prefix,wildcard,regexp,
    fuzzy:term的模糊版本
    type,ids
3. Compound querys: 
    constant_score（默认1）,
    bool: must|must_not|should|filter
    dis_max:合并个子查询，选择最高分。 通过tie_breaker和boost影响评分
    function_score 自定义函数计算
    boosting 可以减分
### PUT VS POST
1. 更新：PUT会将新的json值完全替换掉旧的；而POST方式只会更新相同字段的值，其他数据不会改变，新提交的字段若不存在则增加。
2. PUT和DELETE操作是幂等的。所谓幂等是指不管进行多少次操作，结果都一样。比如用PUT修改一篇文章，然后在做同样的操作，每次操作后的结果并没有什么不同，DELETE也是一样。
3. POST操作不是幂等的，比如常见的POST重复加载问题：当我们多次发出同样的POST请求后，其结果是创建了若干的资源。
4. 创建操作可以使用POST，也可以使用PUT，区别就在于POST是作用在一个集合资源(/articles)之上的，而PUT操作是作用在一个具体资源之上的(/articles/123)。

## API
- 添加数据: 
    `POST /website/blog/1/_update`
    `PUT /website/blog/123/_create` 后面添加了_create, 那么如果已经存在这个id，则返回409冲突
    POST 可以指定ID，也可以不指定
    `PUT /index/type/1/_create`
    `PUT /index/type/1?op_type=create`
    `GET /xxxx/_mapping/the-type`  获取文档的结构
- 更新数据
    `POST /index/type/1/_update` #局部更新
    `PUT /index/type/1?version=1` #更新整个文档
    外部版本号不仅在索引和删除请求中指定，也可以在创建(create)新文档中指定`&version_type=external`
- Mget vs bulk
```
GET /edi_test/a/_mget
{
 "ids" : [ "2", "1" ]
}
```
## Search API
filter不影响查询权重
- 搜索选项（search_type）
count：只返回个数
query_and_fetch(默认)
scan：顺序读取
- from，size,可以放URL，也可以放body。比如
```
GET /_search
{
    "from" : 0, 
    "size" : 10,
    "query" : {
        "term" : { "user" : "kimchy" }
    }
}
GET /_search
{
    "query": {
        "match" : {
            "message" : "this is a test"
        }
    }
}
GET /_search
{
    "query": {
        "match" : {
           "message" : {
                "query" : "this is a testt",
                "fuzziness": "AUTO",
                "zero_terms_query": "all"
            }
        }
    }
}
GET _search
{
  "from": 0,
  "size": 100,
  "query": {
    "bool": {
        "must": [
            {
            "match": {
                "device_id": "bf11200fab138dbb2fba2d7a8dd92243302b437423fe56408e92d7735d591e5d"
            }
            }
        ],
        "filter": [
            {"term": {"version": "1.0.28"}},
            {"range": {"servertime": {"gte": 0, "lte": 1591782810347}}}
        ]
    }
  }
}
```
- Sort
```
"sort": { "date": { "order": "desc" }},
"sort": [
    { "date":   { "order": "desc" }},
    { "_score": { "order": "desc" }}
]
```
- projection". stored_fields 或者_source
```
"_source": {
        "includes": [ "obj1.*", "obj2.*" ],
        "excludes": [ "*.description" ]
}
```
- Highlight
```
 "highlight" : {
    "fields" : {
        "content" : {}
    }
}
```
- explain:分析性能用
- version": true
- search_after
```
GET /_search
{
    "query":{
       "xxx":{
            "fields":"value"|{
                query: "quick brown dog",#查询内容
                operator:# and|or
                minimum_should_match:"75%"# 也可以使用数字，表示匹配个数
                boost: 2 权重
                slop:  50,单词距离
                zero_terms_query：当所有term被移除的行为,none:返回空,all：返回所有
                cutoff_frequency:将term分成高频低频两组
                low_freq_operator
                auto_generate_synonyms_phrase_query
                fuzziness:1 #模糊度，fuzzy,match,multi_match都支持
            },
        }
    }
}
```
- Delete By Query
_delete_by_query
## DSL查询语句：
1. Query Context: 带权重
2. Filter Context: 不带权重,主要用于结构化搜索
## 基于词：term,terms
基于全文:match系列，query_string等
1. Full-Text query: 
    match_all|
    match|
    match_phrase|
    match_phrase_prefix|
    multi_match:#底层查询使用match|match_phrase等，通过type控制
    common| 会把term分词高频和低频两组进行查询然后合并
    query_string|simple_query_string
2. Term level query: 
    term:#term是代表完全匹配，即不进行分词器分析
    terms,terms_set,
    range,exists,prefix,wildcard,regexp,
    fuzzy:term的模糊版本
    type,ids
3. Compound querys: 
    constant_score（默认1）,
    bool: must|must_not|should|filter
    dis_max:合并个子查询，选择最高分。 通过tie_breaker和boost影响评分
    function_score 自定义函数计算
    boosting 可以减分

## Example
```
GET /_search
{
  "query": {
    "simple_query_string" : {
        "query": "\"fried eggs\" +(eggplant | potato) -frittata",
        "fields": ["title^5", "body"],
        "default_operator": "and"
    }
  }
}
GET log2/_search
{
  "query": {
    "bool" : {
      "filter":[
        {"term":{"version":"1.0.12"}},
        { "range":{"servertime" : {"gte" : 0,"lte" : 1589896072000}}}
      ]
    }
  }
}

POST log2/_delete_by_query
{
  "query": {
    "bool" : {
      "filter":[
        {"term":{"version":"1.0.3"}},
        { "range":{"servertime" : {"gte" : 0,"lte" : 1589896072000}}}
      ]
    }
  }
}

```
