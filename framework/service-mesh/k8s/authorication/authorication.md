# K8S 认证与授权
参考: https://github.com/kubernetes/dashboard/blob/master/docs/user/access-control/creating-sample-user.md
## 认证
- serviceaccount
- clusterrole & role
  - clusterrole可以跨namespace
  - role不能跨namespace
- rolebinding & clusterrolebinding
### 内置ClusterRole
- cluster-admin
- cluster-status
- admin
- edit 
- view
### 查询密码
- 查询token: `kubectl get secret xxx -o yaml`
- secrets存放在`/var/run/secrets/kubernetes.io/serviceaccount/`
- 证书
  ```
  CA_CRT_PATH=/etc/kubernetes/ssl/ca.pem
  CA_KEY_PATH=/etc/kubernetes/ssl/ca-key.pem
  ```
### 认证有几种方式
- 证书
- Static Token File
  - 启动参数: `--token-auth-file=SOMEFILE`
  - 请求头: `Authorization: Bearer XXXX`
  - 使用方式: 
    - `kubectl --token=the-token xxx`
    - `curl -H "Authorization: Bearer XXXX" https://xxx/api/v1 --insecure`
- Bootstrap Tokens
  - 启动参数: `--enable-bootstrap-token-auth`
  - 请求头: `Authorization: Bearer xxxxxx.xxxxxxxxxxxxxxxx`, 格式: [a-z0-9]{6}\.[a-z0-9]{16}
- Static Password File
  - 启动参数: `--basic-auth-file=SOMEFILE`
  - 请求头: `Authorization: Basic BASE64ENCODED(USER:PASSWORD)`
- Service Account Tokens
  - 默认开启，可选参数: `--service-account-key-file` and `--service-account-lookup`
### Kubernates Security
- 修改kube-apiserver密码（https://kubernetes.io/docs/admin/kube-apiserver/）
登陆到k8s-master机器，修改basic_auth.csv文件。(通过 ps aux | grep kube-apiserver 查看basic-auth-file=/srv/kubernetes/basic_auth.csv),修改了必须重启才生效
- API Server
  ```
    /usr/local/bin/kube-apiserver 
    --allow-privileged=true 
    --anonymous-auth=false 
    --apiserver-count=1 
    --authorization-mode=AlwaysAllow 
    --basic-auth-file=/srv/kubernetes/basic_auth.csv 
    --bind-address=0.0.0.0 
    --client-ca-file=/srv/kubernetes/ca.crt
  ```
- Node
  ```
  /usr/local/bin/kubelet 
  --cgroup-root=/ 
  --cloud-provider=aws 
  --cluster-dns=100.64.0.10 
  --cluster-domain=cluster.local 
  --enable-debugging-handlers=true 
  --eviction-hard=memory.available<100Mi,nodefs.available<10%,nodefs.inodesFree<5%,imagefs.available<10%,imagefs.inodesFree<5% --feature-gates=ExperimentalCriticalPodAnnotation=true --hostname-override=ip-172-20-42-115.us-west-2.compute.internal 
  --kubeconfig=/var/lib/kubelet/kubeconfig 
  --network-plugin-mtu=9001 
  --network-plugin=kubenet 
  --node-labels=kubernetes.io/role=node,node-role.kubernetes.io/node= 
  --non-masquerade-cidr=100.64.0.0/10 
  --pod-infra-container-image=k8s.gcr.io/pause-amd64:3.0 
  --pod-manifest-path=/etc/kubernetes/manifests 
  --register-schedulable=true 
  --v=2 
  --cni-bin-dir=/opt/cni/bin/ 
  --cni-conf-dir=/etc/cni/net.d/ 
  --cni-bin-dir=/opt/cni/bin/
  ```
- kube-proxy
  ```
    /usr/local/bin/kube-proxy 
    --cluster-cidr=100.96.0.0/11 
    --conntrack-max-per-core=131072 --hostname-override=ip-172-20-42-115.us-west-2.compute.internal 
    --kubeconfig=/var/lib/kube-proxy/kubeconfig 
    --master=https://api.internal.stag.easilydo.cc 
    --oom-score-adj=-998 
    --resource-container= 
    --v=2
  ```
