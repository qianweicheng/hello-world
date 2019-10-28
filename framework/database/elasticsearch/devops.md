# Elasticsearch
## Elastic Search 三要素：
1 _index
2 _type, 同一个_index下面的需要_type相同
3 _id
4 _version(如果添加了version_type=external，则表示使用外部版本号)

## 分析器三步(analyzer,normalizer):
1. 字符过滤器(char filter)
    字符串按顺序通过每个字符过滤器 。他们的任务是在分词前整理字符串。一个字符过滤器可以用来去掉HTML，或者将 & 转化成 and
2. 分词器(tokenizer)
    字符串被 分词器 分为单个的词条。一个简单的分词器遇到空格和标点的时候，可能会将文本拆分成词条。
3. token过滤器(token filters)
    词条按顺序通过每个 token 过滤器 。这个过程可能会改变词条（例如，小写化 Quick ），删除词条（例如， 像 a， and， the 等无用词），或者增加词条（例如，像 jump 和 leap 这种同义词）

## 安装中文分词器：
1. `bin/elasticsearch-plugin install analysis-smartcn` 或者 `ik_max_word`
2. 重启
3. 测试效果
```
GET _analyze?pretty
{
  "analyzer":"smartcn",
  "text":"Elasticsearch是一个非常强大的搜索引擎"
}

POST _analyze
{
  "tokenizer":      "keyword", 
  "char_filter":  [ "html_strip" ],
  "text": "<p>I&apos;m so <b>happy</b>!</p>"
}
```
## 常用API
```
GET _cat/[?help|v]
GET _cluster/health?level=indices/shards
GET _cluster/stats
GET _nodes/stats 比较常用
GET my_index(_all)/_stats
```
## 创建新索引
```
PUT /my-index
{
    "settings": {
        "number_of_shards" :   1,
        "number_of_replicas" : 0
    },
    "mappings": {
        #缺省映射
        "_default_": {
            #动态映射
            "dynamic":true/false/strict限定是否可以添加新的字段，默认true
            "_all": { "enabled":  false }
        },
        "blog": {
            "_all": { "enabled":  true  }
        }
    }
}
PUT /my-index/_settings
{
    "number_of_shards" :   1,
    "number_of_replicas" : 0
}
或者,修改所有
PUT /_all/_settings
{
    "number_of_shards" :   1,
    "number_of_replicas" : 0
}
PUT /_cluster/settings
{
    "persistent" : {
        "discovery.zen.minimum_master_nodes" : 2
    }
    "transient":{
        "discovery.zen.minimum_master_nodes" : 3
    }
}
PUT my_index/_mapping/_doc
{
    "settings":{
        "analysis":{
            "normalizer": {
                "my_normalizer": {
                    "type": "custom",
                    "char_filter": [],
                    "filter": ["lowercase", "asciifolding"]
                }
            }
        }
    }
    "properties": {
        "field1": {
          "type":  "text",
          "analyzer":
          "boost":
          "search_analyzer":
          "search_quote_analyzer":
        }
      }
}
```
## Devops
"reason"=>"blocked by: [FORBIDDEN/12/index read-only / allow delete (api)];"
解决办法：
PUT _all/_settings
{ 
"index.blocks.read_only_allow_delete":null 
}

cluster.name:elasticsearch #集群的名称，同一个集群该值必须设置成相同的

node.name:"es3" #该节点的名字

node.master:true #该节点有机会成为master节点

node.data:true #该节点可以存储数据

node.rack:rack3 #该节点所属的机架

index.number_of_shards:5 #shard的数目

index.number_of_replicas:3 #数据副本的数目

network.bind_host:0.0.0.0 #设置绑定的IP地址，可以是IPV4或者IPV6

network.publish_host:10.0.0.206 #设置其他节点与该节点交互的IP地址

network.host:10.0.0.206 #该参数用于同时设置bind_host和publish_host

transport.tcp.port:9300 #设置节点之间交互的端口号

transport.tcp.compress:true #设置是否压缩tcp上交互传输的数据

http.port:9200 #设置对外服务的http端口号

http.max_content_length:100mb #设置http内容的最大大小

http.enabled:true #是否开启http服务对外提供服务

discovery.zen.minimum_master_nodes:2 #设置这个参数来保证集群中的节点可以知道其它N个有master资格的节点。默认为1，对于大的集群来说，可以设置大一点的值（2-4）

discovery.zen.ping_timeout:120s #设置集群中自动发现其他节点时ping连接的超时时间

discovery.zen.ping.multicast.enabled:true #设置是否打开多播发现节点

discovery.zen.ping.unicast.hosts:["10.0.0.209:9300","10.0.0.206:9300","10.0.0.208:9300"] #设置集群中的Master节点的初始列表，可以通过这些节点来自动发现其他新加入集群的节点