# Golang
- 变量定义:
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
- 常量
  `const Pi = 3.14159`
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
## Go语言变量会进行逃逸分析
## 包管理
