# docker发展历程
lxc --> libcontainer --> runC
## Storage
- Bind mounts：可以挂载到Host到任意目录下
- Volumns: 在Host的/var/lib/docker/volumes目录下，外部不能修改它。可以使用`docker volume create`创建
- tmpfs: 存在内存里面