# Devops
## Master node配置
参考: https://kubernetes.io/docs/setup/best-practices/cluster-large/
1-5 nodes: m3.medium
6-10 nodes: m3.large
11-100 nodes: m3.xlarge
101-250 nodes: m3.2xlarge
251-500 nodes: c4.4xlarge
more than 500 nodes: c4.8xlarge
## 扩容时候注意如下服务
InfluxDB and Grafana
kubedns, dnsmasq, and sidecar
Kibana
elasticsearch
FluentD with ElasticSearch Plugin
FluentD with GCP Plugin
## Labels & Selectors
```
"metadata": {
  "labels": {
    "key1" : "value1",
    "key2" : "value2"
  },
  "annotations": {
    "key1" : "value1",
    "key2" : "value2"
  }
}
```
- Labels: 主要用来选择pod，service等. labels有一套推荐规范
```
apiVersion: apps/v1
kind: StatefulSet
metadata:
  labels:
    app.kubernetes.io/name: mysql
    app.kubernetes.io/instance: wordpress-abcxzy
    app.kubernetes.io/version: "5.7.21"
    app.kubernetes.io/component: database
    app.kubernetes.io/part-of: wordpress
    app.kubernetes.io/managed-by: helm
```
- Annotations: 纯粹用来做注释的
## Node
node添加
--node-eviction-rate=0.1 pod/s

## 扩展Kubernates API
允许在不修改源代码的前提下扩展。方式有两个
- API Aggregation
  - 通过apiserver-builder创建
  - sample-apiserver和apiserver-builder/example
- CRD