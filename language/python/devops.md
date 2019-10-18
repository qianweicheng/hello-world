# Stack
- https://github.com/vinta/awesome-python
- https://www.jianshu.com/p/ee0e07dcd969
## DevOps 工具
- Ansible
- Fabric, cuisine, Fabtools
- [supervisor](http://supervisord.org/configuration.htm)
    supervisord : 启动supervisor
    supervisorctl reload :修改完配置文件后重新启动supervisor
    supervisorctl status :查看supervisor监管的进程状态
    supervisorctl start 进程名 ：启动XXX进程
    supervisorctl stop 进程名 ：停止XXX进程
    supervisorctl stop all：停止全部进程，注：start、restart、stop都不会载入最新的配置文件。
    supervisorctl update：启动新配置或有改动的进程，配置没有改动的进程不会受影响而重启