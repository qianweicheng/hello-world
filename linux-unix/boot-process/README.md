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
  由于使用mosh，会导致先运行一个nonlogin shell, 结果导致先运行一遍`~/.bashrc`,然后启动一个login shell，又从`~/.bash_profile`重新运行以便，导致变量赋值两次
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

## 交互式登陆shell
对于交互式的登陆shell而言，CentOS规定了startup文件的加载顺序如下：
- 登陆过程：
1. 读取并执行/etc/profile文件；
2. 读取并执行~/.bash_profile文件；
   - 若文件不存在，则读取并执行~/.bash_login文件；
   - 若文件不存在，则读取并执行~/.profile文件；
- 登出过程：
1. 读取并执行~/.bash_logout文件；
2. 读取并执行/etc/bash.bash_logout文件；
## 非交互式登陆shell
对于非交互式的登陆shell而言，CentOS规定了startup文件的加载顺序如下：
登陆过程：
1. 读取并执行/etc/profile文件；
2. 读取并执行~/.bash_profile文件；
   - 若文件不存在，则读取并执行~/.bash_login文件；
   - 若文件不存在，则读取并执行~/.profile文件；
3. (注意没有登出过程)

## 交互式非登陆shell
对于交互式的非登陆shell而言，CentOS规定了startup文件的加载顺序如下：
1. 读取并执行~/.bashrc或--rcfile选项指定的文件
这里需要说明，其实“rc”系列startup文件还包括/etc/bashrc。但是系统并不直接调用这个文件，而是通过~/.bashrc文件显式地调用它。
