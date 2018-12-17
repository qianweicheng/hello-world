#### 安装EPEL
http://mirrors.kernel.org/fedora-epel/
rpm -Uvh http://mirrors.kernel.org/fedora-epel/epel-release-latest-7.noarch.rpm
或者
sudo yum-config-manager --enable epel

#### Linux服务
service xxxxx start/stop/status
/etc/init.d/xxxx start

#### Linux信号
0   SIGT        ping
1   SIGHUP      挂起进程，当跟父PID脱离时，如关闭shell，常用于后台进程重启
2   SIGINT      终止进程, 一般Ctrl+C时发送，可忽略，同SIGTERM(15)，表示从键盘发送的
3   SIGOQUIT    同SIGINT(2), 它会生成内存转储，表示从键盘发送的
4   SIGILL      Illegal Instruction
5   SIGTRAP     用于Debug设置断点
6   SIGABRT     
7   SIGBUS      BUS error
8   SIGFPE      Floating point exception
9   SIGKILL     无条件终止进程
14  SIGALRM     Timer signal from alarm(2)
15  SIGTERM     尽可能终止进程（默认），友好告诉进程退出(给定时间)，进程先保存好数据，再退出。
17  SIGSTOP     无条件停止，但不终止，  Ctrl+Z.
18  SIGTSTP     同SIGSTOP(17)，但可忽略
19  SIGCONT     继续被SIGSTOP/SIGTSTP挂起的进程
20  SIGCHLD     子进程挂断
> 从16开始不同系统不太一样

#### 在Linux中，可能状态如下：
D    不可中断     Uninterruptible sleep (usually IO)
R    正在运行，或在队列中的进程
S    处于休眠状态
T    停止或被追踪
Z    僵尸进程
W    进入内存交换（从内核2.6开始无效）
X    死掉的进程
<    高优先级
N    低优先级
L    有些页被锁进内存
s    包含子进程
+    位于后台的进程组
l    多线程，克隆线程

#### 文件重定向
0 STDIN
1 STDOUT
2 STDERR
\>  重定向输出
&> 重定向所有输出
tee 是T型输出:既可以输出到stdout，同时又可以输出到文件
ex：date | tee [-a] out.log

#### Linux终端的类型有
- pty/pts  伪终端,成对的逻辑终端设备,如/dev/ptmx/dev/pts/x
- tty    控制终端, tty=tty0当前终端
- ttys   串行终端，（/dev/ttySn）
    echo test > /dev/ttyS1 会把单词”test”发送到连接在ttyS1（COM2）端口的设备上
- console控制台，相当于只读方式打开当前激活tty
#### Linux终端命令
- 查看当前终端：tty
- 查看当前登录终端：who
- 查看当前登录终端，并且展示他们正在做什么：w

#### Linux 进程 N:1 进程组 N:1 会话 1:1 控制终端
#### Linux配置加载(bashrc,profile, rcX.d, rc, rc.local)
[参考](https://www.jianshu.com/p/020f3d02f538)
 顺序：/etc/rc.sysinit（通过分析/etc/inittab文件来确定系统的启动级别，然后才去执行/etc/rc.d/rc*.d下的文件）->rc->rc.d(->init.d)->S99local(->rc.local)

bashrc为交互式non-login，一般图形系统启动的shell和shell内部启动的shell
profile为交互式login shell，一般为远程登录启动的shell
Linux加载环境变量顺序
/etc/profile
    /etc/profile.d等待配置文件
/etc/paths
    /etc/paths.d
    
    $HOME/.bash_profile
    $HOME/.bash_login
    $HOME/.profile
        ~/.bashrc
            /etc/bashrc

#### 脚本目录