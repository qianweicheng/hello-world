## 用户权限管理相关文件
/etc/group
/etc/passwd
/etc/shadow

## 添加用户
useradd（adduser ->link to useradd）
    Ex: useradd killwall -M -N -s /sbin/nologin -c "Only For Kill Wall"
    Ex: useradd normaluser -c "Only For Kill Wall"
passwd normaluser
userdel
usermod 改变用户所属组(usermod -a -G groupName userName)


用visudo 修改/etc/sudoers 可以让添加的用户有运行sudo的权限
su - （运行新用户的启动脚本，重置环境变量和当前目录）
su （单纯的切换用户，环境变量等保持原有的）

sudoers
1) 配置Host_Alias：就是主机的列表 
Host_Alias      HOST_FLAG = hostname1, hostname2, hostname3 
2) 配置Cmnd_Alias：就是允许执行的命令的列表，命令前加上!表示不能执行此命令. 
命令一定要使用绝对路径，避免其他目录的同名命令被执行，造成安全隐患 ,因此使用的时候也是使用绝对路径! 
Cmnd_Alias      COMMAND_FLAG = command1, command2, command3 ，!command4 
3) 配置User_Alias：就是具有sudo权限的用户的列表 
User_Alias USER_FLAG = user1, user2, user3 
4) 配置Runas_Alias：就是用户以什么身份执行（例如root，或者oracle）的列表 
Runas_Alias RUNAS_FLAG = operator1, operator2, operator3 
5) 权限具体配置格式
USER_FLAG HOST_FLAG=(RUNAS_FLAG) NOPASSWD: COMMAND_FLAG 