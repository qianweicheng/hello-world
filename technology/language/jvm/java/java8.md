# Lambda
    Lambda表达式 vs 匿名类
    一个关键的不同点就是关键字 this。匿名类的 this 关键字指向匿名类，而lambda表达式的 this 关键字指向包围lambda表达式的类。另一个不同点是二者的编译方式。Java编译器将lambda表达式编译成类的私有方法。使用了Java 7的 invokedynamic 字节码指令来动态绑定这个方法。
# 方法引用

# 函数式接口,只有一个
    函数式接口就是一个有且仅有一个抽象方法，但是可以有多个非抽象方法的接口。
    函数式接口可以被隐式转换为lambda表达式。
    函数式接口可以现有的函数友好地支持 lambda。

    lambda表达式仅能放入如下代码：预定义使用了 @Functional 注释的函数式接口，自带一个抽象函数的方法，或者SAM（Single Abstract Method 单个抽象方法）类型。这些称为lambda表达式的目标类型，可以用作返回类型，或lambda目标代码的参数。例如，若一个方法接收Runnable、Comparable或者 Callable 接口，都有单个抽象方法，可以传入lambda表达式。类似的，如果一个方法接受声明于 java.util.function 包内的接口，例如 Predicate、Function、Consumer 或 Supplier，那么可以向其传lambda表达式。
# 默认方法
    private interface Defaulable {
        // Interfaces now allow default methods, the implementer may or 
        // may not implement (override) them.
        default String notRequired() { 
            return "Default implementation"; 
        }        
    }
# Streams
# Optional
# 并行数组
# 重复注解
# 更好的类型推断
# Date/Time API(JSR 310)
