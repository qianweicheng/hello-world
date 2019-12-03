# 内存/CPU分析
## /proc
http://man7.org/linux/man-pages/man5/proc.5.html
https://www.kernel.org/doc/Documentation/cgroup-v1/memory.txt
- {pid}/status: 内存等各种状态
- {pid}/stat: 
  - 所有CPU活跃的信息，该文件中的所有值都是从系统启动开始累计到当前时刻
  - `https://blog.csdn.net/cybertan/article/details/7596633`
  - `https://www.jianshu.com/p/9fae17dc5f93` or 
  - `https://blog.csdn.net/houzhizhen/article/details/79474427`
- meminfo
- vmstat
- cpuinfo
- /sys/fs/cgroup/memory 当前命名空间的内存信息, docker的内存在这里查看
## 工具
- top： 读取 /proc/{pid}/status + /proc/meminfo
    https://github.com/moby/moby/issues/10824    
- free： 读取/proc/meminfo
## meminfo
```
%MEM is directly related to RES, it’s the percentage use of total physical memory by the process.
VIRT is the total memory that this process has access to shared memory, mapped pages, swapped out pages, etc.
RES is the total physical memory used shared or private that the process has access to.
SHR is the total physical shared memory that the process has access to.
DATA is the total private memory mapped to process physical or not.
CODE also known as “text resident set” is total physical memory used to load application code
```
## /proc/
- 内存参数:{pid}/status
字段 | 说明
-|-
VmPeak | 进程所使用的虚拟内存的峰值
VmSize | 进程当前使用的虚拟内存的大小
VmLck | 已经锁住的物理内存的大小（锁住的物理内存不能交换到硬盘）
VmHWM | 进程所使用的物理内存的峰值
VmRSS | 进程当前使用的物理内存的大小
VmData | 进程占用的数据段大小
VmStk | 进程占用的栈大小
VmExe | 进程占用的代码段大小（不包括库）
VmLib | 进程所加载的动态库所占用的内存大小（可能与其它进程共享）
VmPTE | 进程占用的页表大小（交换表项数量）
VmSwap | 进程所使用的交换区的大小

- `/proc/meminfo`, `free -h`, `top`, `vmstat`
- 64位系统的虚拟地址空间划分: 一般是2^48。因为并不需要 2^64 这么大的寻址空间，过大空间只会导致资源的浪费。64位Linux一般使用48位来表示虚拟地址空间，40位表示物理地址，这可通过 /proc/cpuinfo 来查看`address sizes   : 40 bits physical, 48 bits virtual`
  - 共提供 256TB(2^48) 的寻址空间
    - `0x0000000000000000~0x00007fffffffffff` 表示用户空间
    - `0xFFFF800000000000~ 0xFFFFFFFFFFFFFFFF` 表示内核空间
## JVM Debug
- arthas阿里出品: 
  - https://alibaba.github.io/arthas/
- jconsole
- mat等
## docker 
文件存储：/var/lib/docker/containers/
/sys/fs/cgroup/memory/docker/<longid>/.
- docker stats：不包括cache
- k8s dashboard 包括了cache
- /sys/fs/cgroup/memory/memory.stat
- 查看tpc连接:`netstat -ant|awk '/^tcp/ {++S[$NF]} END {for(a in S) print (a,S[a])}'`
- K8S:cAdvisor 废弃了