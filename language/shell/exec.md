# 执行外部程序:
sh,exec,source,fork,直接路径执行
## 比较
- sh是通过创建子进程(subshell)去执行脚本，父进程无法使用子进程中的变量，而子进程对环境变量的修改也不会影响到父进程。父进程中的局部变量子进程也无法使用，子进程会继承父进程的环境变量;
- exec: shell的内建命令exec将并不启动新的shell，而是用要被执行命令替换当前的shell进程，并且将老进程的环境清理掉，而且exec命令后的其它命令将不再执行。
- ​source或者“.”来调用外部脚本，不会产生新的进程，继承当前shell环境变量，而且被调用的脚本运行结束后，它拥有的环境变量和声明变量会被当前shell保留，类似将调用脚本的内容复制过来直接执行。执行完毕后原主shell继续运行。
- ​ 使用fork执行脚本的时候会创建一个子进程去执行该脚本，子进程会继承父进程的环境变量和声明变量。当子进程执行完毕后会返回父进程，但是父进程的环境变量不会因子进程的改变而改变。
- ​直接路径. 创建一个子进程去执行脚本(通sh发，唯一区别在于文件必须有执行权限)
## 判断命令是否存在
```
$ command -v foo >/dev/null 2>&1 || { echo >&2 "I require foo but it's not installed.  Aborting.";}
$ type foo >/dev/null 2>&1 || { echo >&2 "I require foo but it's not installed.  Aborting.";}
$ hash foo 2>/dev/null || { echo >&2 "I require foo but it's not installed.  Aborting.";}
```