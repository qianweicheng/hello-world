#Aysnc Program
##Reactor
Reactor 框架主要有两个主要的模块：reactor-core 和 reactor-ipc。前者主要负责 Reactive Programming 相关的核心 API 的实现，后者负责高性能网络通信的实现，目前是基于 Netty 实现的
####Reactive Streams定义的API主要的接口有这三个：
- Publisher:发布者是有序元素的提供者，根据从其订阅者收到的需求发布它们
- Subscriber:在将订阅者实例传递给Publisher.subscribe（订阅者）之后
- Subcription:订阅表示订阅发布者的订阅者的一对一生命周期。
- Processor:处理器代表一个处理阶段 - 既是订阅者又是发布者，并遵守两者的合同。
####常用类
- Mono 实现了 org.reactivestreams.Publisher 接口，代表0到1个元素的发布者。
- Flux 同样实现了 org.reactivestreams.Publisher 接口，代表0到N个元素的发表者。
##Java Web编程模型
- Servlet. SpringMVC与Struts2
- Webflux:基于Reactor模型
- Vert.x
##Linux 网络I/O模型5种模型
- 阻塞，最简单常用。在进程空间中调用recvfrom,其系统调用直到数据包到达并且复制到用户进程或者发生错误才返回
- 非阻塞。recvfrom从应用层到内核的时候，如果缓冲区没有数据，就直接返回，如果有则复制到用户进程（还是有阻塞）。主要用来轮询。
- I/O复用。 select/epoll, 阻塞到select，监听多个FD，后面流程跟阻塞模型一样。
- 信号驱动I/O模型。类似I/O复用，不同的是不阻塞，只响应信号
- 异步I/O。告知内核启动某个操作，并让内核在完整操作完成后，包括数据从内核复制到用户自己的缓冲区，然后通知我们。
##Netty
####主要类
- Java:Socket接口和ServerSocket
- Netty:SocketChannel和ServerSocketChannel->Channel
>都提供阻塞和非阻塞模式
####流Channel

