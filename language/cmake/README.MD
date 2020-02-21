# 编译Python
## cmake
https://cmake.org/cmake/help/latest/index.html
- 不区分大小写
- 命令由命令名称、小括号和参数组成,参数之间使用空格进行间隔
- `AUX_SOURCE_DIRECTORY(. DIR_SRCS)` AUX_SOURCE_DIRECTORY 将当前目录中的源文件名称赋值给变量 DIR_SRCS 
- `ADD_EXECUTABLE(main ${DIR_SRCS})` 
- 定义顶级target三种方法：
  - add_executable()
  - add_library()
  - add_custom_target()

## 命令
add_dependencies(target1 target-dependency)
add_custom_target
add_custom_command
## 常量/变量
https://cmake.org/cmake/help/v3.17/manual/cmake-variables.7.html

## Demo1
```
#1. cmake verson，指定cmake版本 
CMAKE_MINIMUM_REQUIRED(VERSION 3.2)
SET(CMAKE_CXX_STANDARD 14)
SET(CMAKE_CXX_STANDARD_REQUIRED ON)
SET(CMAKE_CXX_EXTENSIONS OFF)

OPTION (USE_MYMATH "Use provided math implementation" ON)
# 是否加入 MathFunctions 库
IF (USE_MYMATH)
    INCLUDE_DIRECTORIES ("${PROJECT_SOURCE_DIR}/math")
    add_subdirectory (math)
    SET (EXTRA_LIBS ${EXTRA_LIBS} MathFunctions)
ENDIF (USE_MYMATH)

#2. project name，指定项目的名称，一般和项目的文件夹名称对应
PROJECT(test_sqrt)

#3. head file path，头文件目录
INCLUDE_DIRECTORIES(
    include
)

#4.source directory，源文件目录
AUX_SOURCE_DIRECTORY(src DIR_SRCS)
AUX_SOURCE_DIRECTORY(lib DIR_LIB)
AUX_SOURCE_DIRECTORY(thirdparty DIR_TP)

#5. 汇总所有源代码文件夹设置环境变量，编译用到的源文件全部都要放到这里，否则编译能够通过，但是执行的时候会出现各种问题，比如"symbol lookup error xxxxx , undefined symbol"
SET(TEST_MATH
    ${DIR_SRCS}
    ${DIR_LIB}
    ${DIR_TP}
)

#6. 指定头文件目录位置，添加共享库搜索路径
INCLUDE_DIRECTORIES(${PROJECT_SOURCE_DIR}/include)
LINK_DIRECTORIES(${PROJECT_SOURCE_DIR}/lib)


# 编译可执行文件
ADD_EXECUTABLE(${PROJECT_NAME} ${TEST_MATH})
# (Optional)添加可执行文件所需要的库，比如我们用到了libm.so（命名规则：lib+name+.so），就添加该库的名称
TARGET_LINK_LIBRARIES(${PROJECT_NAME} m)

# 编译库文件
ADD_LIBRARY( 
    # Sets the name of the library.
    native-lib
    # Sets the library as a shared library.
    SHARED
    # Provides a relative path to your source file(s).
    ${SRC_LIST}
)
```
## Demo2
https://github.com/python-cmake-buildsystem/python-cmake-buildsystem

``` Android
    cmake -DCMAKE_INSTALL_PREFIX:PATH=`pwd`/../python-install \
        -DCMAKE_TOOLCHAIN_FILE=$ANDROID_NDK/build/cmake/android.toolchain.cmake \
        -DANDROID_ABI=x86 ../
make -j10
```
``` *inux
    cmake -DCMAKE_INSTALL_PREFIX:PATH=`pwd`/../python-install \
    -DBUILD_LIBPYTHON_SHARED=ON ../
make -j10
make install
```
``` *inux + shard libx`
make -j10
make install


cmake -S. -B_builds -GXcode \
    -DCMAKE_SYSTEM_NAME=iOS \
    "-DCMAKE_OSX_ARCHITECTURES=armv7;armv7s;arm64;i386;x86_64" \
    -DCMAKE_OSX_DEPLOYMENT_TARGET=9.3 \
    -DCMAKE_INSTALL_PREFIX=`pwd`/_install \
    -DCMAKE_XCODE_ATTRIBUTE_ONLY_ACTIVE_ARCH=NO \
    -DCMAKE_IOS_INSTALL_COMBINED=YES
```

## Tell configure what flags Android requires.
// Tell configure what tools to use.
target_host=aarch64-linux-android
export AR=$target_host-ar
export AS=$target_host-clang
export CC=$target_host-clang
export CXX=$target_host-clang++
export LD=$target_host-ld
export STRIP=$target_host-strip
export CFLAGS="-fPIE -fPIC"
export LDFLAGS="-pie"