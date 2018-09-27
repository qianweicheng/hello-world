https://golang.org/doc/install
tar -C /usr/local -xzf go$VERSION.$OS-$ARCH.tar.gz

如果默认安装的话：只需要设置下path
export PATH=$PATH:/usr/local/go/bin

如果安装到其他目录的话，就需要设置GOROOT
export GOROOT=$HOME/go1.X
export PATH=$PATH:$GOROOT/bin

https://golang.org/doc/faq
This situation can be confusing, and arises when a nil value is stored inside an interface value such as an error return:
func returnsError() error {
	var p *MyError = nil
	if bad() {
		p = ErrBad
	}
	return p // Will always return a non-nil error.
}