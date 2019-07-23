# Kubernates Security
## 修改kube-apiserver密码（https://kubernetes.io/docs/admin/kube-apiserver/）
登陆到k8s-master机器，修改basic_auth.csv文件。(通过 ps aux | grep kube-apiserver 查看basic-auth-file=/srv/kubernetes/basic_auth.csv)
## API Server
    /usr/local/bin/kube-apiserver 
    --allow-privileged=true 
    --anonymous-auth=false 
    --apiserver-count=1 
    --authorization-mode=AlwaysAllow --basic-auth-file=/srv/kubernetes/basic_auth.csv 
    --bind-address=0.0.0.0 
    --client-ca-file=/srv/kubernetes/ca.crt 
## 每个POD下面都有如下文件夹
var/run/secrets/kubernetes.io/serviceaccount/
- ca.crt 根证书
- token: 一个jwt格式的token。其内容是一个secret资源，对应一个ServiceAccount和其绑定的Role
## ServiceAccount, ClusterRole,ClusterRoleBinding
