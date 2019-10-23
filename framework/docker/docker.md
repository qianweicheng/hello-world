# Docker
## Docker Daemon
- 启动服务
  - systemctl enable docker
  - systemctl start docker
- daemon监听: /var/run/docker.sock， client通过/var/run/docker.sock与daemon通讯, 通过监听docker.sock获取docker事件流
`curl --unix-socket /var/run/docker.sock http://localhost/events`
- 日记: /var/lib/docker/containers/ --log-opt max-size=10m --log-opt max-file=3
- 配置
  - /etc/sysconfig
  - .docker 私有库用户名密码
## 常用命令
```
docker build -t busybox .
docker tag busybox edisonchat/busybox
docker push edisonchat/busybox
docker ps #列出运行中的docker
docker images #列出所有本机的镜像
docker rm -f $(docker ps -a -q) #清理docker
docker start 启动已经停止的docker
docker stop 停止守护式docker
docker run 
    --name myname 
    -p 8080:80 
    -v, --volume 文件映射 
    -u root(用户) 
    -d(后台模式)
    -rm 停止后自动删除
    --link: add link to another container(new-name:existing-container)
    --network 选择网络，默认default
    -w, --workdir string
    ubuntu:14.04 /bin/sh -c "xxxx" 
docker exec -t -i aofo /bin/bash # 必须正在运行的
docker attach 
    可以attach到一个已经运行的容器的stdin，然后进行命令执行的动作。 但是需要注意的是，如果从这个stdin中exit，会导致容器的停止. "docker attach xxx"
docker inspect 获取容器内部信息
docker port NAME 查看端口映射情况。
docker logs NAME
```
### 案例
```
docker run -rm -it ubuntu bash
```
## Docker 挂载目录权限问题
在CentOS7中，挂载的本地目录在容器中没有执行权限，原因是CentOS7安全模块selinux把权限禁掉了，至少有以下三种方式解决挂载的目录没有权限的问题：
1. 在运行容器的时候，给容器加特权
    `--privileged=true`
2. 临时关闭selinux: `su -c "setenforce 0"`
3. 添加selinux规则，将要挂载的目录添加到白名单
## 镜像
### ENTRYPOINT 指令的两种格式：
- ENTRYPOINT ["executable", "param1", "param2"] (the preferred exec form)
- ENTRYPOINT command param1 param2 (shell form)
CMD 指令的三种格式：
- CMD ["executable","param1","param2"] (exec form, this is the preferred form)
- CMD ["param1","param2"] (as default parameters to ENTRYPOINT)
- CMD command param1 param2 (shell form)

> 备注：不能通过rc.local文件设置自动启动
### 搭载私有docker hub
参考文档：https://docs.docker.com/registry/deploying/
docker run -d -p 5000:5000 -v /opt/data/registry:/tmp/registry registry
在”/etc/docker/“目录下，创建”daemon.json“文件。在文件中写入：
{
    "insecure-registries": [
        "your url:5000"
    ]
}
### docker 17.05+ 支持多重编译的新特性
使用多阶段构建好处
- 减少镜像Size
- 简化构建过程(如果使用传统方式来减少Size的话，必须通过脚本`docker cp`拷贝文件)
- 提高安全性
```
# FROM golang:latest as builder
FROM golang:latest
WORKDIR /go/src/github.com/sparkdevo/href-counter/
RUN go get -d -v golang.org/x/net/html
COPY app.go    .
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o app .

FROM alpine:latest
RUN apk --no-cache add ca-certificates
WORKDIR /root/
# COPY --from=builder /go/src/github.com/sparkdevo/href-counter/app .
COPY --from=0 /go/src/github.com/sparkdevo/href-counter/app .
CMD ["./app"]
```
### 从另外的image拷贝
`COPY --from=lachlanevenson/k8s-kubectl:v1.10.3 /usr/local/bin/kubectl /usr/local/bin/kubectl`

## Docker in Docker
直接映射到宿主机的docker(mac和linux的安装地址不一样)
docker run --name jenkins -d  -p 8080:8080 jenkins/jenkins:lts
docker run -it -v /var/run/docker.sock:/var/run/docker.sock -v /usr/bin/docker:/usr/bin/docker --name jenkins -d  -p 8080:8080 jenkins/jenkins:lts
> 映射/var/run/docker.sock可以利用宿主机的dockerd，docker内部本身可以自己安装docker client，或者映射宿主机的client

## Docker network
- docker network ls
    默认有三个:
    bridge:bridge(默认)
    host:host
    null:null
- create network:
`docker network create my_net`
`docker network create --driver bridge my_net`
- run within special network
在一个局域网里启动， name相当于host，可以通过其相互连通
`docker run --name xxx --network my_net xxxx`
## 坑
- 运行在docker里面的程序新开启的文件会被docker缓存而得不到释放，从而造成内存泄漏
- 使用alpine等精简的base image可能确实部分东西,如证书等，可以通过目录自己添加。`RUN apk --no-cache add ca-certificates`