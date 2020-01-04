# File
0 标准输入
1 标准输出
2 标准错误
## 输出
command > file.log 标准输出到file.log
command 1> file.log 同上
command 2>&1 1> file.log  标准输出和标准错误到file.log
command &> file.log 同上
## 输入
- 本来需要从键盘获取输入的命令会转移到文件读取内容，注意 "<"只能从文件中读取输入 `command < file.txt`
```
```
- Here Documents:用来将输入重定向到一个交互式 Shell 脚本或程序。
```
command << delimiter
    document
delimiter
```
```Example
cat << EOF >> file.txt

EOF
```
- Here Strings:`command <<< file.txt`,普通字符串
```
echo 123 | base64
等价
base64 <<< 123
```