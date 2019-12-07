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
GOROOT: Golang的安装目录
GOPATH: Used to specify directories outside of $GOROOT that contain the source for Go projects and their binaries.
## 包管理
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
- go module: (官方)1.11开始，最新推荐
- go get: 
## 依赖包管理方式
目前主流有两种模式:
- vender模式
  -  go 1.11, the vendor directories are only supported when $PWD is under $GOPATH
- modules模式(最新推荐)
  - A module is a collection of Go packages stored in a file tree with a go.mod file at its root.
  - 只寻找当前go.mod文件夹下，go.mod依赖和GOROOT下，不寻找GOPATH下的包

最新版本的golang，有`GO111MODULE`,`GOPATH`,`go.mod`三要素。
- Go 1.11
  - 打开了`GO111MODULE=on`，所有的go命令都会工作在module模式下，会存在对go.mod的依赖
  - 当前目录在GOPATH下的，则需要显示的设置`GO111MODULE=on`
  - 当前目录不在GOPATH下，则系统自动会进入modules模式
- Go 1.13 默认进入modules模式
### vendor模式
go在1.5版本引入了vendor属性(默认关闭，需要设置go环境变量GO15VENDOREXPERIMENT=1)，并在1.6版本中默认开启了vendor属性。在使用vendor中，给出如下建议：
- 一个library库工程（不包含main的package）不应该在自己的版本控制中存储外部的包在`vendor`目录中，除非他们有特殊原因并且知道为什么要这么做。
- 在一个app应用中,（包含main的package），建议只有一个vendor目录在代码库一级目录。
- 搜索顺序
  1. 当前包下的vendor目录
  2. 向上级目录查找，直到找到src下的vendor目录
  3. 在GOPATH下面查找依赖包，自定义的包和第三方包的源码
  4. 在GOROOT目录下查找标准包，位于`$GOROOT/src/`下面
### modules模式
环境变量`GO111MODULE`来控制依赖包的管理方式。当GO111MODULE的值为on时，那么就会使用modules功能，这种模式下，$GOPATH不再作为build时导入的角色，依赖包会存放在$GOPATH/pkg/mod目录下. 项目本身的包可以不在GOPATH下面。
### go module
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
### go.mod文件格式
- module 语句指定包的名字（路径）
- require 语句指定的依赖项模块
- replace 语句可以替换依赖项模块
- exclude 语句可以忽略依赖项模块
### 包仓库代理
  - `export GOPROXY=https://goproxy.cn`
  - `go env -w GOPROXY="https://goproxy.cn,direct"`
  - `go env -w GOPROXY="https://proxy.golang.org,direct"`  
## 命令行
- go clean
- go run
- go fmt
- go test
- go pprof
- go install
- go build: 
  - 编译`go build ./main.go` or `go build {module-name}` or `go build ./...`
  - module模式：`go build -mod [mode]` mode可用`readonly，release，vendor`
- go get：
  - `go get -u [./...]` 会更新主模块下的所有依赖包
- go mod
  - 所有的go命令中现在已经内置了对module的支持，而不仅仅是`go mod`
  - `go mod tidy`，用来查看和添加缺失的module需求声明以及移除不必要的
  - `go mod init`，初始化一个module管理文件
  - `go list -m -u all` 检查所有包的版本状态
  - `go mod vendor` 此命令会将build阶段需要的所有依赖包放到主模块所在的vendor目录中
  - `go mod verify`此命令会检查当前模块的依赖是否已经存储在本地下载的源代码缓存中

## 跨平台
```
set GOARCH=amd64     //设置目标可执行程序操作系统构架，包括 386，amd64，arm
set GOOS=linux       //设置可执行程序运行操作系统，支持 darwin，freebsd，linux，windows
```
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
