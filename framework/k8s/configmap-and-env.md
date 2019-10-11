# ConfigMap&Env
配置文件会自动更新，TTL默认=1 minute
## 创建configmap
- 通过文件夹创建: `kubectl create configmap my-config --from-file=the-folder/`
- 直接指定文件,重新指定文件名: `kubectl create configmap my-config --from-file=new-file-name=game.properties`
- 直接指定文件: `kubectl create configmap my-config-2 --from-file=game.properties --from-file=ui.properties`
- 也可以直接使用`--from-literal`
## ENV变量引用
```
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
```
#### 批量配置环境变量
```
envFrom:
- configMapRef:
    name: special-config
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