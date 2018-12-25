# Springboot
## Springboot创建命令行命令行
1. 直接使用bare最方便，
2. 在Application中实现CommandLineRunner方法
## 运行
1. IDE直接运行
2. mvn spring-boot:run
3. java -jar xxx.jar
## Spring-Boot 热部署
1 使用 Spring Loaded
2 使用 spring-boot-devtools
此处我们使用方法2
a. 添加依赖
<dependency>
 <groupId>org.springframework.boot</groupId>
 <artifactId>spring-boot-devtools</artifactId>
 <optional>true</optional> <!-- 这个需要为 true 热部署才有效 -->
</dependency>

b. 设置IDE, 选中Build,Execution,Deployment->Compiler->Make project automatically
c. 运行mvn spring-boot:run
## Autoconfig
- 通过标准的Java-SPI
- 通过spring.factories注入几种类型的类，主要是AutoConfiguration, AutoConfiguration通过两种机制引入其它configuration
    - @Import其它类型
    - SpringFactoryImportSelector返回一个引入类型列表，相比@Import的优势是可以动态编程控制
## Context
## Actuator 
@Endpoint添加管理节点
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-actuator</artifactId>
    </dependency>
## 静态资源
spring.resources.static-locations=file:target/,classpath:/META-INF/resources/,classpath:/resources/,classpath:/static/,classpath:/public/
## 添加编译信息, 在/actuator/info查看
- BuildProperties:自动提取build.properties的内容
- GitProperties: 插件会自动生成git.properties
    ```
        <plugin>
           <groupId>pl.project13.maven</groupId>
            <artifactId>git-commit-id-plugin</artifactId>
        </plugin>
    ```
- InfoProperties: 在yml/properties 里面添加: info.xxx
## spring-boot-starter-parent
1. spring-boot-parent
    1.1 spring-boot-devtools
    1.2 spring-boot-starters
        1.2.1 spring-boot-starter-test
            spring-boot-test
        1.2.2 spring-boot-starter
                spring-boot
                spring-boot-autoconfigure
                spring-boot-starter-logging
                spring-core

## 常用
@EnableAutoConfiguration
@ComponentScan
@Configuration，使用了此标签的类默认就是一个Bean
@ConfigurationProperties，控制配置的前缀
@Bean 一定要放Configuration里面
@Autowired
@SpringBootApplication
@Component,
@Service, 
@Repository, 
@Controller
@RestController
@EnableScheduling
@ServletComponentScan: @WebServlet, @WebFilter, and @WebListener
## Springboot 配置文件查找顺序
0、命令行--xxx=yyy
1、config/application.properties
2、config/application.yml
3、application.properties（项目根目录下）
4、application.yml
5、resources/config/application.properties
6、resources/config/application.yml
7、resources/application.properties
8、resources/application.yml

## Springboot autoconfigure
几乎包含Spring里面的各个项目的自动配置文件：<optional>true</optional>
## 注入对象生命周期两种方式
1. JSR250： @PostConstruct，@PreDestroy
2. Spring： 注解指定@Bean(initMethod="init",destroyMethod="destroy")
## Springboot 初始化对象过程
0. SpringApplication.run 
    - SpringFactoriesLoader.loadFactoryNames:扫描class path里面所有jar包里面的spring.factories
    - 7个ApplicationContextInitializer:
        DelegatingApplicationContextInitializer
        ContextIdApplicationContextInitializer
        RestartScopeInitializer(dev)
        ConfigurationWarningsApplicationContextInitializer
        ServerPortInfoApplicationContextInitializer
        SharedMetadataReaderFactoryContextInitializer
        ConditionEvaluationReportLoggingListener
    - prepareEnvironment:创建environment,触发environmentPrepared事件，创建子Context等
    - createContext，创建一个AnnotationConfigApplicationContext（其中包含：AnnotatedBeanDefinitionReader，ClassPathBeanDefinitionScanner）
    AnnotatedBeanDefinitionReader.registerAnnotationConfigProcessors
    > 在这里会调用AnnotationConfigUtils注册内置的Processor，比如Configuration annotation processor，Autowired annotation processor，BeanNameGenerator等做为RootBeanDefinition
    - prepareEnvironment,触发environmentPrepared
        - 此处Spring Cloud 会监听，然后初始化一个context
    - prepareContext：此处触发两个事件contextPrepared和contextLoaded
        - applyInitializers 初始化4个ApplicationContextInitializer
        - createBeanDefinitionLoader(这里创建AnnotatedBeanDefinitionReader，xmlReader)：BeanDefinitionLoader.load，设置扫描的包
        - 触发contextLoaded事件
    - SpringApplication.refreshContext
    - AbstractApplicationContext->refresh
        - prepareRefresh
        - prepareBeanFactory 设置DefaultListableBeanFactory, 主要过滤的bean， 注册回调，注册系统bean
        - postProcessBeanFactory初始化spring.factories里面定义的org.springframework.boot.autoconfigure.EnableAutoConfiguration列表
        - invokeBeanFactoryPostProcessors(TODO)
        - registerBeanPostProcessors:从DefaultListableBeanFactory里面提取出PostProcessors，进行注册.在这一步基本把PostProcessors等第一层次的类全部找到
        - initMessageSource
        - initApplicationEventMulticaster
        - onRefresh(WebApplication在这里创建WebServer)
        - registerListeners()
        - finishBeanFactoryInitialization(最复杂的事情就在这里)
            - beanFactory.freezeConfiguration();
            - beanFactory.preInstantiateSingletons()
                - AbstarctBeanFactory.getBean
                - AbstarctBeanFactory.doGetBean
                - AbstarctBeanFactory.getSingleton
                - AbstarctBeanFactory.createBean
                    - resolveBeforeInstantiation 如果创建了一个wrapper则直接返回
                    - doCreateBean
                        - createBeanInstance：处理autowire，构造函数依赖等
                            - instantiateBean调用BeanUtils.instantiateClass最终初始化，返回一个wrapper
                            - populateBean 初始化bean的各个属性，AutowrieAnnotationBeanPostProcessor在此工作，postProcessPropertyValues->inject->resolveDependency
                            - initializeBean（TODO）
                        - applyMergedBeanDefinitionPostProcessors->PostProcessor.postProcessMergedBeanDefinition->(在这一步初始化普通Bean)
                            - populateBean->postProcessPropertyValues->inject
                            - createBeanInstance
            
        - finishRefresh(在这里启动WebServer并发布ServletWebServerInitializedEvent)
    - afterRefresh
    - 触发started事件
    - Call ApplicationRunner/CommandLineRunner
    - 触发running事件
    - 返回context  
## HTTP的几个Client对比
- Java标准HttpURLConnection(Feign默认使用)
- Apache HttpClient
- OkHttp
## 其它
## 数据总线：Application Event
- spring-boot-context:DelegatingApplicationListener.onApplicationEvent
- spring-cloud-context:BootstrapApplicationListener.onApplicationEvent
- RestartApplicationListener
- ClasspathLoggingApplicationListener
- BackgroundPreinitializer
- DelegatingApplicationListener
- ConditionEvaluationReportLoggingListener

