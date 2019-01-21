https://redis.io/commands/

http://www.runoob.com/redis/redis-server.html

启动redis集群之后，去/root 目录里面运行start-server.sh
不能使用域名，必须直接使用ip地址。
所以下面的目录无法正常使用 :(
./redis-trib.rb create --replicas 1 redis-0.redis.default.svc.cluster.local:6379 \
redis-1.redis.default.svc.cluster.local:6379 \
redis-2.redis.default.svc.cluster.local:6379 \
redis-3.redis.default.svc.cluster.local:6379 \
redis-4.redis.default.svc.cluster.local:6379 \
redis-5.redis.default.svc.cluster.local:6379

查看系统状态
info

cluster集群管理
cluster nodes
cluster info
cluster slots
cluster meet <ip> <port> ：将 ip 和 port 所指定的节点添加到集群当中，让它成为集群的一份子, 此命令运行在新添加节点，ip是集群中任意一台机器
cluster forget <node_id> ：从集群中移除 node_id 指定的节点，必须在一分钟内在每个机器上删除，否则会自动恢复。
cluster reset [hard/soft]: 从集群中删除自己
cluster replicate <node_id> ：将当前节点设置为 node_id 指定的节点的从节点。

redis扩容步骤：
1）在集群内部的一台机器上运行：CLUSTER MEET 127.0.0.1 6385
或者redis-trib.rb add-node 127.0.0.1:6386(new node) 127.0.0.1:6379(one of cluster ip)
2) ./redis-trib.rb reshard --from <node-id[,node-id]>/all --to <node-id> --slots <number of slots> [--yes] <host>:<port>
redis缩容步骤：
1) ./redis-trib.rb info localhost:6379 或 ./redis-trib.rb check localhost:6379 查看集群状态
2）把当前机器的slots移动到其他机器上去：./redis-trib.rb reshard --from <node-id> --to <node-id> --slots <number of slots> [--yes] <host>:<port>
3）删除机器（先删除master）：./redis-trib.rb del-node 127.0.0.1:6379（集群人意一台机器） `<node-id>`

慢日记分析
slowlog get N 查询
config set slowlog-log-slower-than 20000
config get slowlog-log-slower-than
config set slowlog-max-len 1024
config rewrite 写回

清除数据
FLUSHALL 
当前DB：FLUSHDB 

保存数据
SAVE/BGSAVE 

连接管理
CLIENT LIST

动态修改redis的配置
config get/set *

监控
redis-cli monitor 只能查看静态数据
redis-benchmark -n 10000

redis-stat可以持续观察
安装方法：
    apt-get install gem
    gem install redis-stat

kubectl scale statefulset redis --replicas=5