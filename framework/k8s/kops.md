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
## View 
`kops get --name $NAME -o yaml`