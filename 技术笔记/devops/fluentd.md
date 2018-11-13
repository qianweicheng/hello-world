##Fluentd
####Install
1. [github](https://github.com/fluent/fluentd-kubernetes-daemonset) 上clone下源代码
2. docker built image
或者直接在 https://hub.docker.com/u/fluent/ 使用镜像
####Devops
v1.0和v0.12差异很大，注意参数
https://docs.fluentd.org/v0.12/articles/
https://docs.fluentd.org/v1.0/articles/
https://github.com/uken/fluent-plugin-elasticsearch
#aws issues
https://discuss.elastic.co/t/elasitcsearch-ruby-raises-cannot-get-new-connection-from-pool-error/36252/10
Flush 频率默认60s
####ElasticSearch
https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html
https://www.elastic.co/guide/en/kibana/current/_pulling_the_image.html

扩容升级步骤：
1. 扩大机器
kubectl scale elasticsearch-logging --replicas=5

2. 修改配置防止脑裂
PUT /_cluster/settings
{
    "transient":{
        "discovery.zen.minimum_master_nodes" : 3
    }
}