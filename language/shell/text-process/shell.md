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
${string:start:length}: 子字符串
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