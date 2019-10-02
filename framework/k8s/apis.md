# Info
## Commands
- `kubectl api-versions`
- `kubectl cluster-info`
- `kubectl get apiservices`
- 测试最好使用`kubectl proxy`
## API groups & versioning
/apis/$GROUP_NAME/$VERSION
- Groups
  - /api/v1
  - /api/batch/v1
- API versioning
  - /api/v1alpha1
  - /api/v2beta3
  - /api/v1
## APIs
- /  约等于 /swaggerapi
    所有的RESTful API
- /openapi/v2 == /swagger-2.0.0.json
    详细的RESTful API 列表说明
- /api:废弃
    kind: APIVersions
- /api/v1:废弃
    kind: APIResourceList
- /apis 
    kind: APIGroupList
- /apis/apps/v1
    `/apis/apps/v1:APIResourceList(/apis/group-name/version)`
    kind: APIResourceList
- /apps/v1/deployments
- /apps/v1/namespaces/default/deployments
    这个包含了deployment statefulset 等资源
## 访问服务
https://kubernetes.io/docs/tasks/access-application-cluster/access-cluster/
- /api/v1/namespaces/namespace_name/services/[https:]service_name[:port_name]/proxy
- 命令行
  ```
        APISERVER=$(kubectl config view --minify | grep server | cut -f 2- -d ":" | tr -d " ")
        SECRET_NAME=$(kubectl get secrets | grep ^default | cut -f1 -d ' ')
        TOKEN=$(kubectl describe secret $SECRET_NAME | grep -E '^token' | cut -f2 -d':' | tr -d " ")
        curl $APISERVER/api --header "Authorization: Bearer $TOKEN" --insecure
  ```
## APIs
"/api",
"/api/v1",
"/apis",
"/apis/",
"/apis/admissionregistration.k8s.io",
"/apis/admissionregistration.k8s.io/v1beta1",
"/apis/apiextensions.k8s.io",
"/apis/apiextensions.k8s.io/v1beta1",
"/apis/apiregistration.k8s.io",
"/apis/apiregistration.k8s.io/v1",
"/apis/apiregistration.k8s.io/v1beta1",
"/apis/apps",
"/apis/apps/v1",
"/apis/apps/v1beta1",
"/apis/apps/v1beta2",
"/apis/authentication.k8s.io",
"/apis/authentication.k8s.io/v1",
"/apis/authentication.k8s.io/v1beta1",
"/apis/authorization.k8s.io",
"/apis/authorization.k8s.io/v1",
"/apis/authorization.k8s.io/v1beta1",
"/apis/autoscaling",
"/apis/autoscaling/v1",
"/apis/autoscaling/v2beta1",
"/apis/batch",
"/apis/batch/v1",
"/apis/batch/v1beta1",
"/apis/certificates.k8s.io",
"/apis/certificates.k8s.io/v1beta1",
"/apis/events.k8s.io",
"/apis/events.k8s.io/v1beta1",
"/apis/extensions",
"/apis/extensions/v1beta1",
"/apis/kubeapps.com",
"/apis/kubeapps.com/v1alpha1",
"/apis/metrics.k8s.io",
"/apis/metrics.k8s.io/v1beta1",
"/apis/networking.k8s.io",
"/apis/networking.k8s.io/v1",
"/apis/policy",
"/apis/policy/v1beta1",
"/apis/rbac.authorization.k8s.io",
"/apis/rbac.authorization.k8s.io/v1",
"/apis/rbac.authorization.k8s.io/v1beta1",
"/apis/samplecontroller.k8s.io",
"/apis/samplecontroller.k8s.io/v1alpha1",
"/apis/scheduling.k8s.io",
"/apis/scheduling.k8s.io/v1beta1",
"/apis/storage.k8s.io",
"/apis/storage.k8s.io/v1",
"/apis/storage.k8s.io/v1beta1",
"/healthz",
"/healthz/autoregister-completion",
"/healthz/etcd",
"/healthz/ping",
"/healthz/poststarthook/apiservice-openapi-controller",
"/healthz/poststarthook/apiservice-registration-controller",
"/healthz/poststarthook/apiservice-status-available-controller",
"/healthz/poststarthook/bootstrap-controller",
"/healthz/poststarthook/ca-registration",
"/healthz/poststarthook/generic-apiserver-start-informers",
"/healthz/poststarthook/kube-apiserver-autoregistration",
"/healthz/poststarthook/scheduling/bootstrap-system-priority-classes",
"/healthz/poststarthook/start-apiextensions-controllers",
"/healthz/poststarthook/start-apiextensions-informers",
"/healthz/poststarthook/start-kube-aggregator-informers",
"/healthz/poststarthook/start-kube-apiserver-admission-initializer",
"/healthz/poststarthook/start-kube-apiserver-informers",
"/logs",
"/metrics",
"/openapi/v2",
"/swagger-2.0.0.json",
"/swagger-2.0.0.pb-v1",
"/swagger-2.0.0.pb-v1.gz",
"/swagger.json",
"/swaggerapi",
"/version"

## 扩展Kubernates API
允许在不修改源代码的前提下扩展。方式有两个
- API Aggregation
  - 通过apiserver-builder创建
  - sample-apiserver和apiserver-builder/example
- CRD

