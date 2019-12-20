#!/usr/bin/env bash
# getopts对输入参数进行处理的几种方法：
# `getopts :ahf:gv OPTION`
# 几个特殊变量:
# OPTIND: 从1开始， 跟$1有不同，./xxx.sh -f a 当解析到a的时候为3
# OPTION: 自定义变量
# OPTARG: 带参数的值
# 选项参数的格式必须是-d val，而不能是中间没有空格的-dval。不支持长选项， 也就是--debug之类的选项
# 前面带冒号隐藏错误信息，后面带冒号表示带参数
# shift $((OPTIND-1))
# 所有不认识的变量都放 ? 里面，*就走不到
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
echo ext params: $*