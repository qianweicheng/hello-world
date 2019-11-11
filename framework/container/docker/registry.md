# Registry
## Install: 
  - `docker run -d -p 5000:5000 --name registry registry:2`
  - `docker run -d -p 5000:5000 --restart=always --name registry registry:2`
## Config
- htpasswd 加密方式必须是bcrypt
- 添加用户
  ```
  docker run \
  --entrypoint htpasswd \
  registry:2 -Bbn testuser testpassword > auth/htpasswd
  ```
## Copy an Image from DockerHub to registry
```
docker pull ubuntu:16.04
docker tag ubuntu:16.04 localhost:5000/my-ubuntu
docker push localhost:5000/my-ubuntu
```
## Test
- ping: GET /v2/
- list images: GET /v2/_catalog
- list image tags: GET /v2/<name>/tags/list

## 搭载私有docker hub
参考文档：https://docs.docker.com/registry/deploying/
docker run -d -p 5000:5000 -v /opt/data/registry:/tmp/registry registry
在”/etc/docker/“目录下，创建”daemon.json“文件。在文件中写入：
{
    "insecure-registries": [
        "your url:5000"
    ]
}