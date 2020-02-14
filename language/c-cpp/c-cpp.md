# C-CPP
## C历史
- C90标准(ANSI C)：
- C99标准：引入了许多特性，包括内联函数（inline functions）、可变长度的数组、灵活的数组成员（用于结构体）、复合字面量、指定成员的初始化器、对IEEE754浮点数的改进、支持不定参数个数的宏定义，在数据类型上还增加了 long long int 以及复数类型。
- C11标准：字节对齐说明符、泛型机制（generic selection）、对多线程的支持、静态断言、原子操作以及对 Unicode 的支持。
## CPP历史
- C++98:C++标准第一版
- C++03:
- C++11: 新增的右值引用使得能够给容器提供移动语义。其次，由于新增了模板类initilizer_list，因此新增了将initilizer_list作为参数的构造函数和赋值运算符。第三，新增的可变参数模板（variadic template）和函数参数包（parameter pack）使得可以提供就地创建（emplacement）方法
- C++14: 主要是支持普通函数的返回类型推演，泛型 lambda，扩展的 lambda 捕获，对 constexpr 函数限制的修订，constexpr变量模板化
## C/CPP Support in GNU
GNU 在标准的C/CPP基础上加了GNU extensions
## 编译器
- C: GCC, Clang，
- CPP: G++, Clang++
gcc和g++都可以编译c/c++，区别在于对编译时候的一些默认选项. 本质而言，gcc和g++并不是编译器，也不是编译器的集合
1. 对于 *.c和*.cpp文件，gcc分别当做c和cpp文件编译（c和cpp的语法强度是不一样的）
2. 对于 *.c和*.cpp文件，g++则统一当做cpp文件编译
3. 使用g++编译文件时，g++会自动链接标准库STL，而gcc不会自动链接STL
4. gcc在编译C文件时，可使用的预定义宏是比较少的
5. gcc在编译cpp文件时/g++在编译c文件和cpp文件时（这时候gcc和g++调用的都是cpp文件的编译器），会加入一些额外的宏:
    ```
    #define __GXX_WEAK__ 1
    #define __cplusplus 1
    #define __DEPRECATED 1
    #define __GNUG__ 4
    #define __EXCEPTIONS 1
    ```
## 编译
`g++ == gcc -xc++ -lstdc++ -libgcc -shared`
`g++ -std=c++11 input.cxx -o a.out`
常见参数：
```
  –lstdc++  添加stl支持
  -std=c++11
  -std=c++14
  -std=gnu++14
```
## C/C++互相调用
这里主要涉及到ABI，由于函数命名C++函数编译的时候， 会把参数类型加入名字中，C则不会，导致相互间调用需要进行处理
complie function as C api 和 linker function as C api。
因为C++形式的ABI 二进制接口没有统一规范. 如果采用第三方库1.0之后，对方进行了升级到2.0，很有可能会造成库的二进制文件内存布局的变化，导致不兼容。不能只更新第三方库。还需要编译整个项目。生产环境很不推荐在dll里暴露C++接口，尤其是模板接口。因为除非所有的binary都在你的控制之下，否则他们一旦使用的编译器不同（版本不同也算），就极有可能内存miss match垮掉。
```
//C_library.h

#ifdef __cplusplus
extern "C" {
#endif

//
// ... prototypes for C_library go here ...
//

#ifdef __cplusplus
}
#endif
```
## Application binary interface(ABI)
### C ABI
目前没有标准，但一般一个硬件平台/操作系统一个。
- The ARM ABI
- The PowerPC Embedded ABI
- The several ABIs of x86
- Oracle Solaris ABI
- X84情况复杂写。分Windows和Linux

C ABI 指定：
- 预定义类型（char、int、float 等）的大小和布局
- 复合类型（array 和 struct）的布局
- 编程人员定义的名称的外部（链接器可见）拼写
- 机器码函数调用序列
- 堆栈布局
- 寄存器使用
## C++ ABI
目前没有标准，分裂程度比C严重得多。C++ ABI 包括 C ABI。虽然 C++ 标准没有规定C++的ABI，但是几乎所有主流平台都有明文或事实上的 ABI 标准。比方说 
- ARM 有 EABI，Intel Itanium（英特尔安腾）  有 http://www.codesourcery.com/public/cxx-abi/abi.html，
- x86-64 有仿 Itanium 的 ABI，
- SPARC 和 MIPS 也都有明文规定的 ABI
- x86是个例外，它只有事实上的 ABI，比如 
  - Windows是Visual C++，
  - Linux是G++(G++的 ABI 还有多个版本，目前最新的是 G++ 3.4 的版本)。

它还包括以下特性：
- 层次结构类对象（即，基类和虚拟基类）的布局
- 指向成员的指针的布局
- 传递隐藏函数参数（例如 this）
- 如何调用虚拟函数：
- Vtable 内容和布局
- 指向 vtable 的指针在对象中的位置
- 查找 this 指针调整
- 查找基类偏移
- 通过指向成员的指针调用函数
- 管理模板实例
- 名称的外部拼写（“名称改编”）name mangling
- 构造和析构静态对象
- 抛出和捕获异常。RTTI
- 标准库的一些细节：
- 实现定义的细节
- 类型信息和运行时类型信息
- 内联函数对成员的访问

## 标准库
glibc是linux下面c标准库的实现，即GNU C Library。glibc本身是GNU旗下的C标准库，后来逐渐成为了Linux的标准c库，而Linux下原来的标准c库Linux libc逐渐不再被维护。Linux下面的标准c库不仅有这一个，如uclibc（https://www.uclibc.org/）、klibc，以及上面被提到的Linux libc，但是glibc无疑是用得最多的。glibc在/lib目录下的.so文件为libc.so.6。

