# Golang
https://books.studygolang.com/advanced-go-programming-book/
## 变量定义:
  - 变量: `var name type`, `var hp int = 100`, `var hp = 100`
  - 数组: `var name [N]type`
  - 简短方式
  ```
    简短格式
    名字 := 表达式
    需要注意的是，简短模式（short variable declaration）有以下限制：
    1. 定义变量，同时显式初始化。
    2. 不能提供数据类型。
    3. 只能用在函数内部。
  ```
  - 匿名变量`_`,不占内存
  - 常量: `const Pi = 3.14159`
- 数据类型:
  ```
    bool
    string
    int、int8、int16、int32、int64
    uint、uint8、uint16、uint32、uint64、uintptr
    byte // uint8 的别名
    rune // int32 的别名 代表一个 Unicode 码
    float32、float64
    complex64、complex128
  ```
- 字符串
    - 双引号
    - 反引号"`"
    - 包：strings，strconv
## 变量初始化
- 顺序
  - 每个包的变量
  - 每个包的init函数
    - 程序的初始化运行在单个Go程中，但该Go程可能会创建其它并发运行的Go程。
    - 若包 p 导入了包 q，则 q 的 init 函数会在 p 的任何函数启动前完成。
  - main包的main入口
- 除了new创建的，都是值类型；make创建出来的也一样，只不过其底层捂住了一个指针
- make用于创建map,slic,channel,slic为指针
- Go语言和C语言一样，类型都是基于值传递的。要想修改变量的值，只能传递指针
- 在Go语言中没有构造函数的概念，一般使用工厂方法
  rect1 := new(Rect)
  rect2 := &Rect{}
- 暴露给外部使用的成员或者方法都必须大写开头
## Go语言变量会进行逃逸分析
Go 编译器自行决定变量分配在堆栈或堆上，以保证程序的正确性。
Go编译器将为该函数的堆栈帧中的函数分配本地变量。但是，如果编译器在函数返回后无法证明变量未被引用，则编译器必须在垃圾收集堆上分配变量以避免悬空指针错误。此外，如果局部变量非常大，将它存储在堆而不是堆栈上可能更有意义。
在当前的编译器中，如果变量具有其地址，则该变量是堆上分配的候选变量。但是，基本的转义分析可以识别某些情况，这些变量不会超过函数的返回值并且可以驻留在堆栈上。

Go的编译器会决定在哪(堆or栈)分配内存，保证程序的正确性。
## Tips
- Go 中数组赋值和函数传参都是值复制的。
- Slice：引用传递
定义:
```
letters := []string{"a", "b", "c", "d"}
s := make([]string, 5, 5)
s := make([]byte, 5)
```
- 字符串拼接
```
1. +号
2. strings.Join
3. fmt.Sprint
4. g :=new(byte.Buffer) or g :=new(byte.Builder)
```
- 只有一个for：`for i:=0;i<100;i++`or `for i<100{}` or `for{}` or `for i, v := range pow`
- `if v := math.Pow(x, n); v < lim `
- switch,有两种写法，默认break，显式fallthouth
```
switch {
	case t.Hour() < 12:
		fmt.Println("Good morning!")
	case t.Hour() < 17:
		fmt.Println("Good afternoon.")
	default:
		fmt.Println("Good evening.")
	}
```
- defer
- 结构体类型上定义方法,使用指针和不使用指针的方式
- 接口类型的值可以存放实现这些方法的任何值， golang使用duck模式
- chan
  ```
  ch := make(chan int)
  ch <- v    // 将 v 送入 channel ch。
  v := <-ch  // 从 ch 接收，并且赋值给 v。
  ```
  - select
  ```
  select {
  case i := <-c:
      // 使用 i
  default:
      // 从 c 读取会阻塞
  }
  ```
  - 只有发送者才能关闭 channel，而不是接收者
  - 循环 `for i := range c` 会不断从 channel 接收值，直到它被关闭。