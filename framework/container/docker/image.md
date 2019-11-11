# Docker Image
https://hub.docker.com/search/?category=base&source=verified&type=image
## 常用基础Docker镜像
alpine
scratch
docker.io/jeanblanchard/alpine-glibc
golang
buildpack-deps:jessie > jessie-scm > jessie-curl > debian:jessie(50M)
python:2/3 > buildpack-deps:stretch
openjdk:7 > buildpack-deps:stretch-scm
openjdk:7-slim > debian:stretch-slim
openjdk:alpine > alpine
alpine-java:7/8/7_jdk... #Oracle JDK
Ubuntu
CentOS
Debian
### 常见tag
- alpine: based on the Alpine Linux. 缺点是部分lib不是标准的`musl libc vs glibc`
- slim: 经过裁剪的，只包含当前app需要的lib
- stretch: Debian 9
- jessie: Debian 8
- slim-stretch
### python alpine
- Alpine has a smaller default stack size for threads, which can lead to Python crashes.
- One Alpine user discovered that their Python application was much slower because of the way musl allocates memory vs. glibc.
- I once couldn’t do DNS lookups in Alpine images running on minikube (Kubernetes in a VM) when using the WeWork coworking space’s WiFi. The cause was a combination of a bad DNS setup by WeWork, the way Kubernetes and minikube do DNS, and musl’s handling of this edge case vs. what glibc does. musl wasn’t wrong (it matched the RFC), but I had to waste time figuring out the problem and then switching to a glibc-based image.
- Another user discovered issues with time formatting and parsing. 

## 镜像构建
### ENTRYPOINT 指令的两种格式：
- ENTRYPOINT ["executable", "param1", "param2"] (the preferred exec form)
- ENTRYPOINT command param1 param2 (shell form)
CMD 指令的三种格式：
- CMD ["executable","param1","param2"] (exec form, this is the preferred form)
- CMD ["param1","param2"] (as default parameters to ENTRYPOINT)
- CMD command param1 param2 (shell form)

> 备注：不能通过rc.local文件设置自动启动
### ADD vs COPY
ADD 会自动解压zip等压缩包
ADD/COPY  不能直接使用"COPY * ./"， 会把当前文件夹下的子文件目录结构丢失，全部扁平了
ADD指令不仅能够将构建命令所在的主机本地的文件或目录，而且能够将远程URL所对应的文件或目录，作为资源复制到镜像文件系统。
所以，可以认为ADD是增强版的COPY，支持将远程URL的资源加入到镜像的文件系统
拷贝文件夹需要:
ADD/COPY folder1 ./folder1/
不能:
ADD/COPY folder1 ./
### 条件拷贝
COPY foo file-which-may-exist* /target
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