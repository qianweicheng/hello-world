# 获取脚本当前目录
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
cd "$(dirname $0)/../.."
```