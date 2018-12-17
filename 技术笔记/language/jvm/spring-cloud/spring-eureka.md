# Eureka
[文档](https://github.com/Netflix/eureka/wiki/)
@Autowired
private DiscoveryClient client;
ServiceInstance instance = client.getLocalServiceinstance();
## 在单机模式下不需要注册自己，但在集群模式现需要打开
## 代码
EurekaClientAutoConfiguration
EurekaAutoServiceRegistration
EurekaServiceRegistry 注册类
EurekaRegistration 注册信息
