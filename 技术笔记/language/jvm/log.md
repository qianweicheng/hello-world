### slf4j 和 commons-logging 都是日记接口
#### slf4j:The Simple Logging Facade for Java
#### commons-logging(JCL): 

#### log4j logback
log4j是apache实现的一个开源日志组件。
logback同样是由log4j的作者设计完成的，拥有更好的特性，用来取代log4j的一个日志框架。是slf4j的原生实现。（Native implementations）

#### slf4j + logback组合
    1. slf4j-api （slf4j接口）
    1. logback-classic (logback服务于slf4j的”驱动”)
    1. logback-core (logback日志实现)
    1. 如果系统有依赖log4j日志体系，想统一对接到logback，则需要依赖：log4j-over-slf4j

#### slf4j+log4j
    1. slf4j-api （slf4j接口）
    1. slf4j-log4j (log4j 服务于slf4j的”驱动”)
    1. log4j (log4j 日志实现)
    1. log4j.properties

#### JCL+log4j
    1. commons-logging
    2. log4j
    3. log4j.properties


### 不同的获取logger的方式
#### 直接log4j：
import org.apache.log4j.Logger;
Logger logger= Logger.getLogger(xx.class);
#### jcl:
import org.apache.commons.logging.Log; 
import org.apache.commons.logging.LogFactory;
private static Log log = LogFactory.getLog(xx.class);
#### slf4j：
import  org.slf4j.Logger;
import  org.slf4j.LoggerFactory;
Logger logger = LoggerFactory.getLogger(xx.class);
 

<dependency>
    <groupId>org.slf4j</groupId>
    <artifactId>slf4j-log4j12</artifactId>
    <version>1.7.21</version>
</dependency>