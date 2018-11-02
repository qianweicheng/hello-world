#sleuth
```
    <dependency> 
        <groupid>org.springframework.cloud</groupid>   <artifactid>spring-cloud-starter-sleuth</artifactid>
    </dependency>
```
##坑
如果引入了消息队列的话，则会直接使用该消息队列进行存储，可以显式的指定存储类型。