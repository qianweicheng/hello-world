# Storage
## Types of Volumes
- configMap
- emptyDir
- hostPath
- local
- nfs
- persistentVolumeClaim
- secret
- awsElasticBlockStore
- 其他
## Example
```
    volumes:
    - name: cache-volume
      emptyDir: {}
    - name: test-volume
      hostPath:
        # directory location on host
        path: /data
        # this field is optional
        type: Directory
```
## Persistent Volumes
#### Reclaiming
- Retain
  - `kubectl patch pv <your-pv-name> -p '{"spec":{"persistentVolumeReclaimPolicy":"Retain"}}'`
- Delete（默认）
- Recycle（废弃）
## 挂载参数
- mountPath
- mountPropagation
- name
- readOnly: 只对volumn有效，对configmap，secret无效
- subPath: 
  - 挂载单个文件时候,或者单个子文件夹时使用
  - 使用subPath挂载的不能自动刷新，无法感知变化，只能重启pod
- subPathExpr
## Demo
```
containers:
- name: hello-world
  image: nginx
  volumeMounts:
  - name: admin-config2
    mountPath: /etc/nginx/nginx.conf
    subPath: nginx.conf
    readOnly: true
  - name: admin-config2
    mountPath: /usr/share/nginx/html
volumes:
- name: admin-config2
  configMap:
    name: admin-config2
```