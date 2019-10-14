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

## echo
#### echo格式控制
- 参数`-e`
    ```
    要支持同C语言一样的\转义功能，只需要加上参数-e
    字背景颜色范围:40----49 
    字颜色:30-----------39 
    str="kimbo zhang"
    echo -e "\033[30m ${str}\033[0m"      ## 黑色字体
    echo -e "\033[31m ${str}\033[0m"      ## 红色
    echo -e "\033[32m ${str}\033[0m"      ## 绿色
    echo -e "\033[33m ${str}\033[0m"      ## 黄色
    echo -e "\033[34m ${str}\033[0m"      ## 蓝色
    echo -e "\033[35m ${str}\033[0m"      ## 紫色
    echo -e "\033[36m ${str}\033[0m"      ## 青色
    echo -e "\033[37m ${str}\033[0m"      ## 白色
    ```
- 参数`-n`:取消echo后面的`\n`
  `echo "str" | base64` 将字符串str+换行 编码为base64字符串输出, 也可以用`\x00`两位16进制表示.
  - `echo "This is \x30"`输出`This is 0` (0的ASCII码为48)， 只在Mac下支持，并且必须引号
- 随机数:`head -c 32 /dev/urandom | base64`