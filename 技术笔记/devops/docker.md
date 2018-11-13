#Docker配置
/etc/sysconfig
.docker 私有库用户名密码

#新建镜像
docker build -t busybox .
docker tag busybox edisonchat/busybox
docker push edisonchat/busybox

docker ps #列出运行中的docker
docker images #列出所有本机的镜像
docker rm -f $(docker ps -a -q) #清理docker
docker start 启动已经停止的docker
docker stop 停止守护式docker
docker exec 命令在容器内部额外启动新进程。
$ docker exec -t -i aofo /bin/bash
docker run \
--name myname \
-p 8080:80 \
-v 文件映射 \
-u root \
-d #守护模式 \
ubuntu:14.04 /bin/sh -c "xxxx" 
docker attach 
docker inspect 获取容器内部信息
docker port NAME 查看端口映射情况。
docker logs NAME
#镜像启动
ENTRYPOINT 指令的两种格式：
ENTRYPOINT ["executable", "param1", "param2"] (the preferred exec form)
ENTRYPOINT command param1 param2 (shell form)
CMD 指令的三种格式：
CMD ["executable","param1","param2"] (exec form, this is the preferred form)
CMD ["param1","param2"] (as default parameters to ENTRYPOINT)
CMD command param1 param2 (shell form)

备注：不能通过rc.local文件设置自动启动

Docker日记
/var/lib/docker/containers/
--log-opt max-size=10m --log-opt max-file=3

#搭载私有docker hub
参考文档：https://docs.docker.com/registry/deploying/
docker run -d -p 5000:5000 -v /opt/data/registry:/tmp/registry registry
在”/etc/docker/“目录下，创建”daemon.json“文件。在文件中写入：
{
    "insecure-registries": [
        "your url:5000"
    ]
}

#常用基础Docker镜像：
FROM alpine:latest
FROM docker.io/jeanblanchard/alpine-glibc
FROM golang:1.8
FROM buildpack-deps:jessie > jessie-scm > jessie-curl > debian:jessie(50M)
FROM python:2/3 > buildpack-deps:stretch
FROM openjdk:7 > buildpack-deps:stretch-scm
FROM openjdk:7-slim > debian:stretch-slim
FROM openjdk:alpine > alpine
FROM alpine-java:7/8/7_jdk... #Oracle JDK

ADD vs COPY
ADD 会自动解压zip等压缩包
ADD/COPY  不能直接使用"COPY * ./"， 会把当前文件夹下的子文件目录结构丢失，全部扁平了
ADD指令不仅能够将构建命令所在的主机本地的文件或目录，而且能够将远程URL所对应的文件或目录，作为资源复制到镜像文件系统。
所以，可以认为ADD是增强版的COPY，支持将远程URL的资源加入到镜像的文件系统
拷贝文件夹需要:
ADD/COPY folder1 ./folder1/
不能:
ADD/COPY folder1 ./

#Docker in Docker
直接映射到宿主机的docker(mac和linux的安装地址不一样)
docker run --name jenkins -d  -p 8080:8080 jenkins/jenkins:lts
docker run -it -v /var/run/docker.sock:/var/run/docker.sock -v /usr/bin/docker:/usr/bin/docker --name jenkins -d  -p 8080:8080 jenkins/jenkins:lts
> 映射/var/run/docker.sock可以利用宿主机的dockerd，docker内部本身可以自己安装docker client，或者映射宿主机的client

#坑
运行在docker里面的程序新开启的文件会被docker缓存而得不到释放，从而造成内存泄漏