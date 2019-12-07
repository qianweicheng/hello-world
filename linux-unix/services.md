# Linux服务
在Linux生态系统中，Systemd被部署到了大多数的标准Linux发行版中，只有为数不多的几个发行版尚未部署。systemd服务来代替daemon
## 两大管理系统
- service+chkconfig: linux最初的服务管理系统
    - 开启关闭: `service xxxxx start/stop/status`
    - 直接运行脚本: `/etc/init.d/xxxx start`
    - 开机自动启动停止: `chkconfig --add/del` or `chkconfig –level 2345 nginx on`
- systemctl: (Centos)systemctl命令兼容了service
    - 启动关闭: `systemctl start/status/restart xxx.service`
    - 开机自动启动停止: `systemctl enable/disable xxx.service`
    - 添加自动运行并且立即启动:`systemctl enable --now xxx.service`
      - List: `systemctl list-units`
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
## 添加一个应用到服务
- Write the script:`/etc/systemd/system/YOUR_SERVICE_NAME.service`  
    - Service节必须，Type属性控制开启的细节行为。RemainAfterExit

    ```
    [Unit]
    # man systemd.unit
    Description=your_config
    Documentation=http://tuxgraphics.org/npa/
    After=network.target syslog.target
    Before=httpd.service
    Wants=httpd.service
    [Service]
    Type=simple
    ExecStart=YOUR_COMMAND_HERE
    Restart=on-failure
    RestartSec=10
    KillMode=process
    [Install]
    WantedBy=multi-user.target
    ```
- Reload services:`systemctl daemon-reload`
- Start the service: `systemctl start YOUR_SERVICE_NAME`
- Add to Startup List: `systemctl enable YOUR_SERVICE_NAME`
### 参考文档: 
https://www.freedesktop.org/software/systemd/man/systemd.service.html
https://www.freedesktop.org/software/systemd/man/systemd.unit.htm