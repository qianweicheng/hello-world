#jar/META-INF
> 这个文件用来描述此Jar包的一些基本信息，重点有如下三个文件。可以通过在src/main/resources创建一个META-INF文件夹来任意加入文件
##MANIFEST.MF
> 描述jar包的入口类，Class Path(对于可执行文件)，version，author等等
##SPI：service/
> 是 JDK 1.5 后提供的一种服务扩展接口。目前有不少框架用它来做服务的扩展，如 Dubbo，Spring Cloud。 格式如下：service文件夹下存放以接口命名的文件，文件内容就是接口的实现，一行一个实现.
使用JDK自带的java.util.ServiceLoader进行加载.
```
        ServiceLoader<IHello> serviceLoader = ServiceLoader.load(IHello.class);
        Iterator<IHello> it = serviceLoader.iterator();
        while (it != null && it.hasNext()) {
            IHello helloService = it.next();
            helloService.say();
        }
```
##spring.factories
> 主要对于Spring， 内容以properties格式存放，key为接口名，value为实现，多value可以使用逗号隔开