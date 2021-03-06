# Docker
## Docker Daemon
- 启动服务
  ```
    systemctl enable docker
    systemctl start docker
  ```
- 关闭服务
  ```
    systemctl stop docker
    systemctl disable docker
    yum -y remove docker
  ```
- daemon监听: /var/run/docker.sock， client通过/var/run/docker.sock与daemon通讯, 通过监听docker.sock获取docker事件流
`curl --unix-socket /var/run/docker.sock http://localhost/events`
- 日记: /var/lib/docker/containers/ --log-opt max-size=10m --log-opt max-file=3
- 配置
  - /etc/sysconfig
  - .docker 私有库用户名密码
## 常用命令
https://docs.docker.com/engine/reference/commandline/docker/
- 生命周期管理
  - run:
    ```
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
    ```
  - start/stop/restart
  - kill
  - rm: `docker rm -f $(docker ps -a -q) #清理docker`
  - pause/unpause
  - create
  - exec:`docker exec -t -i aofo /bin/bash # 必须正在运行的`
- 容器操作
  - ps: `docker images #列出所有本机的镜像`
  - inspect: `docker inspect 获取容器内部信息`
  - top: 
  - attach: `docker attach 可以attach到一个已经运行的容器的stdin，然后进行命令执行的动作。 但是需要注意的是，如果从这个stdin中exit，会导致容器的停止. "docker attach xxx"`
  - events
  - logs: `docker logs NAME`
  - wait
  - export
  - port: `docker port NAME 查看端口映射情况。`
- 容器rootfs命令
  - commit
  - cp
  - diff
- Image hub
  - login: `docker login`
  - pull: `docker pull edisonchat/busybox`
  - push: `docker push edisonchat/busybox`
  - search
- local image
  - images
  - rmi
  - tag: `docker tag busybox edisonchat/busybox`
  - build: `docker build -t busybox .`
  - history
  - save
  - load
  - import
- info
  - info: 
  - version
## Docker 挂载目录权限问题
在CentOS7中，挂载的本地目录在容器中没有执行权限，原因是CentOS7安全模块selinux把权限禁掉了，至少有以下三种方式解决挂载的目录没有权限的问题：
1. 在运行容器的时候，给容器加特权
    `--privileged=true`
2. 临时关闭selinux: `su -c "setenforce 0"`
3. 添加selinux规则，将要挂载的目录添加到白名单

## Docker in Docker
直接映射到宿主机的docker(mac和linux的安装地址不一样)
```
docker run --name jenkins -d  -p 8080:8080 jenkins/jenkins:lts
docker run 
-it 
-d  
-p 8080:8080 
-v /var/run/docker.sock:/var/run/docker.sock  #将docker daemon映射进来
-v /usr/bin/docker:/usr/bin/docker # 把docker 客户端工具映射进来
--name jenkins 
jenkins/jenkins:lts
```
> 映射/var/run/docker.sock可以利用宿主机的dockerd，docker内部本身可以自己安装docker client，或者映射宿主机的client

## Network
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
## Volume
- `-v /data`: 将本地`/var/lib/docker/volumes/xxx`自动创建一个文件夹映射到`/data/`中。
- 在Dockerfile文件中: `VOLUME /data`声明，作用同上
- `-v /data:/data`: 将本地`/data`映射到容器的`/data`
- `-v data:/data`: 将名字为data的volume映射到`/data`
## 坑
- 运行在docker里面的程序新开启的文件会被docker缓存而得不到释放(存放在cache中). 导致统计偏差
- 使用alpine等精简的base image可能确实部分东西,如证书等，可以通过目录自己添加.`RUN apk --no-cache add ca-certificates`