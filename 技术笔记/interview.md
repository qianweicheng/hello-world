#Java
    接口和抽象类的区别（多继承，成员变量的类型，静态方法，业务上）
# JVM 相关
    垃圾回收方式（对象存活判断：引用计数vs引用追踪）
    JVM内存分配（方法区，本地方法区/方法栈，栈帧，堆）
    垃圾回收策略：标记清除，复制清除，标记压缩，分代收集
        分代收集：Edan/Survivor(8:1:1), Old generation，永久代
    垃圾回收器：Serial，ParNew，Parallel，CMS(Concurrent Mark Sweep),G1
    JVM优化：常见的jvm 参数，-Xms -Xmx -Xss等
    内存泄漏分析:jconsole和jvisualvm
#数据结构
    HashSet 优化
    跳表，链表，hash表，树(B Tree), ConcurrentHashMap
    链表反转，最大子序列，N个数里面最大K个数
# 多线程
    线程池
    线程模型，轻量级线程（纤程go routing）
    线程可重入，CAS，ABA
    线程安全的计数器（多版本）
    1）线程安全的操作链表，各种优化
    2）线程安全的计数器
    1）在web页面实现一个页面访问计数器
# WEB技术
    http协议：常用方法，GET/POST区别， 缓存机制（ETAG，Last-Modified-Since),状态码（300，400，401）
    html: 
        form的enctype
            application/x-www-form-urlencoded	默认。在发送前对所有字符进行编码（将空格转换为 "+" 符号，特殊字符转换为 ASCII HEX 值）。
            text/plain	类似#1，较少使用。将空格转换为 "+" 符号，但不编码特殊字符。
            multipart/form-data	不对字符编码。当使用有文件上传控件的表单时，该值是必需的。
    spring
        AOP方面,Dependency Injection
        springboot vs spring
        spring bean的生命周期，spring支持的几种bean的作用域。
    一个请求的生命周期
        Client->DispatchServlet->HandlerMapping->Handler(filter，intecepter)->Controller->ViewResolver->jsp/Template->Client
    异步方面
# 数据库方面
    user表有百万数量级的数据，username字段建立索引
    这条SQL语句有几个问题：select * from user where username = '% ming'
        a) 语法问题，必须使用like
        b) 左边模糊查询导致全表扫描
        c) select * 效率低
    
    char(N) vs varchar(N)：存储硬盘没有差别，在内存中有差异
    索引优化，普通索引、唯一索引、主键索引、全文索引。 哪种情况下不需要索引
    乐观锁，悲观锁，各种使用场景
    事务
    数据库各个引擎的差异：MyISAM（简单，效率高，支持全文索引）、InnoDB区别（默认，支持事务，行锁等复杂场景），
    数据库范式
# Mongodb相关
    集群方面
    skip，limit
    是否支持事务？（否）
    自增id
# Redis
    支持哪些数据类型？vs memorycache
        (1) memcached所有的值均是简单的字符串，redis作为其替代者，支持更为丰富的数据类型
        (2) redis的速度比memcached快很多
        (3) redis可以持久化其数据
    集群方面，原子操作
    自增id
    AOF vs snapshots
    Jedis库熟悉度
# 消息队列
    kafka topic，partion，replicas，为啥不保证顺序
    RabitMQ/RocketMQ等
# Devops相关
    K8S相关
    Docker相关
    ELK/EFK：elasticsearch 查寻API
    shell/python
    灰度发布,版本控制
    监控（Prometheus/Nagios,Canglia)

#系统架构
    zookeeper工作原理
    微服务
#实战
    探讨“秒杀”功能的实现

