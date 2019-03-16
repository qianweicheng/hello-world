#### 搭建环境
- brew install springboot
- spring install spring-cloud-cli:2.0.0.RELEASE
#### 快捷启动开发环境
`spring cloud`
#### 依赖
spring-cloud-starter
- spring-boot-starter
- spring-cloud-context
- spring-cloud-commons
- spring-security-rsa
spring-cloud-dependencies
- spring-cloud-commons-dependencies
- spring-cloud-netflix-dependencies
- spring-cloud-stream-dependencies
- spring-cloud-task-dependencies
- spring-cloud-config-dependencies
- spring-cloud-consul-dependencies
- spring-cloud-sleuth-dependencies
- spring-cloud-zookeeper-dependencies
- spring-cloud-security-dependencies
- spring-cloud-cloudfoundry-dependencies
- spring-cloud-bus-dependencies
- spring-cloud-contract-dependencies
- spring-cloud-aws-dependencies
spring-cloud-netflix
- spring-cloud-netflix-hystrix-contract
- spring-cloud-netflix-dependencies
- spring-cloud-commons-dependencies
- spring-cloud-test-support
- spring-cloud-config-dependencies
- spring-cloud-stream-dependencies
- spring-cloud-contract-dependencies

spring-cloud-starter-netflix
- spring-cloud-starter
- spring-cloud-netflix-core
- spring-cloud-netflix-eureka-client
- eureka-client
- spring-cloud-starter-netflix-archaius
- spring-cloud-starter-netflix-ribbon
spring-cloud-starter-netflix-eureka-client(一般使用spring-cloud-starter-eureka)
- spring-cloud-starter
- spring-cloud-netflix-core
- spring-cloud-netflix-eureka-client
- eureka-client
- eureka-core

spring-cloud-starter-netflix-eureka-server(一般使用spring-cloud-starter-eureka-server)
- spring-cloud-starter
- spring-cloud-netflix-eureka-server
- spring-cloud-starter-netflix-archaius
- spring-cloud-starter-netflix-ribbon
- ribbon-eureka

spring-cloud-starter-eureka
- spring-cloud-starter-netflix-eureka-client
- spring-boot-autoconfigure-processor
spring-cloud-starter-eureka-server
- spring-cloud-starter-netflix-eureka-server
- spring-boot-autoconfigure-processor
spring-cloud-config
- spring-cloud-config-dependencies
- spring-cloud-commons-dependencies
- spring-cloud-test-support
spring-cloud-config-client
- spring-boot-configuration-processor
- spring-cloud-commons
- spring-cloud-context
spring-cloud-config-dependencies
- spring-cloud-starter-config
- spring-cloud-config-client
- spring-cloud-config-server
- spring-cloud-config-monitor
spring-cloud-config-server
- spring-boot-configuration-processor
- spring-boot-starter-jdbc
- spring-cloud-config-client
- spring-boot-starter-web
spring-cloud-netflix-ribbon
- spring-boot-starter-web
- spring-boot-autoconfigure
- spring-cloud-commons
- spring-cloud-context
- spring-cloud-netflix-archaius
- com.netflix.ribbon.xxx
spring-boot-starter-web
- spring-boot-starter
- spring-boot-starter-tomcat
- spring-boot-starter-validation
- jackson-databind
- spring-web
- spring-webmvc
spring-cloud-starter-feign
- spring-cloud-starter-openfeign
```
 <dependencyManagement>
    <dependencies>
         <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-dependencies</artifactId>
            <version>Finchley.SR1</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
 </dependencyManagement>
 ```
#### 服务注册中心
    @EnableEurekaServer
    spring-cloud-starter-eureka-server:1.4.5.RELEASE
    spring-cloud-starter-eureka:1.4.5.RELEASE (主要用来注册自己)
#### 生产者
    @EnableDiscoveryClient
    spring-cloud-starter-eureka:1.4.5.RELEASE
#### Ribbon(Client Side Load Balancer)
    spring-cloud-starter-netflix-ribbon
    @FeignClient
    @LoadBalanced
    LoadBalancerClient.choose(xxx);
#### Hystrix（断路器）
在需要监控的服务上添加:
    @EnableCircuitBreaker
    @HystrixCommand
    spring-cloud-starter-netflix-hystrix:1.4.5.RELEASE
    spring-boot-starter-actuator
    添加Bean：
    @Configuration
    public class HystrixConfiguration {
      @Bean
      public ServletRegistrationBean<HystrixMetricsStreamServlet> getServlet() {
          HystrixMetricsStreamServlet hystrixMetricsStreamServlet = new HystrixMetricsStreamServlet();
          ServletRegistrationBean<HystrixMetricsStreamServlet> servletRegistrationBean = new ServletRegistrationBean();
          servletRegistrationBean.setServlet(hystrixMetricsStreamServlet);
          servletRegistrationBean.addUrlMappings("/hystrix.stream");
          servletRegistrationBean.setName("HystrixMetricsStreamServlet");
          return servletRegistrationBean;
      }
    }
    访问入口：/hystrix.stream
#### Hystrix Dashboard
    @EnableHystrixDashboard
    spring-cloud-starter-hystrix-dashboard:1.4.5.RELEASE
    spring-boot-starter-actuator
    访问入口：/hystrix
#### Turbine(/turbine.stream)
    @EnableTurbine
    spring-cloud-starter-netflix-turbine
    手动指定Hystrix的Service，把多个hystrix.stream合并成一个turbine.stream,
    然后在Hystrix Dashboard里面添加一个turbine.stream
#### Turbine Stream(高效版Turbine，使用消息队列)
#### Router and Filter: Zuul
    @EnableZuulServer
    spring-cloud-starter-netflix-zuul
    Example:
    zuul:
      routes:
      users:
          path: /myusers/**
          serviceId: users_service
#### Sidecar(Multi-Language Support)
    @EnableSidecar
    spring-cloud-netflix-sidecar
    Example:
    server:
      port: 5678
    spring:
      application:
          name: sidecar
    sidecar:
      port: 8000
      health-uri: http://localhost:8000/health.json