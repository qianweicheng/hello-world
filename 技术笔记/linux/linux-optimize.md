/etc/security/limits.conf  limits.conf是针对用户
/etc/sysctl.conf            sysctl.conf是针对整个系统参数配置。
ulimit针对当前session的修改，默认值从limits.conf加载
===========/etc/sysctl.conf，sysctl -p立即生效==================
所有可设置选项参考/proc/sys/里面
==============================================================
# 系统总共可打开文件数
fs.file-max=1048576
# 单个总共可打开文件数
fs.nr_open=1048576
# 是否可以端口转发
net.ipv4.ip_forward=0;
net.ipv4.tcp_syncookies=1;
# 表示开启重用，允许将TIME-WAIT Sockets重新用于新的TCP连接，默认为0，表示关闭。
# 1. 这个对快速重启动某些服务,而启动后提示端口已经被使用的情形非常有帮助。
# 2. 对于大量的短连接非常有帮助
net.ipv4.tcp_tw_reuse=1;
# 表示开启TCP连接中TIME-WAIT Sockets的快速回收，默认为0，表示关闭。
net.ipv4.tcp_tw_recycle=1;
# 等待TCP断开超时时间，减少处于FIN-WAIT-2连接状态的时间，使系统可以处理更多的连接，预防DDOS
net.ipv4.tcp_fin_timeout=30;
net.ipv4.ip_local_port_range="1024 65535"
# TCP接收缓存大小
net.ipv4.tcp_rmem=4096 87380 16777216;
# TCP发送缓存大小
net.ipv4.tcp_wmem=4096 65536 16777216;
# Timestamps可以防范那些伪造的sequence号码。一条1G的宽带线路或许会重遇到带out-of-line数值的旧sequence号码(假如它是由于上次产生的)。时间戳能够让内核接受这种“异常”的数据包。这里需要将其关掉,以提高性能。
net.ipv4.tcp_timestamps=1; 
# 当网卡接收数据包的速度大于内核处理的速度时，会有一个队列保存这些数据包。这个参数表示该队列的最大值
net.ipv4.tcp_max_syn_backlog=65536; 
net.ipv4.tcp_max_orphans=3276800; 
# 减少系统SYN连接重试次数（默认是5）
net.ipv4.tcp_synack_retries=3; 
# 在内核放弃建立连接之前发送SYN包的数量。
net.ipv4.tcp_syn_retries=3; 
# 系统同时保持TIME_WAIT套接字的最大数量
net.ipv4.tcp_max_tw_buckets=360000; 
net.ipv4.tcp_mem="786432 2097152 3145728"; 
net.ipv4.tcp_retries2=5; 
net.ipv4.tcp_retries1=3; 
net.ipv4.tcp_orphan_retries=1; 
net.ipv4.tcp_no_metrics_save=1; 
net.ipv4.conf.default.rp_filter=1;
net.ipv4.conf.default.accept_source_route=0;

net.core.netdev_max_backlog=32768;
# 用来限制监听(LISTEN)队列最大数据包的数量，超过这个数量就会导致链接超时或者触发重传机制
net.core.somaxconn=32768; 
# 这个参数表示内核套接字接收缓存区最大大小(包括UDP)
net.core.rmem_max=16777216; 
# 这个参数表示内核套接字写入缓存区最大大小(包括UDP)
net.core.wmem_max=16777216;
# 这个参数表示内核套接字接收缓存区默认的大小
net.core.rmem_default=212992;
# 这个参数表示内核套接字发送缓存区默认的大小
net.core.wmem_default=212992;

net.bridge.bridge-nf-call-ip6tables=0
net.bridge.bridge-nf-call-iptables=0
net.bridge.bridge-nf-call-arptables=0
# 当系统认为没有足够的lowmem，而触发OOM Killer，将进程强行杀掉
vm.min_free_kbytes=65536; 
vm.swappiness=0;
vm.overcommit_memory=1;
vm.max_map_count=200000

# 该文件指定一个消息队列的最大长度（bytes）
kernel.msgmnb=16384


===============/etc/security/limits.conf=====================
* soft nofile 1048576
* hard nofile 1048576 

#root 需要单独设置