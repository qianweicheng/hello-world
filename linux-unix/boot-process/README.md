# boot process
## Linux加载环境变量顺序
### Mac OS
- unknown:
    /etc/paths
        /etc/paths.d
- unknown:
    /etc/profile
        /etc/bashrc
- unknown:
    $HOME/.bash_profile
### Centos
- 初始化:
    /usr/local/bin:
    /bin:
    /usr/bin:
    /usr/local/sbin:
    /usr/sbin:
    /sbin:
-  一般流程
  ```
    /etc/profile ->/etc/profile.d
    (~/.bash_profile | ~/.bash_login | ~/.profile) 
    ~/.bashrc
    /etc/bashrc (non-login模式会调用/etc/profile.d)
    ~/.bash_logout
  ```
- 使用mosh的问题
  由于使用mosh，会导致先运行一个nonlogin shell, 结果导致先运行一便`~/.bashrc`,然后启动一个login shell，又从`~/.bash_profile`重新运行以便，导致变量赋值两次
### Ubuntu
- unknown:
    /etc/environment
    /etc/profile
        /etc/bash.bashrc
        /etc/profile.d/
- unknown:
    ~/.bashrc
        ~/.bash_aliases
## 启动服务
/etc/init.d 和 /etc/rc.x 都是链接到/etc/rc.d/里面去
/etc/rc.d
    rc.local 废弃
    init.d  兼容模式，存放老的/etc/init.d
    rc.x 
/etc/systemd 真正放服务的地方