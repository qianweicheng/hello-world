##手动编译Java
- javac xxx.jar
- 创建META-INF/MENIFEST.MF, 注意最后面的空行
    ```
    Manifest-Version: 1.0
    Created-By: 1.8.0_121 (Oracle Corporation)
    Main-Class: Hello

    ```
- 注意文件顺序：`jar -cvfm xxx.jar META-INF/MENIFEST.MF xxx.class *`

##classpath和classpath*区别： 
- classpath：只会到你的class路径中查找找文件。
- classpath*：不仅包含class路径，还包括jar文件中（class路径）进行查找。
- "**/"表示的是任意目录