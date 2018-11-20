#Kotlin
##空安全
- 在条件中检查null
    ```
    var k = if(i!=null) i.length else -1
    ```
- 安全调用, Elvis操作符:`?.`
    ```
    var k = i?.length ?: -1
    ```
- !!操作符
    ```
    var k = i!!.length
    ```
##函数式编程的特点
- 函数是”第一等公民”
- 只用”表达式”，不用”语句”
- 无副作用，不修改状态，引用透明
##函数分类
- 基本函数
    ```
    // 无返回值, Unit vs Void
    fun printHello(name: String?): Unit {
        if (name != null)
        println("Hello ${name}")
        else
        println("Hi there!")
        // `return Unit` 或者 `return` 是可选的
    }
    ```
- 单表达式函数
    ```
    fun getTriple(x: Int): Int = x * 3
    // 返回值类型可由编译器推断时
    fun getTriple(x: Int) = x * 3
    ```
- 顶层函数
- 中缀函数(infix)
    ```
    infix fun Int.shl(x: Int): Int {
        …… 
    }
    ```
    使用：
    ```
    // 用中缀表示法调用该函数
    1 shl 2
    // 等同于这样
    1.shl(2)
    ```
- 局部函数
- 泛型函数
- 尾递归函数(tailrec)
    >一个函数用 tailrec 修饰符标记并满足所需的形式时，编译器会优化该递归，留下一个快速而高效的基于循环的版本
- 扩展函数
  ```
    fun ArrayList<T>.swap(index1: T, index2: T) {
        val tmp = this[index1] 
        this[index1] = this[index2]
        this[index2] = tmp
    }
  ```
- 内联函数(inline)
- 高阶函数
- 匿名函数
    ```
    fun(x: Int, y: Int): Int {
        return x + y
    }
    ```
- Lambda 表达式
语法糖：
    - 如果函数的最后一个参数接受函数，那么作为相应参数传入的 lambda 表达式可以放在圆括号之外：
        `foo("abc"){a,b=>a+b}`
    - 当参数只有一个的时候，声明中可以不用显示声明参数，在使用参数时可以用 it 来替代那个唯一的参数。
        `var inc = {it+1}`
    - 当有多个用不到的参数时，可以用下划线来替代参数名，但是如果已经用下划线来省略参数时，是不能使用 it 来替代当前参数的。
    - 可以使用限定的返回语法从lambda显式返回一个值。 否则，将隐式返回最后一个表达式的值。