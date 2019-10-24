# ConfigMap&Env
配置文件会自动更新，TTL默认=1 minute，使用subPath挂载的不能自动刷新
## 创建configmap
```
# 通过文件夹创建
kubectl create configmap my-config --from-file=the-folder/
# 直接指定文件,重新指定文件名
kubectl create configmap my-config --from-file=new-file-name=game.properties
# 直接指定文件
kubectl create configmap my-config --from-file=game.properties --from-file=ui.properties
# 也可以直接使用 --from-literal
```
## ConfigMap.yaml
```
apiVersion: v1
kind: ConfigMap
metadata:
  creationTimestamp: 2016-02-18T19:14:38Z
  name: example-config
  namespace: default
data:
  # example of a simple property defined using --from-literal
  example.property.1: hello
  example.property.2: world
  # example of a complex property defined using --from-file
  example.property.file: |-
    property.1=value-1
    property.2=value-2
    property.3=value-3
```
## Secret
secret有多种type(kubernetes/pkg/apis/core/types.go)
- Opaque: 最常见
- kubernetes.io/service-account-token
- kubernetes.io/dockercfg
- kubernetes.io/dockerconfigjson
- kubernetes.io/basic-auth
- kubernetes.io/ssh-auth
- kubernetes.io/tls
- bootstrap.kubernetes.io/token
### data vs dataString
- data会base64编码，
- dataString则原始状态，只写，自动变成base64

```
# 两个同时使用会选择stringData
apiVersion: v1
kind: Secret
metadata:
  name: mysecret
type: Opaque
data:
  username: YWRtaW4=
stringData:
  username: administrator
```
### Create a secret
```
# 普通Opaque
kubectl create secret generic db-user-pass 
--from-file=./username.txt 
--from-file=./password.txt
kubectl create secret generic dev-db-secret 
--from-literal=username=devuser 
--from-literal=password='xxx'
# docker-registry
kubectl create secret docker-registry <name> --docker-server=DOCKER_REGISTRY_SERVER 
--docker-username=DOCKER_USER 
--docker-password=DOCKER_PASSWORD 
--docker-email=DOCKER_EMAIL
```
## ENV变量引用
```
command: ["/bin/sh"]
args: ["-c", "while true; do echo $(MESSAGE); sleep 10;done"]
env:
- name: MY_POD_SERVICE_ACCOUNT
  valueFrom:
    fieldRef:
      fieldPath: spec.serviceAccountName
- name: MY_POD_NAME
  valueFrom:
    fieldRef:
      fieldPath: metadata.name
- name: SPECIAL_LEVEL_KEY
  valueFrom:
    configMapKeyRef:
      # The ConfigMap containing the value you want to assign to SPECIAL_LEVEL_KEY
      name: special-config
      # Specify the key associated with the value
      key: special.how
- name: SECRET_USERNAME
  valueFrom:
    secretKeyRef:
      name: backend-user
      key: backend-username
```
#### 批量配置环境变量
```
envFrom:
- configMapRef:
    name: special-config
- secretRef:
    name: test-secret
```
```
volumes:
  - name: config-volume
    configMap:
      # Provide the name of the ConfigMap containing the files you want
      # to add to the container
      name: special-config
      items:
      - key: SPECIAL_LEVEL
        path: keys
```