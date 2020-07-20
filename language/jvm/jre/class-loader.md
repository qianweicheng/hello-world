# ClassLoader
Java装载类使用“全盘负责委托机制”。“全盘负责”是指当一个ClassLoder装载一个类时，除非显示的使用另外一个ClassLoder，该类所依赖及引用的类也由这个ClassLoder载入；“委托机制”是指先委托父类装载器寻找目标类，只有在找不到的情况下才从自己的类路径中查找并装载目标类。这一点是从安全方面考虑的，试想如果一个人写了一个恶意的基础类（如java.lang.String）并加载到JVM将会引起严重的后果，但有了全盘负责制，java.lang.String永远是由根装载器来装载，避免以上情况发生 除了JVM默认的三个ClassLoder以外，第三方可以编写自己的类装载器，以实现一些特殊的需求。类文件被装载解析后，在JVM中都有一个对应的java.lang.Class对象，提供了类结构信息的描述。数组，枚举及基本数据类型，甚至void都拥有对应的Class对象。Class类没有public的构造方法，Class对象是在装载类时由JVM通过调用类装载器中的defineClass()方法自动构造的。
或许你会想，我在自定义的类加载器里面强制加载自定义的java.lang.String类，不去通过调用父加载器不就好了吗?确实，这样是可行。但是，在JVM中，判断一个对象是否是某个类型时，如果该对象的实际类型与待比较的类型的类加载器不同，那么会返回false。
## 加载器
1. Bootstrap类加载器(C++,在java中看不到它)，负责装载JRE的核心类库 – JRE/lib/rt.jar
2. Extension类加载器 – JRE/lib/ext或者java.ext.dirs指向的目录
3. Application类加载器 – CLASSPATH环境变量, 由-classpath或-cp选项定义,或者是JAR中的Manifest的classpath属性定义.
## 双亲加载
1. 安全性
2. 效率

## 类加载-初始化
1. 加载过程
   1. Loading
      1. 双亲委派，主要出于安全来考虑
      2. LazyLoading 五种情况
         1. –new getstatic putstatic invokestatic指令，访问final变量除外
            –java.lang.reflect对类进行反射调用时
            –初始化子类的时候，父类首先初始化
            –虚拟机启动时，被执行的主类必须初始化
            –动态语言支持java.lang.invoke.MethodHandle解析的结果为REF_getstatic REF_putstatic REF_invokestatic的方法句柄时，该类必须初始化
      3. ClassLoader的源码
         1. findInCache -> parent.loadClass -> findClass()
      4. 自定义类加载器
         1. extends ClassLoader
         2. overwrite findClass() -> defineClass(byte[] -> Class clazz)
         3. 加密
         4. 热启动，热部署
      5. 执行模式
         1. 混合执行(默认-X:+mixed)
         2. 编译执行(-X:+comp)
         3. 解释执行(-X:+int)
         4. 检测热点代码：-XX:CompileThreshold = 10000
   2. Linking 
      1. Verification
         1. 验证文件是否符合JVM规定
      2. Preparation
         1. 静态成员变量赋默认值
      3. Resolution
         1. 将类、方法、属性等符号引用解析为直接引用
            常量池中的各种符号引用解析为指针、偏移量等内存地址的直接引用
   3. Initializing
      1. 调用类初始化代码 <clinit>，给静态成员变量赋初始值
2. 小总结：
   1. load - 默认值 - 初始值
   2. new - 申请内存 - 默认值 - 初始值