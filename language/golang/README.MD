# golang
## 安装
参考: https://golang.org/doc/install
`tar -C /usr/local -xzf go$VERSION.$OS-$ARCH.tar.gz`
如果默认安装的话：只需要设置下path
```
   export PATH=$PATH:/usr/local/go/bin
```
如果安装到其他目录的话，就需要设置GOROOT
```
   export GOROOT=$HOME/go1.X
   export PATH=$PATH:$GOROOT/bin
```
## 包管理
### 包下载
- go get: 是是下载包，不做任何管理
### 包版本管理
- glide(glide.yml): 会将所有依赖平铺到顶层的vender目录
   安装 `curl https://glide.sh/get | sh` 或 `brew install glide`
   - glide create/init：初始化
   - glide get xxx：添加依赖库
   - glide install:根据glide.yml安装
- Godeps(Godeps.json)
- dep
- govender
- godep: 第三方(go get github.com/tools/godep)
- vender机制: 1.5开始
- go module(官方): 1.11开始
## go module
如果有go.mod，则在每次编译的时候会自动更新
命令|说明
-|-
download|download modules to local cache (下载依赖包)
edit|edit go.mod from tools or scripts (编辑go.mod)
graph|print module requirement graph (打印模块依赖图)
init|initialize new module in current directory (在当前目录初始化mod)
tidy|add missing and remove unused modules (拉取缺少的模块，移除不用的模块)
vendor|make vendored copy of dependencies (将依赖复制到vendor下)
verify|verify dependencies have expected content (验证依赖是否正确)
why|explain why packages or modules are needed (解释为什么需要依赖)
开始:
- `go mod init`
- `go list -m -u all`
- `go get -u`
### 镜像
  - `export GOPROXY=https://goproxy.cn`
  - `go env -w GOPROXY=https://goproxy.cn,direct`
  - `go env -w GOPROXY="https://proxy.golang.org,direct"`  
### go.mod文件
- module 语句指定包的名字（路径）
- require 语句指定的依赖项模块
- replace 语句可以替换依赖项模块
- exclude 语句可以忽略依赖项模块
## go查找依赖包路径的规则如下：
1. 当前包下的vendor目录。
2. 向上级目录查找，直到找到src下的vendor目录。
3. 在GOPATH下面查找依赖包。
4. 在GOROOT目录下查找
5. 标准包的源码位于`$GOROOT/src/`下面
6. 自定义的包和第三方包的源码放到`$GOPATH/src`
## vendor
go在1.5版本引入了vendor属性(默认关闭，需要设置go环境变量GO15VENDOREXPERIMENT=1)，并在1.6版本中默认开启了vendor属性。在使用vendor中，给出如下建议：
- 一个library库工程（不包含main的package）不应该在自己的版本控制中存储外部的包在`vendor`目录中，除非他们有特殊原因并且知道为什么要这么做。
- 在一个app应用中,（包含main的package），建议只有一个vendor目录在代码库一级目录。
## Language
- 除了new创建的，都是值类型；make创建出来的也一样，只不过其底层捂住了一个指针
- make用于创建map,slic,channel,slic为指针
- Go语言和C语言一样，类型都是基于值传递的。要想修改变量的值，只能传递指针
- 在Go语言中没有构造函数的概念，一般使用工厂方法
  rect1 := new(Rect)
  rect2 := &Rect{}
- 初始化
  - 每个包的变量
  - 每个包的init函数
  - main包的main入口
## 命令行
- go build
- go clean
- go run
- go fmt
- go install/go get
- go test
- go pprof
## “避坑”与技巧
- 接口与nil不相等(Faq. https://golang.org/doc/faq#nil_error)
This situation can be confusing, and arises when a nil value is stored inside an interface value such as an error return:
```
func returnsError() error {
	var p *MyError = nil
	if bad() {
		p = ErrBad
	}
	return p // Will always return a non-nil error.
}
```
- 跨平台
```
set GOARCH=amd64     //设置目标可执行程序操作系统构架，包括 386，amd64，arm
set GOOS=linux       //设置可执行程序运行操作系统，支持 darwin，freebsd，linux，windows
go build ./main.go       //打包
```