#Kubernates Security
##修改kube-apiserver密码（https://kubernetes.io/docs/admin/kube-apiserver/）
登陆到k8s-master机器，修改basic_auth.csv文件。(通过 ps aux | grep kube-apiserver 查看basic-auth-file=/srv/kubernetes/basic_auth.csv)
##