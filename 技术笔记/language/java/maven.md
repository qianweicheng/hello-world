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
