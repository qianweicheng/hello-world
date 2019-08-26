# NDK
- 原生共享库：NDK 从 C/C++ 源代码编译这些库或 .so 文件。
- 原生静态库：NDK 也可编译静态库或 .a 文件，而您可将静态库关联到其他库。
- Java 原生接口 (JNI)：JNI 是 Java 和 C++ 组件用以互相通信的接口。
- 应用二进制接口 (ABI)：ABI 可以非常精确地定义应用的机器代码在运行时应该如何与系统交互。NDK 根据这些定义编译 .so 文件。不同的 ABI 对应不同的架构：NDK 为 32 位 ARM、AArch64、x86 及 x86-64 提供 ABI 支持。有关详情，请参阅 ABI 管理。
- 清单：如果编写的应用不包含 Java 组件，则必须在清单中声明 NativeActivity 类。原生 Activity 和应用的“使用 native_activity.h 接口”部分进一步详细介绍了如何执行此操作。
## JNI 提示
- JNI代码更推荐使用C++来编写
- JNI 定义了两个关键数据结构，即“JavaVM”和“JNIEnv”。两者本质上都是指向函数表的二级指针（在 C++ 版本中，它们是满足以下条件的类：具有指向函数表的指针，并且具有间接通过函数表的每个 JNI 函数的成员函数）。
- JNIEnv 提供了大多数 JNI 函数。原生函数均会接收 JNIEnv 作为第一个参数
- JNIEnv 可用于线程本地存储。因此，无法在线程之间共享 JNIEnv， 可以共享相应 JavaVM
- OnLoad
    当我们使用System.loadLibarary()方法加载so库的时候，Java虚拟机就会找到这个JNI_OnLoad函数兵调用该函数，这个函数的作用是告诉Dalvik虚拟机此C库使用的是哪一个JNI版本，如果你的库里面没有写明JNI_OnLoad()函数，VM会默认该库使用最老的JNI 1.1版本

## JNI开发流程的步骤
1. 在Java中先声明一个native方法
2. 编译Java源文件javac得到.class文件
3. 通过javah -jni命令导出JNI的.h头文件
4. 使用Java需要交互的本地代码，实现在Java中声明的Native方法（如果Java需要与C++交互，那么就用C++实现Java的Native方法。）
5. 将本地代码编译成动态库(Windows系统下是.dll文件，如果是Linux系统下是.so文件，如果是Mac系统下是.jnilib)
6. 通过Java命令执行Java程序，最终实现Java调用本地代码。
## 编译
使用 NDK 编译代码主要有三种方法：
- CMake(最新推荐)
    - 从 AS 2.2 之后便开始采用 CMake 的这种方式来构建. 在CMakeLists.txt文件夹中运行如下命令编译出*.so文件
    - cmake编译的会自动放入jniLibs，如果已经存在这个目录则冲突，解决办法把jniLibs目录设为空或指向其他目录也行，只要不要和CMake输出目录重合，或者配置打包规则，有冲突选择就第一个最为打包内容
        ```
        // https://blog.csdn.net/lbcab/article/details/72771729
        sourceSets {
                main {
                    jniLibs.srcDirs = []
                }
            }
        //or 
        packagingOptions {
            pickFirst "**/libJniTest.so"
        }
        ```
    ```
        cmake \
        -DCMAKE_TOOLCHAIN_FILE=$ANDROID_NDK/build/cmake/android.toolchain.cmake \
        -DANDROID_ABI=x86
        -DANDROID_PLATFORM=android-19
        make
    ```
- 基于 Make 的 ndk-build。
    - create `Android.mk`&`Application.mk`
    - run`ndk-build`
- 独立工具链，用于与其他编译系统集成，或与基于 configure 的项目搭配使用。
    这里分是否>=NDK r19，如果比较新的ndk，直接使用`$ANDROID_NDK/toolchains/llvm/prebuilt/darwin-x86_64/bin/`中的工具
    否则先运行: `$NDK/build/tools/make_standalone_toolchain.py --arch arm --api 21 --install-dir /tmp/my-android-toolchain`生成一套工具
## Android 添加so库
https://blog.csdn.net/longmeifeng/article/details/51353407
## 加载
`System.loadLibrary` vs `System.load` 前者动态加载，后者必须是jvm path里面的
java里面的class full name 必须跟jni里面的方法名匹配