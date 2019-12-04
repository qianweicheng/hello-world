# 说明
## 公式
```
buff = free.(buff/cache) - memory.stat.(total_cache)
memory.usage_in_bytes 
    = memory.stat.(totla_cache) + memory.stat.(total_rss)
    ~= free.used + free.(buff/cache) - (buff)
```
- /sys/fs/cgroup/memory/memory.usage_in_bytes
- /sys/fs/cgroup/memory/memory.stat