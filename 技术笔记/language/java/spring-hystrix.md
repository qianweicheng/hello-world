#Hystrix[Wiki](https://github.com/Netflix/Hystrix/wiki)
源代码放在spring-cloud-netflix-core:2.0.1下面
##开启: @EnableCircuitBreaker
##Feign.Hystrix
##Zuul.Hystrix
##HystrixCommand或者HystrixObservableCommand
- execute()：调用后直接block住，属于同步调用，直到依赖服务返回单条结果，或者抛出异常
- queue()：返回一个Future，属于异步调用，后面可以通过Future获取单条结果
- observe()：订阅一个Observable对象，Observable代表的是依赖服务返回的结果，获取到一个那个代表结果的 Observable对象的拷贝对象
- toObservable()：返回一个Observable对象，如果我们订阅这个对象，就会执行command并且获取返回结果
##配置：hystrix.command.default
execution.isolation.strategy
execution.isolation.thread.timeoutInMilliseconds
execution.timeout.enabled
execution.isolation.thread.interruptOnTimeout
execution.isolation.thread.interruptOnCancel
execution.isolation.semaphore.maxConcurrentRequests
fallback.enabled
fallback.isolation.semaphore.maxConcurrentRequests
circuitBreaker.enabled
circuitBreaker.requestVolumeThreshold
circuitBreaker.sleepWindowInMilliseconds
circuitBreaker.errorThresholdPercentage
circuitBreaker.forceOpen
circuitBreaker.forceClosed
requestCache.enabled
requestLog.enabled
maxRequestsInBatch
timerDelayInMilliseconds
requestCache.enabled
coreSize
maximumSize
maxQueueSize
queueSizeRejectionThreshold
keepAliveTimeMinutes
allowMaximumSizeToDivergeFromCoreSize
metrics.rollingStats.timeInMilliseconds
metrics.rollingStats.numBuckets
##CommandGroup & CommandKey
CommandGroup:在不指定ThreadPoolKey的情况下，字面值用于对不同依赖的线程池/信号区分，也就是在不指定ThreadPoolKey的情况下,CommandGroup用于指定线程池的隔离。命令分组用于对依赖操作分组，便于统计、汇总等。
CommandKey:一般来说每个CommandKey代表一个依赖抽象，相同的依赖要使用相同的CommandKey名称。依赖隔离的根本就是对相同CommandKey的依赖做隔离。不同的依赖隔离最好使用不同的线程池（定义不同的ThreadPoolKey）。从HystrixCommand源码的注释也可以看到CommandKey也用于对依赖操作统计、汇总等。
ThreadPoolKey: ThreadPoolKey简单来说就是依赖隔离使用的线程池的键值。当对同一业务依赖做隔离时使用CommandGroup做区分，但是对同一依赖的不同远程调用如(一个是redis 一个是http)，可以使用HystrixThreadPoolKey做隔离区分。 虽然在业务上都是相同的组，但是需要在资源上做隔离时，可以使用HystrixThreadPoolKey区分。（对于每个不同的HystrixThreadPoolKey建议使用不同的CommandKey）















