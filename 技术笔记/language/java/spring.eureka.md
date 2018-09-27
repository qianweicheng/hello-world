#Eureka
@Autowired
private DiscoveryClient client;
ServiceInstance instance = client.getLocalServiceinstance();
##在单机模式下不需要注册自己，但在机器模式现需要打开
