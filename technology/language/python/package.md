# package
## egg (introduced by setuptools in 2004)
- 打包 
```setup.py
from setuptools import setup, find_packages
setup(
    name = "mymath",
    version = "0.1",
    packages = find_packages()
    )
```
`python setup.py bdist.egg`
- 安装
`easy_install *.egg`
- 删除
编辑`$python_path/Lib/site-packages/easy-install.pth`里面
## Wheel(format was introduced by PEP 427 in 2012)


