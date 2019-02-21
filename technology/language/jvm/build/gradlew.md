# Gradlew
在gradle基础上包了一层，主要是解决版本差异化问题.
## 配置
手动创建gradlew: 在一个空的文件夹中运行`gradle wrapper`
配置文件在：gradle-wrapper.properties
distributionUrl: 远程gradle目录
distributionPath: 下载目录,跟distributionBase结合构成，一般在: `~/gradle/wrapper/dist`
## 常用命令
```
gradlew -v 版本号
gradlew clean 清除目录下的build文件夹
gradlew build 检查依赖并编译打包
gradlew assembleDebug 编译并打Debug包
gradlew assembleRelease 编译并打Release的包
gradlew -q app:dependencies 打印依赖
```
