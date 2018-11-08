#Squid
##Install
`yum install -y squid`
##Config
- 前台启动squid，并输出启动过程
    /usr/local/squid/sbin/squid -N -d1
- 启动squid在后台运行
    squid -s
- 停止squid
    squid -k shutdown
- squid -k reconfigure -f /XXX/squid.conf
- 检查配置是否有效: squid -k parse