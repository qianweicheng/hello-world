# Authentication
## PAM(Pluggable Authentication Modules)
[参考](./pam.md)
## 用户权限管理相关文件
- /etc/group
    格式:`group:pwd:gid:user1,user2`
- /etc/passwd
    格式:`username:pwd:uid:gid:commant:home:shell`
- /etc/shadow
    格式:`登录名:加密口令:最后一次修改时间:最小时间间隔:最大时间间隔:警告时间:不活动时间:失效时间:标志`
    - 加密口令: 
        - 空: 无密码 
        - `*`,`!`,`*LK*`: 锁定
        - `!!`: 锁定(在密码前加，或者空密码前加) or the password has never been set. 不同的系统有些差异
        - `$1`: MD5
        - `$2`: Blowfish
        - `$5$`: SHA256
        - `$6$`: SHA-512
    - 最后一次修改时间: 1970年1月1日起的天数
    - 最小时间间隔: 两次修改口令之间所需的最小天数,
    - 最大时间间隔: 同
    - 警告时间: 开始警告到最终过期的天数
    - 不活动时间: 表示的是用户没有登录活动但账号仍能保持有效的最大天数
    - 失效时间: 一个绝对的天数，如果使用了这个字段，那么就给出相应账号的生存期。期满后，该账号就不再是一个合法的账号
- /etc/sudoers
- /etc/pam.d/*(or /etc/pam.conf)
    程序一般在:`/lib/security/` or `/lib64/security`
## 用户/组管理
### 用户
- 添加: `useradd（adduser ->link to useradd）`
    Ex: useradd killwall -M -N -s /sbin/nologin -c "Only For Kill Wall"
    Ex: useradd normaluser -c "Common"
- 删除: `userdel`
- 修改: `usermod 改变用户所属组(usermod -a -G groupName userName)`
    - 将用户添加到组: `usermod -a -G groupA userA`
    - 将用户重置到组: `usermod -G groupA userA`
### 密码
- 添加密码:`passwd normaluser`
- 删除密码:`passwd -d` 无密码
- 锁定密码:`passwd -l` 静止密码登陆，可以使用ssh public key
- 解锁密码:`passwd -u`
- 查看: `passwd -S`
### 组
- 新建组: `groupadd`
- 删除组: `groupdel`
- 修改组: groupmod  (groupmod groupmod -g NEW-GID groupname)
- 查询: `groups [username]:查询所属group`
### Example
添加用户: `useradd stag -c "this is for stag cluster"`
添加组: `groupadd edison`
将用户添加到组: `usermod -a -G wheel devops`
## shell
- login shell
- nologin shell
- interactive shell:
- non-interactive shell
区别：
使用bash --login启动一个login shell或者通过echo $0的输出结果是否以-开头来判断一个shell是否为login shell
### su
不带`-`的情况下，会保留当前环境变量，并重新运行一次`~/.bashrc`
- `su - xxx` or `-l, --login`: 
  - run a login shell as target user
- `su [xxx]`: 
  - run a shell as target user.
### sudo
- `sudo [-u xxx] -s`: 
  - run a shell as target user. 同`sudo [-u xxx] /bin/bash`
  - 没有运行`~/.bash_profile`,只运行`~/.bashrc`
- `sudo -i`: 
  - run a login shell as target user
  - 运行了`~/.bash_profile`+`~/.bashrc`
> 印证了~/.bash_profile is for login shell
### 提权到root
- sudo系列 可以在/etc/sudoers配置
- sudo su
- sudo su -
- sudo -i
- sudo /bin/bash 
## sudoers
### root 环境变量设置
/etc/sudoers
Defaults  env_reset
Defaults  secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
### visudo
用`visudo`编辑`/etc/sudoers`可以让添加的用户有运行sudo的权限
1. 配置Host_Alias：就是主机的列表 
Host_Alias      HOST_FLAG = hostname1, hostname2, hostname3 
2. 配置Cmnd_Alias：就是允许执行的命令的列表，命令前加上!表示不能执行此命令. 
命令一定要使用绝对路径，避免其他目录的同名命令被执行，造成安全隐患 ,因此使用的时候也是使用绝对路径! 
Cmnd_Alias      COMMAND_FLAG = command1, command2, command3 ，!command4 
3. 配置User_Alias：就是具有sudo权限的用户的列表 
User_Alias USER_FLAG = user1, user2, user3 
4. 配置Runas_Alias：就是用户以什么身份执行（例如root，或者oracle）的列表 
Runas_Alias RUNAS_FLAG = operator1, operator2, operator3 
5. 权限具体配置格式
USER_FLAG HOST_FLAG=(RUNAS_FLAG) NOPASSWD: COMMAND_FLAG(注意这里必须是全路径)
省写1: USER_FLAG HOST_FLAG=NOPASSWD: COMMAND_FLAG
省写2: USER_FLAG HOST_FLAG=COMMAND_FLAG
### 例子
```
# User privilege specification
root ALL=(ALL) ALL
USER_OPS ALL=(ALL) NOPASSWD: ALL
# Members of the admin group may gain root privileges
%admin ALL=(ALL) ALL
```
上面 root 表示用户、%admin 表示 admin 用户组(%+名表示给用户组设置权限)
第一个ALL：标示登录者的主机名
第二个ALL（即括号内的）：指出规定的 user 用户能够以何种身份来执行命令。该ALL表示user用户能够以任何用户的身份执行命令
第三个ALL：表示能执行"命令表"，ALL表示用户能够执行系统中的所有命令。
## Authorization
受限的shell: `bash -r`
`ln -s bash rbash`