# Build
- gcc/g++: 基础编译工具
    `gcc xxx.c -I(the-include-path) -L(the-lib-path) -l(the-lib-name)`
- Makefile(make): 一个批处理编译源文件的工具
- CMake: 一个可以更加简单的生成makefile文件给上面那个make用
    `brew install cmake`
    CMake是一种跨平台编译工具，比make更为高级，使用起来要方便得多。CMake主要是编写CMakeLists.txt文件，然后用cmake命令将CMakeLists.txt文件转化为make所需要的makefile文件，最后用make命令编译源码生成可执行程序或共享库（so(shared object)）
## Makefile文件
- ./configure
- make
- make install
## Cmake
- `cmake -Dxxx=yyy the-CMakeLists.txt-file-path`
- make
## Building dynamic library
`gcc test.c -fPIC -shared -o libtest.so`
## Using dynamic library
```
gcc main.c ccallp.c -o main -I./include -L ./lib -lpython3.6m
export LD_LIBRARY_PATH=`pwd`;./main
```