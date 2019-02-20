# Gateway
## 目前可用的最高版本（2018.11.16）
- Spring Boot 2.0.6.RELEASE 
- Spring Cloud Finchley.SR2
- Spring Gateway 2.0.2.RELEASE
## Filter
添加Filter有两种方式：
- 在router里面添加，只对该router起作用，名字是自动通过Class Name截取前一段
    ```
    spring:
    cloud:
        gateway:
            routes:
                filters:
                - name: RequestRateLimiter
                args:
                    redis-rate-limiter.replenishRate: 10
                    redis-rate-limiter.burstCapacity: 20
    ```

- 通过GlobalFilter定义
