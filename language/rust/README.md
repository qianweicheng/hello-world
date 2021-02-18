# Rust
En:`https://doc.rust-lang.org/book/`
CN:`https://rust-lang.tw/book-tw` 简化中文版`https://kaisery.github.io/trpl-zh-cn/`
## Install
https://www.rust-lang.org/tools/install
这会把rust，cargo都安装到`~/.cargo/bin`里面,然后手动把期加入到环境变量`PATH`里面就可以。
## 包管理器Cargo
https://doc.rust-lang.org/cargo/reference/config.html
`cargo build -h`
## rust 生命周期三原则
- 为每个输入参数分配一个生命周期
- 如果只有一个输入的生命周期，则自动把这个生命周期赋给输出生命周期
- 如果输入有self参数，则输出参数也自动赋予self的生命周期