#Feign
pom依赖
```
    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-openfeign</artifactId>
    </dependency>
```
##底层封装了Hystrix和Ribbon
>对Ribbon的依赖比较少，只是使用了其负载均衡器
##Fallback
- @EnableCircuitBreaker+@HystrixCommand(fallbackMethod) 基于原始API，使用restTemplate
- FeignClient(fallback)
- FeignClient(fallbackFactory) 同#1，可以获取异常信息
##FeignRibbonClientAutoConfiguration默认使用JDK的HttpURLConnection
##配置
feign.client
feign.httpclient
##默认不开启Hystrix：feign.hystrix.enabled=true. 依赖库
- io.github.openfeign.feign-hystrix
- io.github.openfeign.feign-core(真正的发送网络请求在：Client execute)
##调用栈
- 启动的时候HystrixTargeter & DefaultTargeter 将被调用的接口动态生成一个可调用类
- ReflectiveFeign.invoke
- SynchronousMethodHandler->invoke
- executeAndDecode
- LoadBalancerFeignClient->execute 获取某个API的FeignLoadBalancer对象执行executeWithLoadBalancer
    > 这里就开始用RxJava做异步调用了
- 。。。
- LoadBalancerCommand.call
- loadBalancerContext
    - ILoadBalancer.chooseServer 根据IRule选择合适的server 