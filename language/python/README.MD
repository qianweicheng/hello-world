# Python
## 安装
- python3
  - yum: `yum install python3` or `yum install python-setuptools`
  - brew: `brew install python3`
  - apt: `apt-get install -y python3 python3-distutils python-setuptools`
- 对于需要c/c++编译的则添加:
  - ubuntu: `python-dev/python3-dev`
  - centos: `python-devel/python3-devel`
- pip
    `wget https://bootstrap.pypa.io/get-pip.py && python3 get-pip.py`
    `easy_install install pip`
    下载了源代码: `python setup.py install`
    这种方法会将pip安装到对应python的site-packages中
## Mac下三个版本:
- 系统自带:`/System/Library/Frameworks/Python.framework` site-packages: `/Library/Python`
- 官网下载安装:`/Library/Frameworks/Python.framework/Versions`
- HomeBrew: `/usr/local/Cellar/python`(不自带pip)
- Windows下载安装也不自带pip
## virtualenv
- 安装虚拟环境：`pip install virtualenv`
- 创建虚拟环境: `virtualenv -p python3 venv`
    --no-site-packages 表示不复制当前环境的包，可以创建个干净的环境
    -p 表示使用的python版本
- 进入虚拟环境: `source venv/bin/activate`
- 退出虚拟环境: `deactivate`
## 运行
- 直接启动是把脚本所在的目录加入sys.path属性中
  `python xxx.py`
- 模块启动是把当前工作目录加入sys.path属性中, 该模块可以不需要__init__.py文件
  `python -m activity.mumu_stat`
- 设置`PYTHONPATH`环境变量等效与在`sys.path`中加入
    主意python3.6中，可以`PYTHONPATH=xxx;python xxx.py` or `export PYTHONPATH=xxx;python xxx.py`
    主意python3.7中，必须`export PYTHONPATH=xxx;python xxx.py`

## Python 内存分析
- 查看进程占用的堆内存大小: `pmap -x pid`
- gc: python 内置模块, 函数少功能基本, 使用简单, 作为python开发者里边的内容必须过一遍
- **tracemalloc**: 可以直接看到哪个(哪些)对象占用了最大的空间, 这些对象是谁, 调用栈是啥样的
- objgraph: 可以绘制对象引用图, 对于对象种类较少, 结构比较简单的程序适用, 我这个一个库套一个库, 内存还用的这么多,
    - 添加依赖：objgraph 
    - `yum install graphviz` or `brew install graphviz`
    -  注入代码
    ```
    objgraph.show_most_common_types()
    objgraph.show_backrefs(random.choice(objgraph.by_type('Foo')), filename='./edi-volume/refs.png')
    objgraph.show_refs(d, filename='./edi-volume/sample-graph.png')
    ```
- memory_profiler:
    @profile 标注函数， 可以打印每一步消耗的内存
- psutil
    ```
    def memory_usage_psutil():
    # return the memory usage in MB
    import psutil,os
    process = psutil.Process(os.getpid())
    mem = process.memory_info()[0] / float(2 ** 20)
    return mem
    ```
- guppy: 可以对堆里边的对象进行统计（木有成功过）   
- pympler: 可以统计内存里边各种类型的使用, 获取对象的大小
## 内存
- Python GC主要使用引用计数（reference counting）来跟踪和回收垃圾。
- 在引用计数的基础上，通过“标记-清除”（mark and sweep）解决容器对象可能产生的循环引用问题。
- 通过“分代回收”（generation collection）以空间换时间的方法提高垃圾回收效率。