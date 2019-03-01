# JVM
垃圾回收方式（对象存活判断：引用计数vs引用追踪）
JVM内存分配（方法区，本地方法区/方法栈，栈帧，堆）
分代收集：Edan/Survivor(8:1:1), Old generation，永久代
JVM优化：常见的jvm 参数，-Xms -Xmx -Xss等
## 可达性分析
在Java语言中，可作为GC Roots的对象包含以下几种：
- 虚拟机栈(栈帧中的本地变量表)中引用的对象。(可以理解为:引用栈帧中的本地变量表的所有对象)
- 方法区中静态属性引用的对象(可以理解为:引用方法区该静态属性的所有对象)
- 方法区中常量引用的对象(可以理解为:引用方法区中常量的所有对象)
- 本地方法栈中(Native方法)引用的对象(可以理解为:引用Native方法的所有对象)

## 垃圾回收算法
- 标记清除：容易产生碎片，很少用
- 复制算法：一般用在新生带，Survivor，Eden * 2
- 标记整理：一般老年代
## 垃圾收集器
1. Serial：复制算法，历史最悠久
    - 单线程扫描年前代所有存活对象
    - 使用Minor GC进行垃圾回收，同时将存活对象保存到S0或者S1区
2. ParNew收集器： #1的多线程版本
    +UseParallelGC
3. Parallel Scavenge: 复制算法，关注吞吐量而不是停顿时间，一般用在批量作业上，必须配合CMS使用
4. Serial Old：标志整理
5. Parallel Old：#4的多线程版本，标志整理
6. CMS（Concurrent Mark Sweep): 标记清除
    `-XX:+CMSClassUnloadingEnabled`
7. G1
    `-XX:+UseG1GC`
## CMS
CMS 收集器是获取最短回收停顿时间为目标的收集器
#### 常用参数
启用: -XX:+UseConcMarkSweepGC
参数: -XX:ParallelCMSThreads=20
老年代回收阀值: -XX:CMSInitiatingOccupancyFraction=80
#### 过程
- 初始标记(STW): 速度很快
- 并发标记
- 重新标记(STW)
- 并发清除
#### 优点
并发，低停顿
#### 缺点
1. 对CPU非常敏感：在并发阶段虽然不会导致用户线程停顿，但是会因为占用了一部分线程使应用程序变慢. CMS 默认启动的线程是(CPU数量+3)/4,当 CPU 大于4个以上占用资源不超过 25% 的 CPU 资源,但是小于 4 个 CPU 时候 CMS 收集器对用户程序的影响就比较大
2. 无法处理浮动垃圾：在最后一步并发清理过程中，用户县城执行也会产生垃圾，但是这部分垃圾是在标记之后，所以只有等到下一次gc的时候清理掉，这部分垃圾叫浮动垃圾. 所有不能等到老年代满了再进行回收，默认68%就启动回收了，可以通过 -XX:CMSInitiatingOccupancyFraction 参数来设置这个属性。如果 CMS 在运行时候预留的内存无法满足程序需要,就会出现一次“Concurrent Mode Failure”失败,这时候虚拟机临时启用 Serial Old 收集器重新来进行老年代的垃圾收集。 
3. CMS使用“标记-清理”法会产生大量的空间碎片，当碎片过多，将会给大对象空间的分配带来很大的麻烦，往往会出现老年代还有很大的空间但无法找到足够大的连续空间来分配当前对象，不得不提前触发一次FullGC，为了解决这个问题CMS提供了一个开关参数，用于在CMS顶不住，要进行FullGC时开启内存碎片的合并整理过程，但是内存整理的过程是无法并发的，空间碎片没有了但是停顿时间变长了。 还提供了一个参数 -XX:CMSFullGCsBeforeCompaction,这个参数设置在执行多少次不压缩的 Full GC 后,跟着来一次带压缩的。 
## G1
如果你的堆内存大于4G的话，那么G1会是要考虑使用的收集器。它是为了更好支持大于4G堆内存在JDK 7 u4引入的。G1收集器把堆分成多个区域，大小从1MB到32MB，并使用多个后台线程来扫描这些区域，优先会扫描最多垃圾的区域，这就是它名称的由来，垃圾优先Garbage First
#### 过程
- 初始标记
- 并发标记
- 最终标记
- 筛选回收
#### 特点
- 并行并发
    G1能充分利用CPU、多核环境下的硬件优势，使用多个CPU（CPU或者CPU核心）来缩短stop-The-World停顿时间。部分其他收集器原本需要停顿Java线程执行的GC动作，G1收集器仍然可以通过并发的方式让java程序继续执行。
- 分代收集
    虽然G1可以不需要其他收集器配合就能独立管理整个GC堆，但是还是保留了分代的概念。它能够采用不同的方式去处理新创建的对象和已经存活了一段时间，熬过多次GC的旧对象以获取更好的收集效果
- 空间整合
    由于G1使用了独立区域（Region）概念，G1从整体来看是基于“标记-整理”算法实现收集，从局部（两个Region）上来看是基于“复制”算法实现的，但无论如何，这两种算法都意味着G1运作期间不会产生内存空间碎片。虽然还保留了新生代和来年代的概念，但新生代和老年代不再是物理隔离的了它们都是一部分Region（不需要连续）的集合。同时，为了避免全堆扫描，G1使用了Remembered Set来管理相关的对象引用信息。当进行内存回收时，在GC根节点的枚举范围中加入Remembered Set即可保证不对全堆扫描也不会有遗漏了。
- 可预测的停顿
    这是G1相对于CMS的另一大优势，降低停顿时间是G1和CMS共同的关注点，但G1除了追求低停顿外，还能建立可预测的停顿时间模型，能让使用这明确指定一个长度为M毫秒的时间片段内，消耗在垃圾收集上的时间不得超过N毫秒
## 常见的收集器组合
- Serial-CMS+Paralle Old
- Serial-Serial Old
- ParNew-CMS+Paralle Old
- ParNew-Serial Old
- Parallel Scavenge-Serial Old
- Parallel Scavenge-Parallel Old
- G1
## Metaspace vs PermGen
Java 8最大的改变之一是去掉了永久代PermGen。永久代需要开发者仔细调节它的大小，过去多年这是产生OutOfMemory异常的重要原因。现在JVM可以自己管理这块区域了
方法区: JVM 规范
PermGen Spece: JVM的一种实现
Metaspace: 元空间并不在虚拟机中，而是使用本地内存
## Hotspot
## 优化
- 响应时间
- 吞吐量
## 内存泄漏分析
- jconsole
- jvisualvm
- jmx
## 参考
- https://www.oracle.com/technetwork/tutorials/tutorials-1876574.html