# ps
http://man7.org/linux/man-pages/man1/ps.1.html
显示所有进程: -A -a -e -d
控制是否显示包含终端的进程，一般跟A参数配合：-X -x
-c 显示command的简化模式
查看特定id的进程: -G -g [进程组ID]  -p [进程ID]
打印线程信息: -M
排序: -m 内存 -r CPU
只显示某个用户的: -U -u