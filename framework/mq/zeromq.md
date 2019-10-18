# ZeroMQ
## 0MQ提供了4种不同的传输协议
- INPROC: an In-Process communication model
- IPC: an Inter-Process communication model
- MULTICAST: multicast via PGM, possibly encapsulated in UDP
- TCP: a network based transport
## 0MQ提供了3种类型的设备
- QUEUE: a forwarder for the request/response messaging pattern
- FORWARDER: a forwarder for the publish/subscribe messaging pattern
- STREAMER: a forwarder for the pipelined messaging pattern
## 0MQ支持4种模式
- REQUEST/REPLY: bidirectional, load balanced and state based
- PUBLISH/SUBSCRIBE: publish to multiple recipients at once
- UPSTREAM/DOWNSTREAM: distribute data to nodes arranged in a pipeline
- PAIR: communication exclusively between peers
## Demo
- Request-Reply模式，类似常见的web服务器
  ```
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")
    while True:
        message = socket.recv()
        print("Received: %s" % message)
        socket.send("I am OK!")
  ```
- Publish-Subscribe模式: 广播所有client，没有队列缓存，断开连接数据将永远丢失。client可以进行数据过滤。


    ```
        import zmq
        import time

        context = zmq.Context()
        socket = context.socket(zmq.PUB)
        socket.bind("tcp://*:5555")

        while True:
            print('发送消息')
            socket.send("消息群发")
            time.sleep(1)    
    ```
- Parallel Pipeline模式：push进行数据推送，work进行数据缓存，pull进行数据竞争获取处理。区别于Publish-Subscribe存在一个数据缓存和处理负载, 当连接被断开，数据不会丢失，重连后数据继续发送到对端
