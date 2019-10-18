# Windows
## powershell
$env:path
## wget -O "下载文件名" url
## python 安装
1. 下载安装Python
2. 下载安装pip，windows版本不自带pip
3. 设置环境变量
## docker
- Home Edison 需要安装VirtualBox
- 本质是开启了一个虚拟机运行docker，所以映射的端口不能
    `docker-machine ip default` 一般是`ssh docker@192.168.99.100` pwd:tcuser