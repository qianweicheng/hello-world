# 常用命令
## 获取脚本当前目录
- 支持软连接的版本
```
SOURCE="$0"
while [ -h "$SOURCE"  ]; do
    DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
    SOURCE="$(readlink "$SOURCE")"
    [[ $SOURCE != /*  ]] && SOURCE="$DIR/$SOURCE" 
done
DIR="$( cd -P "$( dirname "$SOURCE"  )" && pwd  )"
echo $DIR # 当前脚本的物理文件夹
echo $SOURCE # 当前脚本的绝对地址
```
- 不支持软链接的版本
```
dirname=$(dirname $0)
```
- 获取父目录名
`basename $PWD`
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
## 获取本机ip快捷方式
```
$ host $(hostname) | awk '{print $4}'
```
