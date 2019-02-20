# Java
## 数据结构
#### HashMap
HashSet底层使用hashMap实现
- 数组Entity
    填充因子: 0.75
- Node:
    当数量少时，用LinkedList，当数量到达8时候，使用NodeTree(红黑)
#### SparseArray
从这里可以看出Android里面，很多时候需要时间换空间
- 数组实现，使用二分查找
- 主要是为了节省内存，比HashMap慢一些
#### WeakHashMap
Entry<K,V> extends WeakReference<Object>
- Key是WeakReference
- Value是强引用
- 在计算size等的时候expungeStaleEntries一次清除掉无效的Entry
#### ThreadLocal
每个Thread都有个ThreadLocal.ThreadLocalMap，用来存储ThreadLocal的值
```
Entry extends WeakReference<ThreadLocal<?>>
- value
```
## Reference
- StrongReference
- SoftReference
    内存紧张时回收
- WeakReference
    GC时回收
- PhantomReference
    跟WeakReference的区别时，它必须结合ReferenceQueue，手动从Queue中清除poll/remove。
    PhantomReference对象插入ReferenceQueue队列，而此时PhantomReference对象并没有被垃圾回收器回收，而是要等到ReferenceQueue被你真正的处理后才会被回收。
- ReferenceQueue
    在构造Reference的时候，传入ReferenceQueue， 则再回收Reference的时候，会把其放入ReferenceQueue
## Class Loader
1. Bootstrap类加载器(C++,在java中看不到它)，负责装载JRE的核心类库 – JRE/lib/rt.jar
2. Extension类加载器 – JRE/lib/ext或者java.ext.dirs指向的目录
3. Application类加载器 – CLASSPATH环境变量, 由-classpath或-cp选项定义,或者是JAR中的Manifest的classpath属性定义.

Java装载类使用“全盘负责委托机制”。“全盘负责”是指当一个ClassLoder装载一个类时，除非显示的使用另外一个ClassLoder，该类所依赖及引用的类也由这个ClassLoder载入；“委托机制”是指先委托父类装载器寻找目标类，只有在找不到的情况下才从自己的类路径中查找并装载目标类。这一点是从安全方面考虑的，试想如果一个人写了一个恶意的基础类（如java.lang.String）并加载到JVM将会引起严重的后果，但有了全盘负责制，java.lang.String永远是由根装载器来装载，避免以上情况发生 除了JVM默认的三个ClassLoder以外，第三方可以编写自己的类装载器，以实现一些特殊的需求。类文件被装载解析后，在JVM中都有一个对应的java.lang.Class对象，提供了类结构信息的描述。数组，枚举及基本数据类型，甚至void都拥有对应的Class对象。Class类没有public的构造方法，Class对象是在装载类时由JVM通过调用类装载器中的defineClass()方法自动构造的。
或许你会想，我在自定义的类加载器里面强制加载自定义的java.lang.String类，不去通过调用父加载器不就好了吗?确实，这样是可行。但是，在JVM中，判断一个对象是否是某个类型时，如果该对象的实际类型与待比较的类型的类加载器不同，那么会返回false。
## 并发

