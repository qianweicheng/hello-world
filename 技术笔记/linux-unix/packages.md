# Linux依赖
## 编译准备
- apt-get install build-essential
    depends: gcc g++ make dpkg-dev libc6-dev
## Makefile文件
- ./configure
- make
- make install
## 其他常见依赖
    - automake: 自动生成makefile的。
    - aptitude: aptitude可以比apt-get更加智能地解决依赖问题，先安装它：
    - 域名相关: dig, nslookup, host
        apt-get install dnsutils
        yum install bind-utils
    - curl,wget,telnet,netcat
## Redhat:yum
Redhat系列依赖库:https://rpmfind.net/linux/RPM/index.html
- 安装EPEL:http://mirrors.kernel.org/fedora-epel/
    `rpm -Uvh http://mirrors.kernel.org/fedora-epel/epel-release-latest-7.noarch.rpm`
    或者
    `yum-config-manager --enable epel`
## Ubuntu:apt-get
Ubuntu系列依赖库：https://packages.ubuntu.com/xenial/devel/
- 依赖: python-pip redis-tools dnsutils
- 删除已安装包（不保留配置文件): 
    - apt-get purge / apt-get –purge remove 如软件包a，依赖软件包b，则执行该命令会删除a，而且不保留配置文件
    - apt-get autoremove 删除为了满足依赖而安装的，但现在不再需要的软件包（包括已安装包），保留配置文件。
# Mac: HomeBrew
- brew tap 第三方包路径
- brew install/uninstall
- brew update
- Link:
    删除快捷方式：`brew unlink nginx`
    添加快捷方式：`brew link nginx-full`