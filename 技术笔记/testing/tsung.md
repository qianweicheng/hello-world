0 安装编译环境：yum install -y autoconf make gcc 
1 安装erlang
    a. 直接安装： yum install -y erlang #安装erlang
    b. 从源码安装：
        rpm -Uvh http://mirrors.kernel.org/fedora-epel/epel-release-latest-7.noarch.rpm
        yum install -y clang m4 mcurses termcap termlib git
        git clone https://github.com/erlang/otp.git
        cd otp
        ./otp_build autoconf
        ./configure && make && make install
2 安装tsung
    #安装其它依赖
    yum install -y gnuplot perl-Template-Toolkit 
    pip install matplotlib
    #下载tsung源码
    wget http://tsung.erlang-projects.org/dist/tsung-1.6.0.tar.gz
    tar -xvf tsung-1.6.0.tar.gz
    #编译tsung
    ./configure && make && make install 

===========TSUNG使用==================
tsung -f xxx.xml start
生成报告：
进入报告目录， 运行：
根据安装目录有可能不一致：
/usr/lib/tsung/bin/tsung_stats.pl
/usr/local/tsung/lib/tsung/bin/tsung_stats.pl
http://xxxx/report.html
tsung默认开放8091端口用于监控当前压测状态：http://xxxx:8091/index.html 
