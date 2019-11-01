# package
涉及到`pip, wheel, setuptools, easy_install`
- setuptools是一个用来打包egg，whell的工具包
- easy_install是用来安装egg的(只能安装包，不能卸载包)
- pip功能比较强大（包括了setuptools，easy_install，wheel等工具）
## egg vs whl
Wheel和Egg的主要的不同点：
Wheel有一个官方的PEP427来定义，而Egg没有PEP定义。
Wheel是一种分发格式，即打包格式。而Egg既是一种分发格式，也是一种 运行时安装的格式，并且是可以被import的。
Wheel文件不会包含.pyc文件
Wheel使用和PEP376兼容的.dist-info目录，而Egg使用.egg-info目录。
Wheel有着更丰富的命名规则。
Wheel是有版本的，每个Wheel文件都包含wheel规格的版本和打包它的实现。
Wheel在内部被sysconfig path type管理，因此转向其他格式也更容易。
## setup.py
无论是egg，还是whl,亦或是源码，都需要配置setup.py
```setup.py
from setuptools import setup, find_packages
setup(
    name = "mymath",
    version = "0.1",
    packages = find_packages()
    )
```
## 源码安装
### 常用命令
- build
- install
- sdist: 打包成zip，解压之后用install命令安装
- bdist_egg: 打包成egg
- bdsit_wheel: 打包成whl

setup.py 帮助你纪录安装细节方便你卸载
    `python setup.py install`
    `python setup.py install --record log` #这时所有的安装细节都写到 log 里了
想要卸载的时候 `cat log ｜ xagrs rm －rf` 就可以干净卸载了
## pip
- 使用proxy: `pip install requests -i https://pypi.douban.com/simple`
- 使用配置文件: `pip install -r requirements.txt`
## egg (introduced by setuptools in 2004)
- 打包: `python setup.py bdist_egg`
- 使用easy_install进行安装，安装pip时附带安装了: `easy_install *.egg`
- 删除
    - 编辑`$python_path/Lib/site-packages/easy-install.pth`里面
    - 然后删除egg文件夹即可
## Wheel(format was introduced by PEP 427 in 2012)
wheel文件本质上就是zip或者rar,只不过他更加方便python的安装以及使用
- 打包
    `python setup.py bdist_wheel`
- 安装
    `pip install XXX.whl`
- 卸载
    `pip uninstall xxx`

## 发布
### 源代码发布
1. 可以用pip导出你的dependency:
    `pip freeze > requirements.txt`
2. 然后在通过以下命令安装dependency:
    `pip install -r requirements.txt`
### 二进制发布
1. Install PyInstaller from PyPI:
    `pip install pyinstaller`
2. Go to your program’s directory and run:
    `pyinstaller yourprogram.py`
## 安装之后结构
- xxx.dist-info
- xxx.egg-info