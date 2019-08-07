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
## 编译
`g++ -std=c++11 input.cxx -o a.out`
- 通过如下标志选择版本：
  `-std=c++14` or `-std=gnu++14`
## 标准库
glibc是linux下面c标准库的实现，即GNU C Library。glibc本身是GNU旗下的C标准库，后来逐渐成为了Linux的标准c库，而Linux下原来的标准c库Linux libc逐渐不再被维护。Linux下面的标准c库不仅有这一个，如uclibc（https://www.uclibc.org/）、klibc，以及上面被提到的Linux libc，但是glibc无疑是用得最多的。glibc在/lib目录下的.so文件为libc.so.6。

