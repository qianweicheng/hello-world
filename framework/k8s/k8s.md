## Kubernates 升级
1. [升级kops](https://github.com/kubernetes/kops)
2. [升级集群](https://github.com/kubernetes/kops/blob/master/docs/upgrade.md)：
3. [查看Version](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md)
4. kops edit cluster $NAME #NAME 在create-cluster.md里面查看
5. kops upgrade cluster $NAME
6. kops update cluster $NAME --yes
>此处有坑：VPC的名字不能修改，否则会导致kops找不到，重新创建

## k8s滚动升级
当只有一个实例的时候，没法自动升级，默认直接时用kubectl apply 不能对statefulset的对象进行升级，必须使用RollingUpdate策略，模式是OnDelete策略
***在statefulset 文件定义的时候添加 RollingUpdate ***
或者：kubectl patch statefulset tigase -p '{"spec":{"updateStrategy":{"type":"RollingUpdate"}}}'
kubectl patch statefulset tigase --type='json' -p='[{"op": "replace", "path": "/spec/template/spec/containers/0/image", "value":"edisonchat/tigase-edison:prod-v1"}]'

## 变量引用
```
- name: MY_POD_SERVICE_ACCOUNT
  valueFrom:
    fieldRef:
      fieldPath: spec.serviceAccountName
- name: MY_POD_NAME
  valueFrom:
    fieldRef:
        fieldPath: metadata.name
```
## Service 
#### 分成三类
1. ClusterIP
2. NodePort (default: 30000-32767)
3. LoadBalancer
4. Headless service:port 无需定义，不走service的port, pod 上的port在非NodePort情况下无需定义
#### Service 的三种格式:
- xxxx
- xxxx.<namespace>
- xxxx.<namespace>.svc.cluster.local
####  普通service vs headless service(type:ClusterIP + clusterIP:None) 
1. There is a long history of DNS libraries not respecting DNS TTLs and caching the results of name lookups.
2. Many apps do DNS lookups once and cache the results.
3. Even if apps and libraries did proper re-resolution, the load of every client re-resolving DNS over and over would be difficult to manage.

## 常用命令
- 查看资源:
    `kubectl get pod tigase-0 -o=jsonpath="{.spec.containers[0].image}"`
    `kubectl get pod tigase-0 -o=template --template={{.spec.containers.0.image}}`
    `kubectl get pod tigase-0 -o=go-template={{.spec.containers.0.image}}`
- 修改机器数量
    `kubectl scale statefulset tigase-beta --replicas=3`
    `kubectl scale deployments shadowsocks --replicas=2`
    > Deployment在某个事件点上不保证replicate的准确性，如果需要严格保证的化，使用statefulset
- 强制删除
    `kubectl delete pods <pod> --grace-period=0 --force`
    `kubectl get pvc --all-namespaces（只有get的时候可用）`
    `kubectl get pvc -l xxx=yyy --namespace=xxx`
    `kubectl delete pvc xxx --namespace=xxx`
- 简单创建：
    `kubectl create deployment nginx --image=nginx`
- 查看版本历史
    `kubectl rollout history deployment/nginx-deployment`
    `kubectl rollout history deployment/nginx-deployment --revision=2`
- 回滚到上一个版本: 
    `kubectl rollout undo deployment/nginx-deploymen`
- 回滚到指定一个版本: 
    `kubectl rollout undo deployment/nginx-deployment --to-revision=2`
- Pause: 
    `kubectl rollout pause deployment/nginx-deploymen`
- Resume: 
    `kubectl rollout resume deploy/nginx-deployment`
- Update:
    `kubectl set image deploy/nginx-deployment nginx=nginx:1.9.1`
    `kubectl set resources deployment nginx-deployment -c=nginx --limits=cpu=200m,memory=512Mi`
    `kubectl set image deployment/nginx busybox=busybox nginx=nginx:1.9.1`
- 替换image和command: `kubectl patch deployment mongodb-conf --type='json' -p='[{"op": "replace", "path": "/spec/template/spec/containers/0/image", "value":"edisonchat/mongodb"}, {"op": "remove", "path": "/spec/template/spec/containers/0/command"}, {"op": "add", "path": "/spec/template/spec/containers/0/args", "value":["--configsvr", "--replSet", "configReplSet"]}]'`
- 修改volume大小
    `aws ec2 modify-volume --volume-id vol-070a7796c8543f11d --size 44` 
- 修改资源
    `kubectl patch deployment mongodb-shad-a --type='json' -p='[{"op": "replace", "path": "/spec/template/spec/containers/0/resources/limits/memory", "value":"16Gi"},{"op": "replace", "path": "/spec/template/spec/containers/0/resources/requests/memory", "value":"16Gi"}]'`
    `kubectl patch deployment busybox --patch "$(cat tmp.yaml)"`
    `kubectl patch pod busybox --patch "$(cat pod-busybox.yaml)"`
- 挨个重启的方式
    - 通过set环境变量:`kubectl set env statefulset/kafka key=value`
    - 删除环境变量:`kubectl set env statefulset/kafka key-`
- Context：一个上下文包含四个要素
    - name: context 的名字
    - namespace: 默认default 
    - cluster: 远程k8s集群地址
    - user: 用户
    比如新建一个context: `kubectl config set-context dev1-ctx --namespace=dev1 --cluster=stag.easilydo.cc --user=stag.easilydo.cc`
## 在pod中查看api server 信息
-  `curl -v --cacert /var/run/secrets/kubernetes.io/serviceaccount/ca.crt -H "Authorization: Bearer $(cat /var/run/secrets/kubernetes.io/serviceaccount/token)"`
- `https://kubernetes/`
- `https://$KUBERNETES_SERVICE_HOST:$KUBERNETES_SERVICE_PORT`

## Filesystem
- `aws ec2 modify-volume --region us-east-1 --volume-id vol-11111111111111111 --size 20 --volume-type gp2`
- `aws ec2 describe-volumes-modifications --region us-east-1 --volume-id vol-11111111111111111`
- `kubectl get node -o wide`