- 每个POD下面都有如下文件夹
var/run/secrets/kubernetes.io/serviceaccount/
- ca.crt 根证书
- token: 一个jwt格式的token。其内容是一个secret资源，对应一个ServiceAccount和其绑定的Role
- ServiceAccount, ClusterRole,ClusterRoleBinding
### WebHooks
Webhook Token Authentication: Webhook authentication is a hook for verifying bearer tokens.
```
{
  "apiVersion": "authentication.k8s.io/v1beta1",
  "kind": "TokenReview",
  "status": {
    "authenticated": true,
    "user": {
      "username": "janedoe@example.com",
      "uid": "42",
      "groups": [
        "developers",
        "qa"
      ],
      "extra": {
        "extrafield1": [
          "extravalue1",
          "extravalue2"
        ]
      }
    }
  }
}
```
### Dashboard Authorication
首先必须使用Basic Auth进入（这是由于Dashboard web的原因，自己开发可以直接使用Token），然后:
- 可以直接跳过，这个时候就是使用默认账号登录
- 也可以使用Token登录
- 使用ServiceAccount
  - https://itnext.io/let-you-team-members-use-kubernetes-bf2ebd0be717
### Check
`kubectl auth can-i create deployments --namespace prod`
`kubectl auth can-i list secrets --namespace dev --as user1`
## 授权
### Authorization Modes
- Node
- ABAC
  `{"apiVersion": "abac.authorization.kubernetes.io/v1beta1", "kind": "Policy", "spec": {"user": "kubelet", "namespace": "*", "resource": "pods", "readonly": true}}`
- RBAC
  ```
  kubectl config set-cluster test-dev2 \
    --embed-certs=true \
    --server=https://api.stag.easilydo.cc \
    --certificate-authority=./ca.crt
  user_token={this-the-token}
  kubectl config set-credentials test-dev2 --token=$user_token
  kubectl config set-context test-dev2 \
    --cluster=test-dev2 \
    --user=test-dev2 \
    --namespace=dev
  kubectl config use-context test-dev2
  ```
- Webhook
## API Server 启动
```
/usr/local/bin/kube-apiserver 
--allow-privileged=true 
--anonymous-auth=false 
--apiserver-count=1 
--authorization-mode=AlwaysAllow
--basic-auth-file=/srv/kubernetes/basic_auth.csv 
--bind-address=0.0.0.0 
--client-ca-file=/srv/kubernetes/ca.crt 
--cloud-provider=aws 
--enable-admission-plugins=NamespaceLifecycle,LimitRanger,ServiceAccount,PersistentVolumeLabel,DefaultStorageClass,DefaultTolerationSeconds,MutatingAdmissionWebhook,ValidatingAdmissionWebhook,NodeRestriction,ResourceQuota 
--etcd-cafile=/etc/kubernetes/pki/kube-apiserver/etcd-ca.crt 
--etcd-certfile=/etc/kubernetes/pki/kube-apiserver/etcd-client.crt 
--etcd-keyfile=/etc/kubernetes/pki/kube-apiserver/etcd-client.key --etcd-servers-overrides=/events#https://127.0.0.1:4002 
--etcd-servers=https://127.0.0.1:4001 
--insecure-bind-address=127.0.0.1 
--insecure-port=8080 
--kubelet-preferred-address-types=InternalIP,Hostname,ExternalIP --proxy-client-cert-file=/srv/kubernetes/apiserver-aggregator.cert --proxy-client-key-file=/srv/kubernetes/apiserver-aggregator.key --requestheader-allowed-names=aggregator 
--requestheader-client-ca-file=/srv/kubernetes/apiserver-aggregator-ca.cert --requestheader-extra-headers-prefix=X-Remote-Extra- --requestheader-group-headers=X-Remote-Group --requestheader-username-headers=X-Remote-User 
--secure-port=443 
--service-cluster-ip-range=100.64.0.0/13 
--storage-backend=etcd3 
--tls-cert-file=/srv/kubernetes/server.cert 
--tls-private-key-file=/srv/kubernetes/server.key 
--token-auth-file=/srv/kubernetes/known_tokens.csv 
--v=2
```