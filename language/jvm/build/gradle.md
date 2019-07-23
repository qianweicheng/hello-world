# Gradle
## 总览
- 评估(evaluated) 读取settings.gradle
- 配置: 读取build.gradle
- 执行
>评估阶段的Hook放build.gradle的话会导致无法执行
## Gradle Core Object
- Gradle对象，当我们执行gradle xxx的时候，gradle会从默认的配置脚本中构造出一个Gradle对象。整个执行过程中，就只有这么一个对象。
    https://docs.gradle.org/current/dsl/org.gradle.api.invocation.Gradle.html
- Project 对象： 每一个build.gradle会转换成一个Project对象。
    https://docs.gradle.org/current/dsl/org.gradle.api.Project.html
- Settings对象：每一个settings.gradle都会转换成一个Settings对象
    https://docs.gradle.org/current/dsl/org.gradle.api.initialization.Settings.html
    常使用的有属性:
    - gradle
    - rootProject
    常使用的方法:
    - include
    - apply
    - project
## 系统属性
设置:
- 命令行： `gradle -D name=value` or `gradle -P name=value`
- gradle.properties文件
- project.ext.name=value
读取:
System.properties['JAVA_HOME']
project.ext.name
## Task
https://blog.csdn.net/weixin_38062353/article/details/82710203
### 基本定义
```
task task1 {
    doFirst {

    }
    doLast {

    }
}
task task2 << {
    // <<相当于doLast
}
task1.doFirst {} //包一层回调， 前者靠前，后者愈后
task1.doLast {}
```
### 动态定义:
```
3.times { i ->
    task "Mytask$i" << {
        //
    }
}
```
### task依赖
```
task task1(dependsOn:xxx) << {

}
task task1(dependsOn:[xxx,yyy]) << {
    
}
```
指定类型:有点类似集成自带task
```
task copyFile(type:Copy) {
    from 'xxx'
    info 'yyy'
    include '1.txt'
    rename  '1.txt', '2.txt'
}
```
打印所有task:
```
task printlnAllTask<<{
    tasks.eachWithIndex {task,index->
        println "${index}     ${task.name}"
    }
}
```
## 依赖
```
dependencies {
    compile fileTree(dir:'libs',include:['*.jar'])
    compile 'com.xxx.yyy:zzz:1.0.0'
    compile group:'com.xxx.yyy', name:'zzz', version: '1.0.0'
}
```
<Gradle 3.4|Gradle 3.4+
:-:|:-:
apk|runtimeOnly
provided|compileOnly
compile|api
没有对应|implementation
debugCompile|debugImplementation
releaseCompile|releaseImplementation
androidTestCompile|androidTestImplementation
## 插件
- 直接在build.gradle 中编写
- 单独module编写（名字必须是buildSrc）
- 上传到maven库，添加依赖引用
buildscript 节点配置gradle的运行环境，包括引入插件. 
比如引入了
`apply plugin: "com.android.application"`插件之后
就可以使用:
`apply plugin: 'com.android.application'`
`apply plugin: 'com.android.library'`
```
buildscript {
    dependencies {
        classpath 'com.android.tools.build:gradle:2.3.0'
        classpath "io.realm:realm-gradle-plugin:5.1.0"
        classpath 'com.google.gms:google-services:4.0.1'
    }
}
```
## 目录
- caches # gradle缓存目录
    - modules-2 # 下载缓存目录
        - files-2.1 # gradle下载的jar/aar目录
            ${org}/${package}/${version}/${shanum1}/${package-version}.pom
            ${org}/${package}/${version}/${shanum2}/${package-version}.jar
        - metadata-2.xx
- daemon # daemon日志目录
- native # gradle平台相关目录
- wrapper # gradle-wrapper下载目录