# Python
## Python Language
https://github.com/taizilongxu/interview_python
## 子类调用父类
- 直接调用法：Student.__init__(self,name)
- 通过super方式：super(child_class, child_object).parent_attribute(arg)
其中child_class, child_object可以省略，super().parent_attribute(arg)

## Class
__dir__ 返回属性列表
函子：__call__
上下文管理器：With
修饰器
支持多继承
__slots__
生成器(yield)其实是一种特殊的迭代器(__iter__(),__next__())
生成器表达式(generator expression): (x*x for x in range(10))
__getattribute__()一定调用，性能损失>具体属性>__getattr__()如果未找打则调用
## Python 调用外部程序
- os.system(cmd)  打印日记并且返回一个16位的二进制数，低位为杀死所调用脚本的信号号码，高位为脚本的退出状态码,一般使用n >> 8 获取
- os.popen(cmd)   返回值是脚本执行过程中的输出内容
- 安装第三方库`commands`. (status, output) = commands.getstatusoutput(cmd), status和第一种方式一样需要`>>8`
## 嵌入Python
https://docs.python.org/3.7/extending/embedding.html
## 与C交互
- ctypes（内置）
- swig（第三方）
- cython（功能强大）