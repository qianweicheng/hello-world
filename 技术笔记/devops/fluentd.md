# Fluentd
## Install
1. [github](https://github.com/fluent/fluentd-kubernetes-daemonset) 上clone下源代码
2. docker built image
或者直接在 https://hub.docker.com/u/fluent/ 使用镜像
## 配置
- Input
    tag: 后面可以加`*`, 表示实际的文件，`/`替换成`.`。 例如: tag: mytag.*
    parser: 解析每条日记，有json，csv，nginx, apache等等格式
- Output:
    主要注意缓存和非缓存的区别
- Filter:
    用法跟Output一样，都需要一个tag进行匹配
## Devops
v1.0和v0.12差异很大，注意参数
https://docs.fluentd.org/v0.12/articles/
https://docs.fluentd.org/v1.0/articles/
https://github.com/uken/fluent-plugin-elasticsearch
## aws issues
https://discuss.elastic.co/t/elasitcsearch-ruby-raises-cannot-get-new-connection-from-pool-error/36252/10
Flush 频率默认60s
## ElasticSearch
https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html
https://www.elastic.co/guide/en/kibana/current/_pulling_the_image.html

## 扩容升级步骤：
1. 扩大机器
kubectl scale elasticsearch-logging --replicas=5

2. 修改配置防止脑裂
PUT /_cluster/settings
{
    "transient":{
        "discovery.zen.minimum_master_nodes" : 3
    }
}