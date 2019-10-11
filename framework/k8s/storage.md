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
