# Shell
## 常用命令
- 空命令
    shell里面的空语句必须使用`:` 填充
- shell运行的目录
    以当前运行shell的目录作为工作目录，而不是脚本(或者软连接)所在目录， 需要获得脚本所在目录
- exec: shell的内建命令exec将并不启动新的shell，而是用要被执行命令替换当前的shell进程，并且将老进程的环境清理掉，而且exec命令后的其它命令将不再执行。
- case 双分号结束
- 算数
    - $[]:     用于整数运算,基本的文本和算数运算 #i=$[i-1]  sh 不兼容  
    - [[]]:    扩展的文本和算数运算 #sh 不兼容  
    - (()):    C语言风格的算数运算
    - expr:    $(expr $i - 1) #注意空格,$?返回值有坑，
    - let:     let I=8+4*5 #sh 不兼容
- For循环
    for循环省略了in之后就对位置参数进行循环
    for循环最好使用:
    ```
        for i in $(seq 0 $nodes_count);do
            xxxxx
        done
    ```
- 逻辑运算: &&,||, !
    - c风格
    if [ "$a" = 'a' ] || [ "$b" = 'b' ]
    if [ ! $n = 0 ] && [ ! $m = 0 ]
    - shell风格: -o = or , -a = and
    if [ $a -gt $b -o $a -lt $c ]
