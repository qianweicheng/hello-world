# Golang
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
  - main包的main入口
- 除了new创建的，都是值类型；make创建出来的也一样，只不过其底层捂住了一个指针
- make用于创建map,slic,channel,slic为指针
- Go语言和C语言一样，类型都是基于值传递的。要想修改变量的值，只能传递指针
- 在Go语言中没有构造函数的概念，一般使用工厂方法
  rect1 := new(Rect)
  rect2 := &Rect{}
- 暴露给外部使用的成员或者方法都必须大写开头
## Go语言变量会进行逃逸分析