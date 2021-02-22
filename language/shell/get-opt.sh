#!/bin/bash  
#本脚本使用了gnu-getopt工具，getopt有两个版本，MacOS 默认安装BSD-getpot，
#如果在MacOS上运行，请运行:brew install gnu-getopt; brew --link gnu-getopt;

#定义选项， -o 表示短选项 -a 表示支持长选项的简单模式(以 - 开头) -l 表示长选项   
# a 后没有冒号，表示没有参数  
# b 后跟一个冒号，表示有一个必要参数  
# c 后跟两个冒号，表示有一个可选参数(可选参数必须紧贴选项)  
# -n 出错时的信息  
# -- 也是一个选项，比如 要创建一个名字为 -f 的目录，会使用 mkdir -- -f ,  
#    在这里用做表示最后一个选项(用以判定 while 的结束)  
# $@ 从命令行取出参数列表(不能用用 $* 代替，因为 $* 将所有的参数解释成一个字符串  
#                         而 $@ 是一个参数数组)  
set -e
#-----------------------------------------------------------------------  
# FUNCTION: usage  
# DESCRIPTION:  Display usage information.  
#-----------------------------------------------------------------------  
usage() {  
    cat << EOF  
  
Usage : 
  -h, --help                    Display this message  
  -s, --start                   Start the instance
  -S, --stop                    Stop the instance
Example:  
  1) xxxxxxx
EOF
}
if [ $# -eq 0 ]; then usage; exit 1; fi  

RET=`getopt -o hs:S:c:: -al help,start:,stop:,cherry:: -n "error message" -- "$@"` 
# 判定 getopt 的执行时候有错，错误信息输出到 STDERR  
if [ $? != 0 ];then  
    echo "Terminating....." >&2  
    exit 1  
fi

# 重新排列参数的顺序  
# 使用eval 的目的是为了防止参数中有shell命令，被错误的扩展
# set 会重新排列参数的顺序，也就是改变$1,$2...$n的值，这些值在getopt中重新排列过了
# echo RET:"$RET"  
eval set -- "$RET"  
  
# 处理具体的选项  
while [ -n "$1" ];do
    case "$1" in  
        -h | --help ) usage; exit 1;;  
        -s | --start | -start)    
            echo $2
            shift 2;;  
        -S | --stop | -stop)  
            echo $2
            shift 2;;
        -c | --cherry | -cherry)  
            case "$2" in  
                "") # 选项 c 带一个可选参数，如果没有指定就为空  
                    echo "option c, no argument"  
                    shift 2;;  
                *)  
                    echo "option c, argument $2"  
                    shift 2;;  
            esac  
            ;;  
        --) shift;break;;  
        *)  echo "Internal error!$1";exit 1;;  
        esac  
  
done  
  
#显示除选项外的参数(不包含选项的参数都会排到最后)， For 语言省略了in，就是对$@进行循环
for other_arg do  
   echo '--> '$other_arg ;
done
