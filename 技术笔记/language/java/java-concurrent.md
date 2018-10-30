## Java 并发编程
* AtomicXXXX
* Lock: ReentrantLock,ReadWriteLock
* BlockingQueue/Deque 
* Runnable, Callable, Future
- ConcurrentXXXX
    * ConcurrentHashMap,HashSet,LinkedQueue,LinkedDeque, CopyOnWriteXXX
- 同步工具类
    * CountDownLatch（闭锁，一次性）
    * FutureTask： Runnabe,Future<-RunnabeFuture<-FutureTask
    * Semaphore: 计数信号量，主要用于控制同时并发某个特定资源
    * CyclicBarrier: new CyclicBarrier(N, new Runnable()), x.await() N 次
    * Exchanger:（栅栏,可多次使用）
- LinkedBlockingXXX


