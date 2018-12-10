http://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html

####通过绑定阶段隐性运行
mvn clean
mvn install
mvn package
mvn test
####显性运行（只会单独运行该插件，不会完整走生命周期）
mvn pluginId:goal@id
mvn exec:java@goalId
mvn exec:exec
####获取帮助
mvn help:describe -Dplugin=“Goal Prefix” -Ddetail
mvn help:describe -Dplugin=“Group:Artifact”
####隐藏默认的plugin（hack）
建一个id跟已有的plugin一样的，然后把goals设置成none

####常用插件
- maven-jar-plugin + maven-dependency-plugin
- maven-shade-plugin
- maven-assembly-plugin
- spring-boot-maven-plugin
- Git-Commit-Id-Plugin

####mvnw（maven wrapper）安装方式
默认使用IntelliJ都会自动添加mvnw，如果没有，则可以通过如下两种方式添加
方法1(推荐). 下载指定的mvn版本号，然后运行mvnw：`mvn -N io.takari:maven:wrapper -Dmaven=3.5.3`

方法2. 
1. pom.xml中添加
    ```
    <plugin>
        <groupId>com.rimerosolutions.maven.plugins</groupId>
        <artifactId>wrapper-maven-plugin</artifactId>
        <version>0.0.5</version>
    </plugin>
    ```
2. 运行：`mvn wrapper:wrapper`
####dependency详解
- scope: 设置编译的选项
    - compline(默认):compile是默认的范围；如果没有提供一个范围，那该依赖的范围就是编译范围
    - provided: 依赖只有在当JDK 或者一个容器已提供该依赖之后才使用
    - runtime:赖在运行和测试系统的时候需要，但在编译的时候不需要。比如，你可能在编译的时候只需要JDBC API JAR，而只有在运行的时候才需要JDBC
    - test: 在一般的编译和运行时都不需要，它们只有在测试编译和测试运行阶段可用。
- type:
    - pom:定义引用的是一个pom文件
    - jar:定义引用的是一个jar文件
- optional:true,false
    解绑引用链关系
####常用命令
- 查看依赖树: mvn dependency:tree