# Linux服务
在Linux生态系统中，Systemd被部署到了大多数的标准Linux发行版中，只有为数不多的几个发行版尚未部署。systemd服务来代替daemon
两大管理系统
- service+chkconfig: linux最初的服务管理系统
    `service xxxxx start/stop/status` or `/etc/init.d/xxxx start`
    自动启动停止服务:
    `chkconfig --add/del`
    `chkconfig –level 2345 nginx on`
- systemctl: (Centos)systemctl命令兼容了service
    `systemctl start/status/restart/enable/disable xxx`

    systemctl|service|chkconfig|备注
    -|-|-|-
    systemctl start [unit type]|service [服务] start||
    systemctl stop [unit type]|service [服务] stop||
    systemctl restart [unit type]|service [服务] restart||
    systemctl enable [unit type]||chkconfig [服务] on|开机自启动
    systemctl disable [unit type]||chkconfig [服务] off|关闭开机自启动
    systemctl is-active [unit type]||| 查看服务是否运行
    systemctl is-enable [unit type]|||查看服务是否设置为开机启动
    systemctl mask [unit type]||| 注销指定服务
    systemctl unmask [unit type]|||取消注销指定服务
    systemctl poweroff|init 0||关机