对输入参数进行处理的几种方法：
1,getopts :ahf:gv OPTION 
    1.1.选项参数的格式必须是-d val，而不能是中间没有空格的-dval。
    1.2.所有选项参数必须写在其它参数的前面，因为getopts是从命令行前面开始处理，遇到非-开头的参数，或者选项参数结束标记--就中止了，如果中间遇到非选项的命令行参数，后面的选项参数就都取不到了。
    1.3.不支持长选项， 也就是--debug之类的选项
    1.4.前面带冒号隐藏错误信息，后面带冒号表示带参数
    echo 处理完参数后的 OPTIND：$OPTIND
    echo 移除已处理参数个数：$((OPTIND-1))
    shift $((OPTIND-1))

2,shift
3,getopt, 一般跟shift组合
    后没有冒号，表示没有可以参数
    后跟一个冒号，表示有一个必要的参数  
    后跟两个冒号，表示有一个可选的参数（参数必须紧挨着选项） 

getopts变量： OPTIND，OPTARG
while abc OPTION;do
#case 双分号结束
case $OPTION in 
    a) ALL=true 
    echo "ALL is $ALL" 
    ;; 
    *)
    echo "======"
    ;;
esac