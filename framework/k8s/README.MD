# K8S知识图
## 架构图
![PIC1](./images/architecture.png)
![PIC2](./images/master.png)
![PIC3](./images/node.png)
![PIC4](./images/layer.jpg)
#### Kubernetes主要由以下几个核心组件组成：
- etcd
  - 保存了整个集群的状态；
  - Etcd是CoreOS基于Raft开发的分布式key-value存储
  - 监听机制
  - 原子CAS和CAD，用于分布式锁和leader选举
  - key的过期及续约机制，用于监控和服务发现
  - Etcd Zookeeper and Consul
- apiserver
  - 提供了资源操作的唯一入口，并提供认证、授权、访问控制、API注册和发现等机制
  - `/swaggerapi`查看Swagger API, `/swagger.json`查看OpenAPI
  - 开启`--enable-swagger-ui=true`后还可以通过`/swagger-ui`访问Swagger UI。
  - 访问：kubectl or SDK(支持多种语言)
  - 扩展API:`kubectl get apiservice`
- controller manager
  - 负责维护集群的状态，比如故障检测、自动扩展、滚动更新等
  - Controller Manager由kube-controller-manager和cloudcontroller-manager组成，是Kubernetes的大脑。
    - kube-controller-manager由一些列Controller组成
      - Replication Controller
      - Node Controller
      - CronJob Controller
      - Daemon Controller
      - Deployment Controller
      - Endpoint Controller
      - Garbage Collector
      - Namespace Controller
      - Job Controller
      - Pod AutoScaler
      - RelicaSet
      - Service Controller
      - ServiceAccount Controller
      - StatefulSet Controller
      - Volume Controller
      - Resource quota Controller
    - cluod-controller-manager 在启动Cloud Provider的时候才需要
      - Node Controller
      - Route Controller
      - Service Controller
  - 由一系列的控制器组成
    - Replication Controller
    - Node Controller
    - CronJob Controller
    - Daemon Controller
    - ...
- scheduler负责资源的调度，按照预定的调度策略将Pod调度到相应的机器上
  - kube-scheduler负责分配调度Pod到集群内的节点上，它监听kubeapiserver，查询还未分配Node Pod，然后根据调度策略为这些Pod分配节点（更新Pod的 NodeName 字段）。
  - 调度因素：
    - 公平调度
    - 资源高效利用
    - QoS
    - affinity 和 anti-affinity
    - 数据本地化（data locality）
    - 内部负载干扰（inter-workload interference）
    - deadlines
- kubelet(node)负责维持容器的生命周期，同时也负责Volume（CVI）和网络（CNI）的管理
  - 每个节点上都运行一个kubelet服务进程，默认监听10250端口
  - 在集群内部可以直接访问 kubelet 的 10255 端口，`http://<node-name>:10255/stats/summary`
  - cAdvisor 4194
  - healthz 10248
- Container runtime(node)负责镜像管理以及Pod和容器的真正运行（CRI）
  - Docker
  - containerd
  - cri-o
  - rktlet 
- kube-proxy(node)负责为Service提供cluster内部的服务发现和负载均衡
  - kube-proxy可以直接运行在物理机上，也可以以static pod或者daemonset的方式运行。
  - 监听API server中service和endpoint的变化情况，并通过iptables等来为服务配置负载均衡（仅支持TCP和UDP）。
  - 可以直接运行在物理机上，也可以以static pod或者daemonset的方式运行
#### 除了核心组件，还有一些推荐的Add-ons：
- kube-dns负责为整个集群提供DNS服务
  - 查询请求首先会被发送到kube-dns的DNS缓存层(Dnsmasq 服务器)。Dnsmasq服务器会先检查请求的后缀，带有集群后缀（例如：”.cluster.local”）的请求会被发往kube-dns，拥有存根域后缀的名称（例如：”.acme.local”）将会被发送到配置的私有DNS服务器[“1.2.3.4”]。最后，不满足任何这些后缀的请求将会被发送到上游DNS [“8.8.8.8”,“8.8.4.4”]里
- Ingress Controller为服务提供外网入口
- Heapster提供资源监控
- Dashboard提供GUI
- Federation提供跨可用区的集群
- Fluentd-elasticsearch提供集群日志采集、存储与查询
## 集群搭建
- 单机部署：minikube
- 集群部署
  - kubeadm
  - kops(生产级)
  - ...
- Kubernetes-The-Hard-Way
#### 选择
- 在aws上建议使用kops来部署。
- 在Linux物理机或虚拟机中，建议使用kubeadm或kubespray来部署Kubernetes集群。
## API介绍
/api/v1/proxy/namespaces/kube-system/services/monitoring-grafana
## Label与Annotation
## Namespaces
## Pod及其相关资源
## Services
## 健康检测
## 数据存储
## 调度
## 日常维护
## 网络方案介绍
## 应用自动弹性伸缩
## 负载均衡
## 安全
## 包管理
## 部署
## 监控告警
## 镜像管理
## 日记收集与分析
