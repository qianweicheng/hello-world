## Linux终端
## 终端
对应关系：Linux 进程 N:1 进程组 N:1 会话 1:1 控制终端
tmux就是基于一个终端对应N个会话
终端的类型：
- pty/pts  伪终端,成对的逻辑终端设备,如/dev/ptmx /dev/pts/x
- tty    控制终端, tty=tty0当前终端
- ttys   串行终端，（/dev/ttySn）
    echo test > /dev/ttyS1 会把单词”test”发送到连接在ttyS1（COM2）端口的设备上
- console控制台，相当于只读方式打开当前激活tty
## 文件
终端: /dev/tty
伪终端: /dev/[pts|pty]
- 向自己发送信息: `echo xxx > /dev/tty`
- 向另外一个终端发送: `echo xxx > /dev/pts/x`
当前tty设备:/dev/tty
当前终端设备文件的别名: /dev/tty0
/dev/console: 是个只输出的设备，功能很简单，只能在内核中访问；tty是char设备，可以被用户程序访问。
## Linux配置加载(bashrc,profile, rcX.d, rc, rc.local)
[参考](https://www.jianshu.com/p/020f3d02f538)
 顺序：/etc/rc.sysinit（通过分析/etc/inittab文件来确定系统的启动级别，然后才去执行/etc/rc.d/rc*.d下的文件）->rc->rc.d(->init.d)->S99local(->rc.local)
- bashrc为交互式non-login，一般图形系统启动的shell和shell内部启动的shell
- profile为交互式login shell，一般为远程登录启动的shell
#### 终端命令
- 查看当前终端: `tty`
- 查看当前登录终端: (/var/run/utmp) `who`, `w`(详细), `users`
- 查看历史登陆记录: last (/var/log/wtmp)
- 查看历史登陆失败记录: `lastb` (/var/log/btmp)
- SSH日记: `tail -f /var/log/secure`
- 修改终端设置:`stty`
