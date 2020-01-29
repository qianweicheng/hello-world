# Install
## New install
注意版本，如果客户端版本比服务器版本低，则容易出`Error from server (NotFound): the server could not find the requested resource`错误
- 安装kubectl,kops,awscli
  - 参考: https://github.com/kubernetes/kops/blob/master/docs/install.md
- Create S3
  - 这里有点坑
  ```
    aws s3api create-bucket \
    --bucket dev-k8s-easilydo-cc \
    --region ap-northeast-1 \
    --create-bucket-configuration LocationConstraint=ap-northeast-1
    aws s3api put-bucket-versioning \
    --bucket dev-k8s-easilydo-cc \
    --versioning-configuration Status=Enabled
    ```
- Config the Domain
    - 创建一个子域名，dev.easilydo.cc
    - 将子域名的NS拷贝到父域名中
- Create The cluster
  ```
    # 列出一个region下所有的zones
    aws ec2 describe-availability-zones --region ap-northeast-1
    # a DNS baseed cluster MUST config the domain
    export NAME=dev.easilydo.cc
    # a gossip-based cluster can be easily created.
    export NAME=mytest1.k8s.local
    export KOPS_STATE_STORE=s3://dev-k8s-easilydo-cc
    kops create cluster \
    --zones ap-northeast-1a \
    $NAME
  ```
## 升级
- 一行搞定(直接升级到最新的release版本): `kops upgrade cluster`
- The Hard way:
    1. [升级kops](https://github.com/kubernetes/kops)
    2. [升级集群](https://github.com/kubernetes/kops/blob/master/docs/upgrade.md)：
    3. [查看Version](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md)
    4. `kops edit cluster` 在create-cluster.md里面查看
    5. `kops upgrade cluster $NAME`
>此处有坑：VPC的名字不能修改，否则会导致kops找不到，重新创建
## Delete cluster
`kops delete cluster $NAME`