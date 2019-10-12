# Network
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
## master&node communication 
- node->master: 
  - 通过service account
  - 通过证书走api-server认证流程
- master->node（默认不做证书验证，存在中间人攻击）
  - from the apiserver to the kubelet: 一般用来获取日记，attaching to running pods,port-forwarding等
  - through the apiserver’s proxy functionality.