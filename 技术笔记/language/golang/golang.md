#golang
##安装https://golang.org/doc/install
>tar -C /usr/local -xzf go$VERSION.$OS-$ARCH.tar.gz
如果默认安装的话：只需要设置下path
export PATH=$PATH:/usr/local/go/bin
如果安装到其他目录的话，就需要设置GOROOT
export GOROOT=$HOME/go1.X
export PATH=$PATH:$GOROOT/bin
##初始化
- make用于创建map,slic,channel,slic为指针
- 除了new创建的，都是值类型；make创建出来的也一样，只不过其底层捂住了一个指针
- Go语言和C语言一样，类型都是基于值传递的。要想修改变量的值，只能传递指针
- 在Go语言中没有构造函数的概念，一般使用工厂方法
  rect1 := new(Rect)
  rect2 := &Rect{}

##程序启动
1. 每个包的变量
2. 每个包的init函数
3. main包的main入口
##Faq. https://golang.org/doc/faq
This situation can be confusing, and arises when a nil value is stored inside an interface value such as an error return:
func returnsError() error {
	var p *MyError = nil
	if bad() {
		p = ErrBad
	}
	return p // Will always return a non-nil error.
}
##包管理
- go get
- glide(glide.yml): 会将所有依赖平铺到顶层的vender目录
   安装 `curl https://glide.sh/get | sh` 或 `brew install glide`
   - glide create/init：初始化
   - glide get xxx：添加依赖库
   - glide install:根据glide.yml安装
- Godeps(Godeps.json)
- dep(官方)
- govender
##vendor
go在1.5版本引入了vendor属性(默认关闭，需要设置go环境变量GO15VENDOREXPERIMENT=1)，并在1.6版本中默认开启了vendor属性。
##go查找依赖包路径的规则如下：
1. 当前包下的vendor目录。
2. 向上级目录查找，直到找到src下的vendor目录。
3. 在GOPATH下面查找依赖包。
4. 在GOROOT目录下查找
##在使用vendor中，给出如下建议：
- 一个library库工程（不包含main的package）不应该在自己的版本控制中存储外部的包在`vendor`目录中，除非他们有特殊原因并且知道为什么要这么做。
- 在一个app应用中，（包含main的package），建议只有一个vendor目录在代码库一级目录。