# Shell
## 常用命令
- 空命令
    shell里面的空语句必须使用`:` 填充
- shell运行的目录
    以当前运行shell的目录作为工作目录，而不是脚本(或者软连接)所在目录， 需要获得脚本所在目录
- exec: shell的内建命令exec将并不启动新的shell，而是用要被执行命令替换当前的shell进程，并且将老进程的环境清理掉，而且exec命令后的其它命令将不再执行。
- case 双分号结束
- 算数
    - []:      基本的文本和算数运算 #i=$[i-1]  sh 不兼容  
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
## 数组
- 定义: 
    arr=(1 2 3)
    或者
    array_name[0]=value0
    array_name[1]=value1
    array_name[2]=value2
- 获取: ${arr[0]}
- 数组长度: ${#arr[@]}
- 打印所有: ${arr[@/*]}

## 命令替换
()      命令组，开启一个新的shell运行，兼容性较``差
``      命令组，开启一个新的shell运行，兼容性较好
$()     将() 运行的结果替换
$``     同上
{}      命令组， 前面有空格，最后得有分号,在本shell里执行
${}     变量替换
## 变量替换
假设我们定义了一个变量为：
file=/dir1/dir2/dir3/my.file.txt
可以用${ }分别替换得到不同的值：
${file#*/}： 删掉第一个/ 及其左边的字符串：dir1/dir2/dir3/my.file.txt
${file##*/}：删掉最后一个/  及其左边的字符串：my.file.txt
${file%/*}： 删掉最后一个/  及其右边的字符串：/dir1/dir2/dir3
${file%%/*}：删掉第一个/  及其右边的字符串：(空值)
${file:0:5}：提取最左边的5 个字节：/dir1
${file:5:5}：提取第5 个字节右边的连续5个字节：/dir2
${file/dir/path}：将第一个dir 替换为path：/path1/dir2/dir3/my.file.txt
${file//dir/path}：将全部dir 替换为path：/path1/path2/path3/my.file.txt
${#string}	$string的长度
${string:position}	在$string中, 从位置$position开始提取子串

记忆的方法为：
\# 是 去掉左边（键盘上#在 % 的左边）
%是去掉右边（键盘上% 在# 的右边）
单一符号是最小匹配；两个符号是最大匹配
利用${ } 还可针对不同的变数状态赋值(沒设定、空值、非空值)： 
${var}                                       变量var的值, 与$var相同
${var-DEFAULT}                               如果var没有被声明, 那么就以$DEFAULT作为其值 *
${var:-DEFAULT}                              如果var没有被声明, 或者其值为空, 那么就以$DEFAULT作为其值 *
${var=DEFAULT}                               如果var没有被声明, 那么就以$DEFAULT作为其值 *
${var:=DEFAULT}                              如果var没有被声明, 或者其值为空, 那么就以$DEFAULT作为其值 *
${var+OTHER}                                 如果var声明了, 那么其值就是$OTHER, 否则就为null字符串
${var:+OTHER}                                如果var被设置了, 那么其值就是$OTHER, 否则就为null字符串
${var?ERR_MSG}                               如果var没被声明, 那么就打印$ERR_MSG *
${var:?ERR_MSG}                              如果var没被设置, 那么就打印$ERR_MSG *
${!varprefix*}                               匹配之前所有以varprefix开头进行声明的变量
${!varprefix@}                               匹配之前所有以varprefix开头进行声明的变量

${file:?my.file.txt} ：若$file 没设定或为空值，则将my.file.txt 输出至STDERR。(非空值時不作处理)
${#var} 可计算出变量值的长度：
${#file} 可得到27 ，因为/dir1/dir2/dir3/my.file.txt 是27个字节
${!var} 动态变量名，变量名拼接
${!var@} 用于返回当前shell中，变量名以var开始的变量
## 字符串正则
[[ abc == a* ]];echo $?


## Shell快捷键
cd -    返回到前一个目录(上一个cd命令的目录）
open . 通过Finder 打开当前文件夹
go2shell 在Finder中开启一个命令行直接进入当前目录(App Store小程序)
ctrl + u 删除命令行光标前面的字符
ctrl + k 删除命令行光标后面的字符
ctrl + w 删除光标前面一个单词
ctrl + l  清屏，与目录clear等效
ctrl + a 将光标移动道最前面
ctrl + e 将光标移动道最后面
set -x 打开shell脚本的调试模式
set -e 当shell脚本产生错误立即退出( 默认行为是产生了错也继续执行)

## echo要支持同C语言一样的\转义功能，只需要加上参数-e
echo格式控制
字背景颜色范围:40----49 
字颜色:30-----------39 