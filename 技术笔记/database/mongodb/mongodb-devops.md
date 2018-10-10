#### 在config机器，shard机器
    configserver={_id:'configReplSet',members:[
    {_id:0,host:'host1:port',priority:2},
    {_id:1,host:'host1:port',priority:1},
    {_id:2,host:'host1:port',priority:1}]
    }
    rs.initiate(configserver)
    修改使用：rs.reconfig(config_data)

####添加Shard（在router机器）：
>此处只需要指向shard里面其中一台机器
use admin
db.runCommand({addshard:"rs1/host1:port,host2:port"})
db.runCommand({addshard:"rs2/host1:port,host2:port"})
db.runCommand({addshard:"rs3/host1:port,host2:port"})
sh.addShard("rs3/host1:port,host2:port")
Ex: db.runCommand({addshard:"rs1/mongodb-shad-a-0.mongodb-shad.default.svc.cluster.local:27018"})

####建立索引有两种:一种是升序，一种是hash
db.collection.createindex/ensureIndex({_id:1/"hashed"})

use tigase
db.edi_contact.createIndex({ownerId:"hashed"})
db.msg_history.createIndex({from_hash:1})

####建立分片
>use admin
`sh.enableSharding("<database>")` or `db.runCommand({enablesharding:"<database>"})`
    sh.shardCollection("<database>.<collection>", { <key> : "hashed" } )

    sh.enableSharding("mydb")

    sh.shardCollection("mydb.wq", {name : "hashed"}, false, {numInitialChunks : 3})
    db.runCommand({shardcollection:"tigase.edi_contact",key:{_id:1}, options:{numInitialChunks : 3}})
> mongo collection建立了shard之后，无法修改与删除，只能做好数据备份之后，drop掉这个collection重建

####删除shard，先进行数据迁移
- db.runCommand({movePrimary : "tigase", to : "rs2" })
- sh.moveChunk("tigase.wq",{"value":NumberLong(1)},"rs1")
- db.runCommand({removeshard:"rs1"})

####设置迁移维护窗口
db.getCollection("settings").update({"_id":"balancer"},{"$set":{"activeWindow.stop":"23:30"}})

####预先分片
db.tig_users.getShardDistribution()
sh.splitAt("mydb.wq", {name: 1})  强制指定拆分点
sh.splitFind("mydb.wq", {name:1}) 自动计算，让两子分片大致平衡
sh.moveChunk("tigase.wq",{"value":NumberLong(1)},"rs1")

db.runCommand( { moveChunk:"tigase.wq",find :{"value": "rs2"}, to :"rs1"} )
db.runCommand( { moveChunk:"tigase.wq", bounds :[{"value": "$minKey"}, {"value":"$maxKey"}], to:"rs1"} )

sh.stopBalancer()
sh.startBalancer()

####查看分片信息：
db.wq.getShardDistribution()
如果某次发现改函数返回空，但用sh.status()有能看到，那很可能是底下某个shard的index被删除了，解决方案就是到该shard里面去重建index

####添加删除机器到某个shard
rs.add("host:port")
rs.remove("host:port")
rs.addArb("host:port") 或者rs.add({_id:x,host:'xxxx',arbiterOnly:true})
db.adminCommand

####读写分离：
db.getMongo().setSlaveOk() = rs.slaveOk();
db.getMongo().getSlaveOk()
primary/primaryPreferred/secondary/secondaryPreferred/nearest
db.getMongo().setReadPref('secondary')
db.getMongo().getReadPrefMode()


####模拟故障
db.adminCommand({"shutdown":1})

####性能监控
mongostat
mongotop

打开慢查询
db.getProfilingStatus();
2.开启慢日志，设置超过100毫秒的操作为慢操作
db.setProfilingLevel(1,100); 
或者 db.setProfilingLevel(2)
3.查看慢日志内容
db.system.profile.find().sort({$natural:-1})
或者 db.system.profile.find()

导出数据到当前文件夹
1）mongodump -h localhost -p 27018 [--out /data/backup/]
   部分备份  mongodump --collection myCollection --db test
2）直接拷贝文件，不要启动服务器：mongodump --dbpath /data/db/

####导入数据
mongorestore -d tigase -c tig_users dump/tigase/tig_users.bson
####运行命令
mongo mongodb-shad-a-0.mongodb-shad:27018 --eval "printjson(rs.status())"

直接安装步骤（https://www.mongodb.com/download-center#community）：
wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-amazon-3.4.10.tgz
tar -xvzf mongodb-linux-x86_64-amazon-3.4.10.tgz
sudo mv mongodb-linux-x86_64-amazon-3.4.10 /usr/local/mongodb
 mongod --shardsvr --replSet rs1 --dbpath=/home/ec2-user/data/db


1. Mongodb 压垮之前的征兆：
即将崩溃
Error in workloop { MongoError: failed to connect to server [127.0.0.1:27018] on first connect [MongoError: connect ECONNREFUSED 127.0.0.1:27018]
W NETWORK [ReplicaSetMonitor-TaskExecutor-0] Failed to connect to 100.96.5.23:27018, in(checking socket for error after poll), reason: Connection refused kubernetes.pod_name:mongodb-shad-b-0 stream:stdout
已经开始报警了：
Error in heartbeat request to mongodb-shad-b-1.mongodb-shad.default.svc.cluster.local:27018; HostUnreachable: Connection refused kubernetes.pod_name:mongodb-shad-b-0

错误：
Cannot allocate memory at src/mongo/db/storage/wiredtiger/wiredtiger_record_store.cpp 459
MongoDB starting memory