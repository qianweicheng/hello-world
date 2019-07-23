#Linux进程查看及管理的工具
- ps: `apt-get update && apt-get install -y procps`
    Print a process tree: ps -ejH, ps axjf
    To get info about threads: ps -eLf, ps axms
    Simple Process Selection：
        -A, -N, T, -a, a[BSD], -d, -e, g, r, x[BSD]
    Process Selection By List:
        -C,-G, U, -U, -g, p, -p, q, -q, -s, t, -t ,-u, --pid, --ppid, --sid, -123=--sid 123, 123=--pid 123, xxx
    Output Format Control:
        -F, -O, O, -M, X, Z, -c, -f, j, -j, l, -l, o, -o, s, u, v, -y, -Z
    Output Modifiers:
        -H, N, O, S, c, e, f, h, k, -n, n, -w, w, ...
    Thread Display:
        H, -L, -T, m, -m
    Other Information:
        L, -V, V --help, --info --version
- pstree: 树状结构显示进程
- pidof:根据进程名查询进程ID
- pgrep,pkill:过滤
- top
- htop: 进程树`htop t`
- atop: 一个用来查看Linux系统负载的交互式监控工具
- pmap: 显示进程的内存布局`pmap xxx`
- vmstat: 虚拟内存状态工具---经典
- nice: 进程优先级调整,动态范围[-20,19]，静态优先级：[100-139]，数字越小，优先级越高
- glance
- dstat
- pkill,支持部分名字查询
- killall，名字全匹配

####内存CPU查看
- pmap pid
- top -p xxx
- ps -ef
    UNIX 风格，选项可以组合在一起，并且选项前必须有“-”连字符
    BSD 风格，选项可以组合在一起，但是选项前不能有“-”连字符
    GNU 风格的长选项，选项前有两个“-”连字符
- cat /proc/xxx/status