## 命令替换
()      命令组，开启一个新的shell运行，兼容性较``差
``      命令组，开启一个新的shell运行，兼容性较好
$()     将() 运行的结果替换
$``     同上
{}      命令组， 前面有空格，最后得有分号,在本shell里执行
${}     变量替换
## 文本
三种形式的区别: 
- 双引号: 需要转意的情况只能用这个
- 单引号: 不能有任何转意
- 无引号: 不能有空格
## 场景
- 文本拼接
单引号里面不能用变量，双引号可以
```
a="1"
b="2"
c='$a$b' # result: $a$b
c="$a$b" # result: 12
```
- 字符串处理:
```
可以用${}分别替换得到不同的值: 
${string#*/}:  删掉第一个`/`及其左边的字符串
${string##*/}: 删掉最后一个`/`及其左边的字符串
${string%/*}:  删掉最后一个`/`及其右边的字符串
${string%%/*}: 删掉第一个`/`及其右边的字符串
${string:start:length}`: 子字符串
${string:position}: 同上，length可以省略，在$string中, 从位置$position开始提取子串
${string/src/dst}: 将第一个src 替换为dst
${string//src/dst}: 将全部src 替换为dst
${#string}: $string的长度
${!var} 动态变量名，变量名拼接
${!var@} 用于返回当前shell中，变量名以var开始的变量
```
记忆的方法为: 
\# 是 去掉左边（键盘上#在 % 的左边）
%是去掉右边（键盘上% 在# 的右边）
单一符号是最小匹配；两个符号是最大匹配
## 利用${ } 还可针对不同的变数状态赋值(沒设定、空值、非空值):  
${var}                                       变量var的值, 与$var相同
${var-DEFAULT}                               如果var没有被声明, 那么就以$DEFAULT作为其值 *
${var:-DEFAULT}                              如果var没有被声明, 或者其值为空, 那么就以$DEFAULT作为其值 *
${var=DEFAULT}                               如果var没有被声明, 那么就以$DEFAULT作为其值 * 区别在于调用之后var被赋值了
${var:=DEFAULT}                              如果var没有被声明, 或者其值为空, 那么就以$DEFAULT作为其值 * 区别在于调用之后var被赋值了
${var+OTHER}                                 如果var声明了, 那么其值就是$OTHER, 否则就为null字符串
${var:+OTHER}                                如果var被设置了, 那么其值就是$OTHER, 否则就为null字符串
${var?ERR_MSG}                               如果var没被声明, 那么就打印$ERR_MSG *
${var:?ERR_MSG}                              如果var没被设置, 那么就打印$ERR_MSG *
${!varprefix*}                               匹配之前所有以varprefix开头进行声明的变量
${!varprefix@}                               匹配之前所有以varprefix开头进行声明的变量

${file:?my.file.txt} : 若$file 没设定或为空值，则将my.file.txt 输出至STDERR。(非空值時不作处理)


### 字符串正则
[[ abc == a* ]];echo $?
[[ abc =~ "^abc" ]];echo $?
## 数组
- 定义: 
    arr=(1 2 3)
    或者
    array_name[0]=value0
    array_name[1]=value1
    array_name[2]=value2
- 获取: ${arr[0]}
- 打印所有: ${arr[@/*]}
- 长度
```
${#array_name[@]}  
${#array_name[*]}
```
- 拼接
```
array_new=(${array1[@]}  ${array2[@]})
array_new=(${array1[*]}  ${array2[*]})
```
- 删除
```
unset array_name[index]
```
## 完整内建命令列表
命令|说明
-|-
:|扩展参数列表，执行重定向操作
.|读取并执行指定文件中的命令（在当前 shell 环境中）
alias|为指定命令定义一个别名
bg|将作业以后台模式运行
bind|将键盘序列绑定到一个 readline 函数或宏
break|退出 for、while、select 或 until 循环
builtin|执行指定的 shell 内建命令
caller|返回活动子函数调用的上下文
cd|将当前目录切换为指定的目录
command|执行指定的命令，无需进行通常的 shell 查找
compgen|为指定单词生成可能的补全匹配
complete|显示指定的单词是如何补全的
compopt|修改指定单词的补全选项
continue|继续执行 for、while、select 或 until 循环的下一次迭代
declare|声明一个变量或变量类型。
dirs|显示当前存储目录的列表
disown|从进程作业表中刪除指定的作业
echo|将指定字符串输出到 STDOUT
enable|启用或禁用指定的内建shell命令
eval|将指定的参数拼接成一个命令，然后执行该命令
exec|用指定命令替换 shell 进程
exit|强制 shell 以指定的退出状态码退出
export|设置子 shell 进程可用的变量
fc|从历史记录中选择命令列表
fg|将作业以前台模式运行
getopts|分析指定的位置参数
hash|查找并记住指定命令的全路径名
help|显示帮助文件
history|显示命令历史记录
jobs|列出活动作业
kill|向指定的进程 ID(PID) 发送一个系统信号
let|计算一个数学表达式中的每个参数
local|在函数中创建一个作用域受限的变量
logout|退出登录 shell
mapfile|从 STDIN 读取数据行，并将其加入索引数组
popd|从目录栈中删除记录
printf|使用格式化字符串显示文本
pushd|向目录栈添加一个目录
pwd|显示当前工作目录的路径名
read|从 STDIN 读取一行数据并将其赋给一个变量
readarray|从 STDIN 读取数据行并将其放入索引数组
readonly|从 STDIN 读取一行数据并将其赋给一个不可修改的变量
return|强制函数以某个值退出，这个值可以被调用脚本提取
set|设置并显示环境变量的值和 shell 属性
shift|将位置参数依次向下降一个位置
shopt|打开/关闭控制 shell 可选行为的变量值
source|读取并执行指定文件中的命令（在当前 shell 环境中）
suspend|暂停 Shell 的执行，直到收到一个 SIGCONT 信号
test|基于指定条件返回退出状态码 0 或 1
times|显示累计的用户和系统时间
trap|如果收到了指定的系统信号，执行指定的命令
type|显示指定的单词如果作为命令将会如何被解释
typeset|声明一个变量或变量类型。
ulimit|为系统用户设置指定的资源的上限
umask|为新建的文件和目录设置默认权限
unalias|刪除指定的别名
unset|刪除指定的环境变量或 shell 属性
wait|等待指定的进程完成，并返回退出状态码