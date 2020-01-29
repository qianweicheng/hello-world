# Kubectl
https://kubernetes.io/docs/reference/kubectl/overview/
https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands
## Context
- 一个上下文包含四个要素
    - name: context 的名字
    - namespace: 默认default 
    - cluster: 远程k8s集群地址
    - user: 用户
- 配置文件
  - 所在地`~/.kube/config`
  - 通过环境变量配置默认文件(可以多个): KUBECONFIG=~/.kube/config:~/.kube/kubconfig2 
  - 通过`--kubeconfig`指定配置文件,`kubectl config --kubeconfig=~/.kube/config view`
- 查看context: 
  - 只看当前：`kubectl config view --minify`
  - 看所有：`kubectl config view`
- 新建一个context: 
  ```
    kubectl config set-context dev1-ctx 
    --namespace=dev1 
    --cluster=stag.easilydo.cc 
    --user=stag.easilydo.cc
  ```
- 切换context: `kubectl config use-context test-dev2`
- 也可以不需要context，直接链接，使用相应的flag配置参数
  - `--user --cluster --server, --certificate-authority, --insecure-skip-tls-verify`
  - `--client-certificate, --client-key, --username, --password, --token`
- 删除：
  - 用户: `kubectl config unset users.foo `
  - Context: `kubectl config unset contexts.foo`
## COMMAND
kubectl api-versions
kubectl api-resources # 列出所有resources
kubectl cluster-info
kubectl get apiservices
kubectl cp
kubectl explain
kubectl top node
kubectl top pod
### Help man
kubectl explain 
`kubectl explain Deployment.spec.selector`
### Creating
- `kubectl create --image=nginx deployment nginx`
- `kubectl create --image=nginx nginx-app --port=80`
- `kubectl run -it --rm --restart=Never alpine --image=alpine sh`
- `kubectl run -i --tty --restart=Never busybox --image=busybox -- sh`
- Run pod nginx and write its spec into a file called pod.yaml
  `kubectl run nginx --image=nginx --restart=Never --dry-run -o yaml > pod.yaml`
- Run command in existing pod 
    - `kubectl attach my-pod -i` or `kubectl exec my-pod -- ls /`
    - 两者区别在于前者退出时，前者pod停止，后者不会
### Viewing, Finding Resources
#### api-resources
```
kubectl api-resources --namespaced=true      # All namespaced resources
kubectl api-resources --namespaced=false     # All non-namespaced resources
kubectl api-resources -o name                # All resources with simple output (just the resource name)
kubectl api-resources -o wide                # All resources with expanded (aka "wide") output
kubectl api-resources --verbs=list,get       # All resources that support the "list" and "get" request verbs
kubectl api-resources --api-group=extensions # All resources in the "extensions" API group
```
#### Flag
- `-o wide`: With more details
- `-o name`: Name only
- `-o json` or `-o yaml` 输出格式
- `-o jsonpath={xxx}` or `-o go-template={{xx}}` or `-o template={{}}` 输出部分
- `--export`: Get a pod's YAML without cluster specific information
- `--sort-by=.metadata.name`
- `--show-labels`
#### Example
- 选择：
  - `kubectl get node -o wide`
  - `kubectl get pods --field-selector status.phase=Running`
  - `kubectl get pods -lapp=nginx`
  - `kubectl get pvc --all-namespaces（只有get的时候可用）`
  - `kubectl get pvc -l xxx=yyy,mmm=nnn --namespace=xxx`
- 查看资源:
    `kubectl get pod tigase-0 -o=jsonpath="{.spec.containers[0].image}"`
    `kubectl get pod tigase-0 -o=template --template={{.spec.containers.0.image}}`
    `kubectl get pod tigase-0 -o=go-template={{.spec.containers.0.image}}`
#### Update Resources
- Edit
    `kubectl edit svc/docker-registry`
- 修改机器数量
    `kubectl scale statefulset tigase-beta --replicas=3`
    `kubectl scale deployments shadowsocks --replicas=2`
    `kubectl patch statefulset web -p '{"spec":{"replicas":3}}'`
    > Deployment在某个事件点上不保证replicate的准确性，如果需要严格保证的化，使用statefulset
