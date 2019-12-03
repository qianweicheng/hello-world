# expect
一个自动化shell交互框架
https://linux.die.net/man/1/expect
## concept
- spawn
- expect
- send
- set
- interact：允许用户交互
## install
`brew install expect`, `yum install expect` or `apt-get install expect`
## expect最常用的语法(tcl语言:模式-动作) 
- 单一分支模式语法： 
        expect “hi” {send “You said hi\n"}           匹配到hi后,会输出“you said hi”，并换行

- 多分支模式语法: 
    expect "hi" { send "You said hi\n" } \ "hehe" { send “Hehe yourself\n" } \ "bye" { send “Good bye\n" } 
- 匹配hi,hello,bye任意字符串时,执行相应输出.等同如下:
    expect { 
        "hi" { send "You said hi\n"} 
        "hehe" { send "Hehe yourself\n"} 
        "bye" { send “Good bye\n"} 
    } 
- expect脚本必须以interact或expect eof结束
- 设置expect超时
```
    set timeout -1  // 永不
    set timeout 300 // 300秒超时
```
- 一条Tcl命令由空格分割的单词组成.  第一个单词是命令名称, 其余的是命令参数
cmd arg arg arg
- 接收返回值：expect_out
```
set results $expect_out(buffer) # 当前匹配的和上一次未匹配的
$expect_out(0, string) # 当前匹配的
$expect_out(1, string) # 第一个正则组内
# 如果添加了-indices
expect -indices -re "b(b*).*(k+)"
set expect_out(0,start) 1 # 当前匹配的start索引
set expect_out(0,end) 10 # 当前匹配的end索引
```
