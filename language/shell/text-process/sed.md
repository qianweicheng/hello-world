# sed
## mac sed vs gnu-sed
```
# Install gnu-sed using Homebrew
# The `--with-default-names` option configures `sed` to use gnu-sed
# Without that option, you'll need to type `gsed` to use gnu-sed
brew install --default-names gnu-sed 

# Verify which version of sed is used when you run the `sed` command
#  OK:  /usr/local/bin/sed
#  BAD: /usr/local/bin/gsed 
# If BAD, run `brew uninstall gnu-sed`, then reinstall with `--with-default-names`
```
## sed vs awk
sed擅长取行，awk命令擅长取列
sed会一次处理一行内容。处理时，把当前处理的行存储在临时缓冲区中，成为"模式空间"，接着用sed命令处理缓冲区中的内容，处理完成后，把缓冲区的内容送往屏幕。接着处理下一行，这样不断重复，直到文件末尾。文件内容并没有改变，除非你使用重定向存储输出。
sed 有两个内置的存储空间：
- 模式空间：模式空间用于 sed 执行的正常流程中。该空间 sed 内置的一
个缓冲区，用来存放、修改从输入文件读取的内容。
- 保持空间：保持空间是另外一个缓冲区，用来存放临时数据。Sed 可以在保持空间
和模式空间交换数据，但是不能在保持空间上执行普通的 sed 命令
`sed [options] [address]command`
## Flag
-n ：只打印模式匹配的行,一般跟`p`结合
-e ：直接在命令行模式上进行sed动作编辑，此为默认选项
-f ：将sed的动作写在一个文件内，用–f filename 执行filename内的sed动作
-r ：支持扩展表达式
-i ：直接修改文件内容
## 模式空间(pattern space)
p 打印匹配行（和-n选项一起合用）
a\ 在定位行号后插入新文本信息: `sed '/100/'a\ "new line" hello.txt`
i\ 在定位行号前插入新文本信息: `sed '/100/'i\ "new line" hello.txt`
c\ 用新文本替换定位文本: `sed '/100/'c\ "new line" hello.txt`
s 使用替换模式替换相应模式：`sed 's/old/new/flag'` flag有四种：数字,g,p,w
q 第一个模式匹配完成后退出或立即退出
{} 在定位行执行的命令组，用分号隔开
w  写入文件: `sed '1,10w a.txt' file.txt`
y 传送字符，替换单个字符: `sed 'y/123/789/' file.txt` 把字符1替换成7...
= 添加行号
## 保持空间(hold space)
n 读取下一行替换当前模式空间的行, 然后执行后续命令
N 读取下一行，追加到模式空间行后面，然后执行后续命令
d 删除当前模式空间所有内容
D 删除模式空间第一行到\n
p 打印当前模式空间所有内容
P 打印当前模式空间第一行(\n分割)
h 把模式空间的内容复制到保留空间，覆盖模式
H 把模式空间的内容追加到保留空间，追加模式
g 把保留空间的内容复制到模式空间，覆盖模式
G 把保留空间的内容追加到模式空间，追加模式
x 将暂存空间的内容于模式空间里的当前行互换。
! 对所选行取反。
& 表示前面的正则匹配group:`sed 's/.at/"&"/g'`  将前面匹配到的单词加引号
## 使用地址
- 数字+$ 形式表示行区间
- 正则过滤
## 案例
```
删除: `sed '2d' test.txt`
删除: `sed '2,$d' test.txt`
删除空行: `sed '/^$/d' test.txt`
替换行: `sed -n '1,20s/old/new/gp' test.txt`
替换块: `sed '2,5c No 2-5 number test.txt` # 将2-5行替换成`No 2-5 number`
命令组: `sed -n '/weicheng/{s/weicheng/root/;p;q}' access.log`
添加: `sed -e 4a\newline test.txt`  在第四行添加
第一个字母大写: echo foo | sed -e "s/\b\(.\)/\u\1/g"
每行后面添加个空行: sed G access.log
每两行添加个空行: sed 'n;G;' access.log 
将文件倒序: sed '1!G;h;$!d' file
```