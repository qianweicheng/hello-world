#!/usr/bin/env bash
# getopts对输入参数进行处理的几种方法：
# `getopts :ahf:gv OPTION`
# 几个特殊变量:
# OPTIND: 从1开始， 跟$1有不同，./xxx.sh -f a 当解析到a的时候为3
# OPTION: 自定义变量
# OPTARG: 带参数的值
# 第一个冒号标示屏蔽getopts的错误信息，每个参数后面的冒号标示带参数
# 选项参数的格式必须是-d val，而不能是中间没有空格的-dval。不支持长选项， 也就是--debug之类的选项
# 所有选项参数必须写在其它参数的前面，因为getopts是从命令行前面开始处理，遇到非-开头的参数，或者选项参数结束标记--就中止了
# shift $((OPTIND-1))
# 所有不认识的变量都放?里面. *,? 都是通配符
if [ $# -gt 0 ];then
    while getopts :f:h OPTION;do
        case $OPTION in
            f)  echo $OPTIND opt:$OPTION value:$OPTARG;;
            h)  echo $OPTIND opt:$OPTION value:$OPTARG;;
            :)  echo "Missing argument for $OPTARG";;
            ?)  echo $OPTIND opt:$OPTION value:$OPTARG;;
            # *)  echo $OPTIND opt:$OPTION value:$OPTARG;;
        esac    
    done
    echo $OPTIND
    shift $(( $OPTIND-1 ))
else
    echo "no params"
fi
echo "ext params: $*"