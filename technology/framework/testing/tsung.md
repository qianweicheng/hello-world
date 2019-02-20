# Tsung
[官方文档](http://tsung.erlang-projects.org/user_manual)
## 安装erlang
- 安装编译环境：`yum install -y autoconf make gcc`
- 直接安装： `yum install -y erlang` #安装erlang
- 从源码安装：
    ```
        rpm -Uvh http://mirrors.kernel.org/fedora-epel/epel-release-latest-7.noarch.rpm
        yum install -y clang m4 mcurses termcap termlib git
        git clone https://github.com/erlang/otp.git
        cd otp
        ./otp_build autoconf
        ./configure && make && make install
    ```
## 安装tsung
- 安装其它依赖
`yum install -y gnuplot perl-Template-Toolkit`
`pip install matplotlib`
- 下载tsung源码
```
    wget http://tsung.erlang-projects.org/dist/tsung-1.6.0.tar.gz
    tar -xvf tsung-1.6.0.tar.gz
```
- 编译tsung
`./configure && make && make install`

## TSUNG使用
`tsung -f xxx.xml start`
生成报告：
进入报告目录， 运行：
`/usr/lib/tsung/bin/tsung_stats.pl` or
`/usr/local/tsung/lib/tsung/bin/tsung_stats.pl` 
(根据安装目录有可能不一致)
tsung默认开放8091端口用于监控当前压测状态：`http://xxxx:8091/index.html` or `http://xxxx/report.html`
## Tsung配置
**每个子element的顺序必须严格按照dtd的定义顺序**
配置详情: http://tsung.erlang-projects.org/user_manual/dtd.html
`<client type="batch" batch="torque" maxusers="30000" use_controller_vm=false>`
maxusers: 表示一个进程最多开启多少个session，主要避免操作系统对单进程打开文数的限制
use_controller_vm: 默认false，表示当达到了maxusers之后，就开启新的进程
interarrival:每多少秒一个
arrivalrate:每秒多少个
session_setup: 选择session
thinktime：单位秒
rate_limit: <set_option name="rate_limit" value="64" /> #64KB/sec
## 统计
名字|备注
-|-
connect|建立连接数，大部分时候>=session,一般比较接近
session|相当于一个测试用例或者user
page|被thinktime隔开的request就算一个page
transactions|主要为了方便统计，相当于group
request|最终实际请求数