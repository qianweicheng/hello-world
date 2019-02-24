# Sed-Awk
## sed
sed会一次处理一行内容。处理时，把当前处理的行存储在临时缓冲区中，成为"模式空间"，接着用sed命令处理缓冲区中的内容，处理完成后，把缓冲区的内容送往屏幕。接着处理下一行，这样不断重复，直到文件末尾。文件内容并没有改变，除非你使用重定向存储输出。
删除: `sed '2d' test.txt`
删除: `sed '2,$d' test.txt`
删除空行: `sed '/^$/d' test.txt`
替换: `sed -n '1,20s/old/new/gp' test.txt`
-n: 静默，一般跟`p`结合
1,20:行范围，可选
a: 新增，目前的下一行
c: 取代
d: 删除
g:全替，/Ng, 第几个开始替
i: 插入，目前的上一行
p:打印当前
s:替换
## awk
awk [-F|-f|-v] 'BEGIN{} //{command1; command2} END{}' file
NF          字段数量变量
NR          每行的记录号，多文件记录递增
RS       输入的记录分隔符,默认回车
FS(-F)   输入域分隔符，默认为一个空格,BEGIN时定义分隔符
OFS   输出域分隔符,默认空格:`{print $1,$2}`
ORS   输出记录分隔符 
-f 脚本文件
#### 示例
`awk 'BEGIN{FS=":"; OFS="\t"; ORS="\n\n"}{print $1} test.txt`
`awk -F ":" '$3 > 100' /etc/passwd`
`cat xxx.txt | awk '$1~/^abc/{print $0}'`=`awk -F: '{if($1~/^abc/) print $1}' xxx.txt`
逻辑&&: `awk -F ":" '$1~/mail/ && $3>8 {print }' xxx.txt`
`awk -F":" '$1=="mysql"{print $3}'` = `awk -F":" '{if($1=="mysql") print $3}'`