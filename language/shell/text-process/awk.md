# awk
awk [-F|-f|-v] 'BEGIN{} //{command1; command2} END{}' file
### 内置变量
NF          字段数量变量
NR          每行的记录号，多文件记录递增
RS       输入的记录分隔符,默认回车
FS(-F)   输入域分隔符，默认为一个空格,BEGIN时定义分隔符
OFS   输出域分隔符,默认空格:`{print $1,$2}`
ORS   输出记录分隔符 
FNR 各文件分别计数的行号
FILENAME 当前文件名
ARGC：命令行参数的个数
ARGV：数组，保存的是命令行所给定的各参数
### 外部变量
awk -v name="egrep" "BEGIN{print name}"
awk 'BEGIN{name="egrep";print name}'  
### 示例
`awk 'BEGIN{FS=":"; OFS="\t"; ORS="\n\n"}{print $1} test.txt`
`awk -F ":" '$3 > 100' /etc/passwd`
`cat xxx.txt | awk '$1~/^abc/{print $0}'`=`awk -F: '{if($1~/^abc/) print $1}' xxx.txt`
逻辑&&: `awk -F ":" '$1~/mail/ && $3>8 {print }' xxx.txt`
`awk -F":" '$1=="mysql"{print $3}'` = `awk -F":" '{if($1=="mysql") print $3}'`
#### 输出格式化
- printf 必须显式的使用`\n`换行
- 单引号:`awk 'BEGIN {printf "单引号 \47"}'`
- 双引号:`awk 'BEGIN {printf "\""}'`
- 内置各种字符串函数
- `awk 'BEGIN {printf "%s->%s", $1, $2}'`