# Linux
## 发布版本
- Redhat: 收费。黄金标准的企业发行版。它每五年左右更新一次，在系统的稳定性，前瞻性和安全性上有着极大的优势
- CentOS: 从Redhat衍生，免费。命令行下的人性化做得比较好，稳定，有着强大的英文文档与开发社区的支持
- Debian: 
  - 相对稳定，是没有真正意义的 release 概念的。
  - 更多自主可控。计划组织跟其他自由操作系统(如 Ubuntu、openSUSE、Fedora、Mandriva、OpenSolaris 等)的开发组织不同。 上述这些自由操作系统的开发组织通常背后由公司或机构支持。Debian组织则完全是一个独立的、分散的开发者组织，纯粹由志愿者组成， 背后没有任何公司或机构支持。
  - 目前版本主要有: 
    - Next Release: bullseye
    - Debian 10 (buster) — current stable release
    - Debian 9 (stretch) — oldstable release
    - Debian 8 (jessie) — oldoldstable release
    - Debian 7 (wheezy) — obsolete stable release
    - Debian 6.0 (squeeze) — obsolete stable release
- Ubuntu: 从Debian衍生，UI特长。完善的包管理系统，强大的软件源支持，丰富的技术社区. 主要版本:
  - xenial (16.04LTS)
  - bionic (18.04LTS)
  - cosmic (18.10)
  - disco (19.04)
  - disco-updates
  - disco-backports
  - eoan

## Linux信号
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

## 进程状态如下：
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

## 文件重定向
```
0 STDIN
1 STDOUT
2 STDERR
>  重定向输出
&> 重定向所有输出
>& 重定向所有输入
tee 是T型输出:既可以输出到stdout，同时又可以输出到文件
ex：date | tee [-a] out.log
```
## 管道
1. pipe匿名管道
    主要用于父进程与子进程之间，或者两个兄弟进程之间
2. named pipe(FIFO)有名管道: `mkfifo /tmp/k.pipe`
    命名管道是为了解决无名管道只能用于近亲进程之间通信的缺陷而设计的。命名管道是建立在实际的磁盘介质或文件系统（而不是只存在于内存中）上有自己名字的文件
## LANG问题:locale
1）对于CentOS，可以直接编辑/etc/sysconfig/i18n文件，将LANG="en_US.UTF-8"设置成LANG="zh_CN.UTF-8"
localedef -i en_US -f UTF-8 en_US.UTF-8
## Etc
`source`效果等同`.`
nohub xxx &
