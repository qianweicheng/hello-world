# KOPS
https://github.com/kubernetes/kops
## Create
- 创建后要过一段时间，`203.0.113.123`是一个占位符IP
- 创建可以不需要DNS了，必须`.k8s.local`结尾
```
kops create cluster \
    --node-count 3 \
    --zones us-west-2a,us-west-2b,us-west-2c \
    --master-zones us-west-2a,us-west-2b,us-west-2c \
    --node-size t2.medium \
    --master-size t2.medium \
    --topology private \
    --networking kopeio-vxlan \
    hacluster.example.com
```
## COMMAND
```
export KOPS_STATE_STORE=s3://dev-k8s-easilydo-cc
export NAME=dev.easilydo.cc
```
- 获取集群整体信息: `kops get --name $NAME -o yaml`
- 修改node instance group: `kops edit ig nodes`
- 修改master instance group: `kops edit ig master-ap-northeast-1a`
- 更新集群: `kops update cluster --yes`
- 删除集群: `kops delete cluster`
## 关闭/开启集群
关闭集群跟删除集群不一样，关闭会保存集群信息，方便后面重新开启
- 关闭: 将两组instance group机器修改成0，然后`kops update cluster --yes`
- 开启: 将ig改回来，然后`kops update cluster --yes`
