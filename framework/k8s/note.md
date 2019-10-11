# K8S
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
## master&node communication 
- node->master: 
  - 通过service account
  - 通过证书走api-server认证流程
- master->node（默认不做证书验证，存在中间人攻击）
  - from the apiserver to the kubelet: 一般用来获取日记，attaching to running pods,port-forwarding等
  - through the apiserver’s proxy functionality.
## Discovering Services
- environment variables 
- DNS.
## Public Service
https://kubernetes.io/docs/concepts/services-networking/service/
https://kubernetes.io/docs/concepts/cluster-administration/cloud-providers/
- ClusterIP
- NodePort
- LoadBalancer
  - Internal load balancer: `service.beta.kubernetes.io/aws-load-balancer-internal: "true"`
  - TLS support on AWS: 
    - `service.beta.kubernetes.io/aws-load-balancer-ssl-cert: arn:aws:xxx`
    - `service.beta.kubernetes.io/aws-load-balancer-backend-protocol: (https|http|ssl|tcp)`
    - `service.beta.kubernetes.io/aws-load-balancer-proxy-protocol: "*"`
    - `service.beta.kubernetes.io/aws-load-balancer-ssl-ports: "443,8443"`
    - `service.beta.kubernetes.io/aws-load-balancer-ssl-negotiation-policy: "ELBSecurityPolicy-TLS-1-2-2017-01"`
- ExternalName
## Kubernetes networking model
- ACI
- AOS from Apstra
- AWS VPC CNI for Kubernetes
- Big Cloud Fabric from Big Switch Networks
- Cilium
- CNI-Genie from Huawei
- cni-ipvlan-vpc-k8s
- Contiv
- Contrail / Tungsten Fabric
- DANM
- Flannel
## 扩展Kubernates API
允许在不修改源代码的前提下扩展。方式有两个
- API Aggregation
  - 通过apiserver-builder创建
  - sample-apiserver和apiserver-builder/example
- CRD