# Info
测试最好使用`kubectl proxy`
## API groups & versioning
/apis/$GROUP_NAME/$VERSION 返回都是APIResourceList
- Groups
  - /api/v1: 返回所有资源
  - admissionregistration.k8s.io
  - apiextensions.k8s.io
  - apiregistration.k8s.io
  - apps
  - authentication.k8s.io
  - authorization.k8s.io
  - autoscaling
  - batch
  - certificates.k8s.io
  - coordination.k8s.io
  - discovery.k8s.io
  - events.k8s.io
  - extensions
  - kubeapps.com
  - metrics.k8s.io
  - networking.k8s.io
  - node.k8s.io
  - policy
  - rbac.authorization.k8s.io
  - samplecontroller.k8s.io
  - scheduling.k8s.io
  - storage.k8s.io
  - storage.k8s.io	
- Versionings
  - v1alpha1
  - v1beta1
  - v1beta2
  - v2beta3
  - v1
- Access
    - 在非core group的使用`/api/v1/namespaces/{namespace}/{resourcename}/{name}` 格式访问
      ```
        GET /apis/apps/v1/deployments
        GET /apis/apps/v1/namespaces/{namespace}/deployments
        GET /apis/apps/v1/namespaces/{namespace}/deployments/{name}
        GET /apis/apps/v1/watch/namespaces/{namespace}/deployments
        GET /apis/apps/v1/watch/namespaces/{namespace}/deployments/{name}
        GET /apis/apps/v1/namespaces/{namespace}/deployments/{name}/status
        GET /apis/apps/v1/namespaces/{namespace}/deployments/{name}/scale
      ```
    - Service,POD,ReplicationController等在core group的则使用`/api/`
        ```
        GET /api/v1/namespaces/{namespace}/pods/{name}
        GET /api/v1/services
        GET /api/v1/namespaces/{namespace}/services
        GET /api/v1/namespaces/{namespace}/services/{name}
        GET /api/v1/namespaces/{namespace}/services/{name}/status
        GET /api/v1/namespaces/{namespace}/services/{name}/proxy
        GET /api/v1/namespaces/{namespace}/services/{name}/proxy/{path}
        ```
    - 查询属性
      - log: pod专属
      - status
      - scale
      - proxy
#### 访问服务
https://kubernetes.io/docs/tasks/access-application-cluster/access-cluster/
- /api/v1/namespaces/namespace_name/services/[https:]service_name[:port_name]/proxy
- 命令行
  ```
        APISERVER=$(kubectl config view --minify | grep server | cut -f 2- -d ":" | tr -d " ")
        SECRET_NAME=$(kubectl get secrets | grep ^default | cut -f1 -d ' ')
        TOKEN=$(kubectl describe secret $SECRET_NAME | grep -E '^token' | cut -f2 -d':' | tr -d " ")
        curl $APISERVER/api --header "Authorization: Bearer $TOKEN" --insecure
  ```
  ```
    APISERVER=$(kubectl config view --minify -o jsonpath='{.clusters[0].cluster.server}')
    TOKEN=$(kubectl get secret $(kubectl get serviceaccount default -o jsonpath='{.secrets[0].name}') -o jsonpath='{.data.token}' | base64 --decode )
    curl $APISERVER/api --header "Authorization: Bearer $TOKEN" --insecure
  ```
#### Fetch Log
```
GET /api/v1/namespaces/{namespace}/pods/{name}/log
```
## API List
不带Version的返回APIGroup，包含各个version
```
/: 返回所有URL
/api: 返回APIVersions
/api/v1": 上一个的v1版本，返回APIResourceList
/apis": APIGroupList
/apis/": 同上
/apis/admissionregistration.k8s.io: 
/apis/admissionregistration.k8s.io/v1beta1: 
/apis/apiextensions.k8s.io: 
/apis/apiextensions.k8s.io/v1beta1: 
/apis/apiregistration.k8s.io: 
/apis/apiregistration.k8s.io/v1: 
/apis/apiregistration.k8s.io/v1beta1: 
/apis/apps: 
/apis/apps/v1: 
/apis/apps/v1beta1: 
/apis/apps/v1beta2: 
/apis/authentication.k8s.io: 
/apis/authentication.k8s.io/v1: 
/apis/authentication.k8s.io/v1beta1: 
/apis/authorization.k8s.io: 
/apis/authorization.k8s.io/v1: 
/apis/authorization.k8s.io/v1beta1: 
/apis/autoscaling: 
/apis/autoscaling/v1: 
/apis/autoscaling/v2beta1: 
/apis/batch: 
/apis/batch/v1: 
/apis/batch/v1beta1: 
/apis/certificates.k8s.io: 
/apis/certificates.k8s.io/v1beta1: 
/apis/events.k8s.io: 
/apis/events.k8s.io/v1beta1: 
/apis/extensions: 
/apis/extensions/v1beta1: 
/apis/kubeapps.com: 
/apis/kubeapps.com/v1alpha1: 
/apis/metrics.k8s.io: 
/apis/metrics.k8s.io/v1beta1: 
/apis/networking.k8s.io: 
/apis/networking.k8s.io/v1: 
/apis/policy: 
/apis/policy/v1beta1: 
/apis/rbac.authorization.k8s.io: 
/apis/rbac.authorization.k8s.io/v1: 
/apis/rbac.authorization.k8s.io/v1beta1: 
/apis/samplecontroller.k8s.io: 
/apis/samplecontroller.k8s.io/v1alpha1: 
/apis/scheduling.k8s.io: 
/apis/scheduling.k8s.io/v1beta1: 
/apis/storage.k8s.io: 
/apis/storage.k8s.io/v1: 
/apis/storage.k8s.io/v1beta1: 
/healthz: 
/healthz/autoregister-completion: 
/healthz/etcd: 
/healthz/ping: 
/healthz/poststarthook/apiservice-openapi-controller: 
/healthz/poststarthook/apiservice-registration-controller: 
/healthz/poststarthook/apiservice-status-available-controller: 
/healthz/poststarthook/bootstrap-controller: 
/healthz/poststarthook/ca-registration: 
/healthz/poststarthook/generic-apiserver-start-informers: 
/healthz/poststarthook/kube-apiserver-autoregistration: 
/healthz/poststarthook/scheduling/bootstrap-system-priority-classes: 
/healthz/poststarthook/start-apiextensions-controllers: 
/healthz/poststarthook/start-apiextensions-informers: 
/healthz/poststarthook/start-kube-aggregator-informers: 
/healthz/poststarthook/start-kube-apiserver-admission-initializer: 
/healthz/poststarthook/start-kube-apiserver-informers: 
/logs: 
/metrics: 
/openapi/v2: 所有接口描述(非常大))
/swagger-2.0.0.json: 同上
/swagger-2.0.0.pb-v1: 同上
/swagger-2.0.0.pb-v1.gz: 同上
/swagger.json: 同上
/swaggerapi: 同上
/version: 显示k8s版本及编译信息
```
