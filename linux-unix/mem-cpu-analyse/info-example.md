# Memory
## Case in docker
- /sys/fs/cgroup/memory/memory.stat
cache:          7263240192  6.76442G
rss:            2400301056  2.23545G
                cache+rss = 8.9999G
- /sys/fs/cgroup/memory/memory.usage_in_bytes   9663602688 = 8.9999G
- /sys/fs/cgroup/memory/memory.limit_in_bytes   9663676416 = 8.9999G
- top:          2.207g(主要进程) + 16M(其他进程) = 2.223G
- docker stats                                  2.235G

> 数据全部都对上了
## Case In node1
- free/top(/proc/meminfo + /proc/{pid}/status)
```
              total        used        free      shared  buff/cache   available
Mem:           3.9G        404M        1.0G        1.0M        2.4G        3.1G
                           0.395G 
```
- /sys/fs/cgroup/memory/memory.stat
```
cache           14446592    0.014G
rss             19230720    0.018G
                            =0.32G

total_cache     2355068928  2.193G
total_rss       278073344   0.259G
                           =2.452G

buff = free.(buff/cache) - memory.stat.(total_cache) = 2.4-2.2 = 0.2G
memory.usage_in_bytes = memory.stat.(totla_cache) + memory.stat.(total_rss)
                      ~= free.used + free.(buff/cache) - (buff)
                      = 0.395G + 2.4G - 0.2G = 2.595G
free.used ~= memory.stat.(total_rss) + buff = 0.26G + 0.2G = 0.46G(跟0.4G有误差)
```
- /sys/fs/cgroup/memory/memory.usage_in_bytes   2632024064 2.45G
- dockers in host

    docker|docker1|docker2|sum
    ------|-------|-------|---
    cache |2289664|1527808|3.6M
    rss   |2940928|4853760|7.4M
- /sys/fs/cgroup/memory/docker/memory.stat
- /sys/fs/cgroup/memory/docker/{docker-id}/memory.stat
## Case In node1
- free
              total        used        free      shared  buff/cache   available
Mem:            31G         13G        5.6G        6.1M         12G         17G
Swap:            0B          0B          0B
- /sys/fs/cgroup/memory/memory.usage_in_bytes   26132647936 24.338G
- /sys/fs/cgroup/memory/memory.stat
```
total_cache 11798220800 10.988G
total_rss   14336294912 13.352G  
buff = free.(buff/cache) - memory.stat.(total_cache) = 12-11 = 1G
memory.usage_in_bytes = memory.stat.(totla_cache) + memory.stat.(total_rss) = 24.33G
                      ~= free.used + free.(buff/cache) - (buff)
                      = 13G + 12G - 1G = 24G
free.used ~= memory.stat.(total_rss) + buff = 13.352G + 1G = 14.352G (跟13G有误差)
```