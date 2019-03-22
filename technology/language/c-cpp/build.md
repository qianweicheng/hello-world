# Build
- gcc/g++: 基础编译工具
- Makefile(make): 一个批处理编译源文件的工具
- CMake: 一个可以更加简单的生成makefile文件给上面那个make用
    `brew install cmake`
    CMake是一种跨平台编译工具，比make更为高级，使用起来要方便得多。CMake主要是编写CMakeLists.txt文件，然后用cmake命令将CMakeLists.txt文件转化为make所需要的makefile文件，最后用make命令编译源码生成可执行程序或共享库（so(shared object)）
## Makefile文件
- ./configure
- make
- make install