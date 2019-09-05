# 编译
https://github.com/python-cmake-buildsystem/python-cmake-buildsystem
各种跨平台方案：https://wiki.python.org/moin/Android
## Kivy
Kivy: https://kivy.org
https://kivy.org/doc/stable/gettingstarted/installation.html
#### Install
`pip install python-for-android`
p4a apk --private ~/work/kivy-test --package=org.example.myapp --name "My application" --version 0.1 --bootstrap=sdl2 --requirements=python3,kivy
## BeeWare
BeeWare: https://beeware.org/project/using/
#### voc
一个python 转 java 的项目
https://voc.readthedocs.io/en/latest/background/install.html
- 准备,生成`dist`中几个jar
```
    python3 -m venv env
    . env/bin/activate
    cd voc
    pip install -e .
    ant java
```
- 编译python 2 class
    `voc -v example.py`
- 运行
    `java -classpath ../voc/dist/python-java-support.jar:. python.example`
#### briefcase
https://briefcase.readthedocs.io/en/latest/background/quickstart.html
https://github.com/beeware/Python-Android-template/tree/3.6
```
    pip install briefcase
    pip install cookiecutter
```
```
    cookiecutter https://github.com/beeware/briefcase-template
    # 这会在当前目录创建一个helloworld文件夹，进入该文件夹然后
    python setup.py android -b
    python setup.py android -s
```
```
    cookiecutter https://github.com/pybee/Python-Android-template --checkout 3.6
    ./gradlew build
    ./gradlew run
```
## Python for Android
https://github.com/kivy/python-for-android
https://github.com/GRRedWings/python3-android