- Rolling update "www" containers of "frontend" deployment, updating the image
    `kubectl set image deployment/frontend www=image:v2`
- Check the history of deployments including the revision 
    `kubectl rollout history deployment/frontend`
- Rollback to the previous deployment
    `kubectl rollout undo deployment/frontend`
- Rollback to a specific revision
    `kubectl rollout undo deployment/frontend --to-revision=2`
- Watch rolling update status of "frontend" deployment until completion
    `kubectl rollout status -w deployment/frontend`
- Add a Label
    `kubectl label pods my-pod new-label=awesome`
- Add an annotation
    `kubectl annotate pods my-pod icon-url=http://goo.gl/XXBTWq`
-  Auto scale a deployment "foo"
    `kubectl autoscale deployment foo --min=2 --max=10`
#### Patching
- Partially update a node
    `kubectl patch node k8s-node-1 -p '{"spec":{"unschedulable":true}}'`
- Update a container's image; spec.containers[*].name is required because it's a merge key
    `kubectl patch pod valid-pod -p '{"spec":{"containers":[{"name":"kubernetes-serve-hostname","image":"new image"}]}}'`
- Update a container's image using a json patch with positional arrays
    `kubectl patch pod valid-pod --type='json' -p='[{"op": "replace", "path": "/spec/containers/0/image", "value":"new image"}]'`
- Disable a deployment livenessProbe using a json patch with positional arrays
    `kubectl patch deployment valid-deployment  --type json   -p='[{"op": "remove", "path": "/spec/template/spec/containers/0/livenessProbe"}]'`
- Add a new element to a positional array
    `kubectl patch sa default --type='json' -p='[{"op": "add", "path": "/secrets/1", "value": {"name": "whatever" } }]'`
#### 删除
- 强制删除
    `kubectl delete pods <pod> --grace-period=0 --force`
- 删除另外的ns中的资源
    `kubectl delete pvc xxx --namespace=xxx`
- Delete a pod using the type and name specified in pod.json
    `kubectl delete -f ./pod.json`
- Delete pods and services with same names "baz" and "foo"
    `kubectl delete pod,service baz foo`
- Delete pods and services with label name=myLabel
    `kubectl delete pods,services -l name=myLabel`
- Delete all pods and services in namespace my-ns
    `kubectl -n my-ns delete po,svc --all`
#### Cheat Sheet
- Deployment
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
- patch大法
    `kubectl patch deployment mongodb-shad-a --type='json' -p='[{"op": "replace", "path": "/spec/template/spec/containers/0/resources/limits/memory", "value":"16Gi"},{"op": "replace", "path": "/spec/template/spec/containers/0/resources/requests/memory", "value":"16Gi"}]'`
    `kubectl patch deployment busybox --patch "$(cat tmp.yaml)"`
    `kubectl patch pod busybox --patch "$(cat pod-busybox.yaml)"`
- 挨个重启的方式
    当只有一个实例的时候，没法自动升级，默认直接时用kubectl apply 不能对statefulset的对象进行升级，必须使用RollingUpdate策略，模式是OnDelete策略, **在statefulset 文件定义的时候添加 RollingUpdate **
    - 通过set环境变量:`kubectl set env statefulset/kafka key=value`
    - 删除环境变量:`kubectl set env statefulset/kafka key-`
    - Patch法
        ```
        kubectl patch statefulset tigase -p '{"spec":{"updateStrategy":{"type":"RollingUpdate"}}}'
        kubectl patch statefulset tigase --type='json' -p='[{"op": "replace", "path": "/spec/template/spec/containers/0/image", "value":"edisonchat/tigase-edison:prod-v1"}]'
        ```
## 添加智能提示
- bash
    ```
        echo "source <(kubectl completion bash)" >> ~/.bashrc 
    ```
- zsh
    ```
    echo "if [ $commands[kubectl] ]; then source <(kubectl completion zsh); fi" >> ~/.zshrc
    ```