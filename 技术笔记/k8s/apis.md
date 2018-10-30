# /  约等于 /swaggerapi
所有的RESTful API
#/openapi/v2 == /swagger-2.0.0.json
详细的RESTful API 列表说明
#/api:废弃
kind: APIVersions
#/api/v1:废弃
kind: APIResourceList
#/apis 
kind: APIGroupList
#/apis/apps/v1
> /apis/apps/v1:APIResourceList(/apis/group-name/version)
kind: APIResourceList
- /apps/v1/deployments
- /apps/v1/namespaces/default/deployments
这个包含了deployment statefulset 等资源

#访问服务
http://kubernetes_master_address/api/v1/namespaces/namespace_name/services/service_name[:port_name]/proxy
https:: http://kubernetes_master_address/api/v1/namespaces/namespace_name/services/https:service_name:[port_name]/proxy
