# Steps
1. 编译python
```
    cmake -DCMAKE_INSTALL_PREFIX:PATH=`pwd`/../python-install \
    -DBUILD_LIBPYTHON_SHARED=ON ../
    make -j10
    make install
```
2. 编译本项目
拷贝第一步编译好的两个文件到本项目中
```
gcc -o libmybridge.dylib -shared -fPIC ccallp.c -I./include -L ./lib -lpython3.6m
gcc main.c -o main -I./include  -L . -l mybridge
```
3. 运行
`./main ccallp great_function 2`