# Concurrency
线程安全两个方面:
- 可见性
- 原子性
## 内存模型
#### 重排序(Happens-Before)
- 程序顺序规则: 如果程序中操作A在操作B之前，那么在线程中A操作将在B操作之前执行
- 监视器锁规则: 在监视器锁上的解锁操作必须在同一个监视器锁上的加锁操作之前执行。
- volatile变量规则: 对volatile变量的写入操作必须在对改变量的读操作之前执行
- 线程启动规则: 在线程上对Thread.Start的调用必须在该线程中执行任何操作之前执行
- 线程结束规则: 
- 中断规则: 当一个线程在另一个线程上调用interrupt时，必须在被中断线程检测到interrupt调用之前执行
- 终结器规则: 对象的构造函数必须在启动该对象的终结器之前执行完成。
- 传递性: 如果A<B,B<C, 那么A<C
## 锁
- volatile
- 内置锁(synchronized)
- ReentrantLock
    ```
    ReadWriteLock lock = new ReentrantReadWriteLock();
    Lock r = lock.readLock();
    Lock w = lock.writeLock();
    r.lock();
    try {
        //do something
    } finally {
        r.unlock();
    }
    ```
    公平性:
    - 公平策略
    - 非公平策略
## 线程池
- newFixedThreadPool
- newCachedThreadPool
- newSingleThreadExecutor
- newScheduledThreadPool

#### 饱和策略
- AbortPolicy(默认)
- CallerRunsPolicy
- DiscardPolicy
- DiscardOldestPolicy
## 条件队列
wait
notify/notifyAll
## 同步工具类
- CountDownLatch
- CyclicBarrier
- Semaphore
- AtomicLong/AtomicReference
- ConcurrencyHashMap
- ConcurrentSkipListMap
- CopyOnWriteArrayList
- LinkedBlockingQueue
- ArayBlockingQueue
- ReentrantReadWriteLock
- ReentrantLock(广义的内置条件队列)
    ```
        Lock lock = new ReentrantLock();
        Condition notFull = lock.newCondition();
        Condition notEmpty = lock.newCondition();
    ```
## 自定义同步工具
AQS
CAS
ABA
## 双重检查加锁
- 加上volatile之后，逻辑上没有问题
- 但双重锁存在的基础以及不存在了: 无竞争同步的执行速度很慢，JVM启动时很慢