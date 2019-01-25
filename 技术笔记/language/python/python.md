# Python
#### 源代码发布
1. 可以用pip导出你的dependency:
    `pip freeze > requirements.txt`
2. 然后在通过以下命令安装dependency:
    `pip install -r requirements.txt`
#### 二进制发布
1. Install PyInstaller from PyPI:
    `pip install pyinstaller`
2. Go to your program’s directory and run:
    `pyinstaller yourprogram.py`
3. 下载了wheel，egg等
    `pip install ./xxx.egg`
#### virtualenv
- 安装虚拟环境：`pip install virtualenv`
- 创建虚拟环境: `virtualenv --no-site-packages venv [python=python3.6(version)]`
    --no-site-packages 表示不复制当前环境的包，可以创建个干净的环境
- 进入虚拟环境: `source venv/bin/activate`
- 退出虚拟环境: `deactivate`
设置:PYTHONPATH环境变量
#### 源码安装
setup.py 帮助你纪录安装细节方便你卸载
    `python setup.py install`
    `python setup.py install --record log` #这时所有的安装细节都写到 log 里了
想要卸载的时候 `cat log ｜ xagrs rm －rf` 就可以干净卸载了

#### 子类调用父类
- 直接调用法：Student.__init__(self,name)
- 通过super方式：super(child_class, child_object).parent_attribute(arg)
其中child_class, child_object可以省略，super().parent_attribute(arg)

#### Class
__dir__ 返回属性列表
函子：__call__
上下文管理器：With
修饰器
支持多继承
__slots__
生成器(yield)其实是一种特殊的迭代器(__iter__(),__next__())
生成器表达式(generator expression): (x*x for x in range(10))
__getattribute__()一定调用，性能损失>具体属性>__getattr__()如果未找打则调用
#### Python 调用外部程序
- os.system(cmd)  打印日记并且返回一个16位的二进制数，低位为杀死所调用脚本的信号号码，高位为脚本的退出状态码,一般使用n >> 8 获取
- os.popen(cmd)   返回值是脚本执行过程中的输出内容
- 安装第三方库`commands`. (status, output) = commands.getstatusoutput(cmd), status和第一种方式一样需要`>>8`
#### Python 内存分析
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