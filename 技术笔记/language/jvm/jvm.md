# JVM
垃圾回收方式（对象存活判断：引用计数vs引用追踪）
JVM内存分配（方法区，本地方法区/方法栈，栈帧，堆）
分代收集：Edan/Survivor(8:1:1), Old generation，永久代
JVM优化：常见的jvm 参数，-Xms -Xmx -Xss等
## 垃圾回收算法
1） 标记清除：容易产生碎片，很少用
2） 复制算法：一般用在新生带，Survivor，Eden * 2
3)  标记整理：一般老年代

## 垃圾收集器
1）Serial：复制算法，历史最悠久
2）ParNew收集器： #1的多线程版本
3）Parallel Scavenge: 复制算法，关注吞吐量而不是停顿时间，一般用在批量作业上，
4）Serial Old：标志整理
5）Parallel Old：#4的多线程版本，标志整理
6）CMS（Concurrent Mark Sweep): 标记清除。
    初始标记
    并发标记
    重新标记
    并发清除
7）G1
    初始标记
    并发标记
    最终标记
    率选回收

## 常见的收集器组合
Serial-CMS
Serial-Serial Old
ParNew-CMS
ParNew-Serial Old
Parallel Scavenge-Serial Old
Parallel Scavenge-Parallel Old
## 内存泄漏分析
- jconsole
- jvisualvm
- jmx