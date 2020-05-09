# JNI
http://java.sun.com/javase/6/docs/technotes/guides/jni/spec/design.html#wp615
- 在Java中使用==可以判断两个引用是否指向同一个对象，在JNI中使用下列方法可以进行相同的判断，无论是全局引用，局部引用还是弱全局引用。
- jobject 类型的变量，如果需要全局使用，都必须用NewGlobalRef获取一次引用
- 
## 常用
- NewObject和AllocObject的区别: AllocObject仅仅构建一个新的类对象（仅仅为类对象分配内存空间而已），不初始成员变量，也不调用构造方法.  NewObject需要指明调用的构造方法，构建一个新的类对象，并初始化成员变量，调用指定的构造方法
```
env->NewObject(clsOnlineResult, "<init>", "()V");
jobject obj = env->AllocObject(cls); // 直接调用默认构造函数
```
// 使用GetObjectClass方法获取obj对应的jclass。 
jclass cls = (*env)->GetObjectClass(env, obj);       

// 直接搜索类名，需要是static修饰的类。
jclass cls = (*env)->FindClass(“android/util/log”) 

类型	符号
boolean	Z
byte	B
char	C
short	S
int	I
long	L
float	F
double	D
void	V
object对象	LClassName;      L类名;
Arrays	[array-type        [数组类型
methods方法	(argument-types)return-type     (参数类型)返回类型