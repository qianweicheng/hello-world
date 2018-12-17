# Config 
## 基础pom依赖
- 服务器
    ```
    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-config-server</artifactId>
    </dependency>
    ```
- 客户端
    ```
    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-config</artifactId>
    </dependency>
    ```
## 如需要支持动态刷新
- server和client添加消息队列组件，支持: rabbitMQ（默认），Kafka
    ```
    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-bus-amqp</artifactId>
        <!--Kafka版本-->
        <!--<artifactId>spring-cloud-starter-bus-kafka</artifactId>-->
    </dependency>
    ```
    
- 客户端需要刷新的地方添加：@RefreshScope（ RefreshScope 的缓存和延迟加载机制，生成了新的对象）
    或者@ConfigurationProperties（在同一个对象中重新绑定了所有属性,本地配置文件）
```
    @RefreshScope
    public class MyController {
        @Value("${name}")
        private String name;
        @Value("${age}")
        private String age;
    }
```
## 当config server 检测到config 变动，则POST /actuator/bus-refresh触发事件，会通过Event Bus推送到各个config client，config。一般通过配置webhook等自动触发
## 各种Environment配置
xxxEnvironmentProperties 通过@ConfigurationProperties(spring.cloud.config.server)读取
xxxEnvironmentRepository 返回一个Environment(详细的配置信息)
xxxEnvironmentRepositoryFactory 返回一个xxxEnvironmentRepository
真正选择哪个Repository在EnvironmentRepositoryConfiguration里面
## gitRepository是先下载到本地，然后通过NativeEnvironmentRepository服务
## EnvironmentController是其它应用获取config的入口
### 获取流程
- labelledProperties
- labelled
- findOne