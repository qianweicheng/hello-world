# Linux依赖
## Repositories
帮助文档: http://mirrors.ustc.edu.cn/help/index.html
## Alpine
apk进行包管理
-  添加repositories:
    `echo http://dl-cdn.alpinelinux.org/alpine/latest-stable/main/ > /etc/apk/repositories`
    清华TUNA镜像源：https://mirror.tuna.tsinghua.edu.cn/alpine/
    中科大镜像源：http://mirrors.ustc.edu.cn/alpine/
    阿里云镜像源：http://mirrors.aliyun.com/alpine/
- package查询:
    https://pkgs.alpinelinux.org/packages
    `apk add --update alpine-sdk`
## Deiban/Ubuntu:apt-get
Ubuntu系列依赖库：https://packages.ubuntu.com/xenial/devel/
- 依赖: python-pip redis-tools dnsutils
- 删除已安装包（不保留配置文件): 
    - apt-get purge / apt-get –purge remove 如软件包a，依赖软件包b，则执行该命令会删除a，而且不保留配置文件
    - apt-get autoremove 删除为了满足依赖而安装的，但现在不再需要的软件包（包括已安装包），保留配置文件。
- 单纯安装:`apk add --no-cache curl perl`
## Redhat/Centos:yum
Redhat系列依赖库:https://rpmfind.net/linux/RPM/index.html
- 方法1: `yum -y install epel-release`
- 方法2: 安装EPEL:http://mirrors.kernel.org/fedora-epel/
    `rpm -Uvh http://mirrors.kernel.org/fedora-epel/epel-release-latest-7.noarch.rpm`
    或者
    `yum-config-manager --enable epel`
## 常用依赖
- 编译相关
    - `apt-get install build-essential`
        depends: gcc g++ make dpkg-dev libc6-dev
    - `apk add .build-deps`
    - `yum groupinstall "Development Tools"` or 简化版`yum install -y gcc g++ kernel-devel`
    - archlinux: base-devel
- automake: 自动生成makefile的。
- aptitude: aptitude可以比apt-get更加智能地解决依赖问题，先安装它：
- 常用工具
    curl,wget,telnet,netcat,openssl-devel, dnsutils(包括dig, nslookup, host)
## Mac: HomeBrew
- brew tap 第三方包路径
    ```
        brew tap facebook/fb
        brew install buck
    ```
    ```
        brew untap
    ```
- brew install/uninstall
- brew update
- Link:
    删除快捷方式：`brew unlink nginx`
    添加快捷方式：`brew link nginx-full`
## RPM
`rpm -i xxx.rpm`
`rpm -e xxx`
`rpm -Uvh xxx.rpm`
`rpm -q example`
#### 清理
```
brew doctor 
brew cleanup --prune-prefix
brew update
```
## Lua
luarocks