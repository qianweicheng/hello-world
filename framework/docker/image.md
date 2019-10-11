# Image 制作
## 常用基础Docker镜像：
FROM alpine:latest
FROM docker.io/jeanblanchard/alpine-glibc
FROM golang:1.8
FROM buildpack-deps:jessie > jessie-scm > jessie-curl > debian:jessie(50M)
FROM python:2/3 > buildpack-deps:stretch
FROM openjdk:7 > buildpack-deps:stretch-scm
FROM openjdk:7-slim > debian:stretch-slim
FROM openjdk:alpine > alpine
FROM alpine-java:7/8/7_jdk... #Oracle JDK

## 命令
#### ADD vs COPY
ADD 会自动解压zip等压缩包
ADD/COPY  不能直接使用"COPY * ./"， 会把当前文件夹下的子文件目录结构丢失，全部扁平了
ADD指令不仅能够将构建命令所在的主机本地的文件或目录，而且能够将远程URL所对应的文件或目录，作为资源复制到镜像文件系统。
所以，可以认为ADD是增强版的COPY，支持将远程URL的资源加入到镜像的文件系统
拷贝文件夹需要:
ADD/COPY folder1 ./folder1/
不能:
ADD/COPY folder1 ./
#### 条件拷贝
COPY foo file-which-may-exist* /target
## Case1
```
FROM ubuntu
# Install essential stuffs
RUN apt-get update && apt-get install -qy \
        coreutils \
        bash \
        curl \
        sudo \
        git \
        build-essential \
        postgresql-client \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
```