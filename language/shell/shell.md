# Shell
## 常用命令
- 空命令
    shell里面的空语句必须使用`:` 填充
- case 双分号结束
- 算数
    - $[]:     用于整数运算,基本的文本和算数运算 #i=$[i-1]  sh 不兼容  
    - [[]]:    扩展的文本和算数运算 #sh 不兼容  
    - (()):    C语言风格的算数运算, a=$((b+1))
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
- split
```Option1
string="hello,shell,split,test"  
array=(${string//,/ })  
 
for var in ${array[@]}
do
   echo $var
done 
```
```Option2
string="hello,shell,split,test"  
array=(`echo $string | tr ',' ' '` )  
 
for var in ${array[@]}
do
   echo $var
done 
```
## test 标签
-z:字符串的长度为零
-n:字符串的长度非零
–b:文件存在并且是块设备文件
–c:文件存在并且是字符设备文件
–d:文件存在并且是目录
–e:文件存在
–f:文件存在并且是正规文件
–g:文件存在并且是设置了组ID
–G:文件存在并且属于有效组ID
–h:文件存在并且是一个符号链接（同-L）
–k:文件存在并且设置了sticky位
–b:文件存在并且是块设备文件
–L:文件存在并且是一个符号链接（同-h）
–o:文件存在并且属于有效用户ID
–p:文件存在并且是一个命名管道
–r:文件存在并且可读
–s:文件存在并且是一个套接字
–t:文件描述符是在一个终端打开的
–u:文件存在并且设置了它的set-user-id位
–w:文件存在并且可写
–x:文件存在并且可执行