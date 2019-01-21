#### Kafka和ZK可以直接使用域名，方便扩展；也可以直接指定机器名
kafka-console-producer.sh --broker-list msg-queue:9092 --topic PUSH_MESSAGE
kafka-console-consumer.sh --bootstrap-server msg-queue:9092 --topic PUSH_MESSAGE
kafka-console-consumer.sh --bootstrap-server msg-queue:9092 --from-beginning --topic PUSH_MESSAGE

kafka-topics.sh --create --zookeeper zk:2181 --replication-factor 3 --partitions 6 --topic PUSH_MESSAGE
kafka-topics.sh --delete --zookeeper zk:2181 --topic PUSH_MESSAGE
kafka-topics.sh --describe --zookeeper zk:2181 --topic PUSH_MESSAGE
kafka-topics.sh --alter --topic PUSH_MESSAGE --partitions 6  --zookeeper zk:2181 
kafka-topics.sh --list --zookeeper zk-0.zk-headless:2181
#### 查看consumer group 列表
kafka-consumer-groups.sh --bootstrap-server msg-queue:9092 --list
#### 删除consumer group
删除时group里面必须没有激活状态的consumer
kafka-consumer-groups.sh -bootstrap-server msg-queue:9092 -delete -group xxxx
#### 查看各个Partion上的消息
kafka-run-class.sh kafka.tools.GetOffsetShell --broker-list msg-queue:9092 --topic pingpong --time -1
#### Topic replication等修改
1. 建立配置文件：topics-to-move.json  
```
{
    "topics": [{"topic": "PUSH_MESSAGE"}],
    "version":1
}
```
2. 运行:`kafka-reassign-partitions.sh --zookeeper zk:2181 --topics-to-move-json-file topics-to-move.json --broker-list "0,1,2" --generate`

3. 把上一步生成的方案保存到：reassignment.json
```
{
    "version":1,
    "partitions":[
        {"topic":"PUSH_MESSAGE","partition":2,"replicas":[0,1,2],"log_dirs":["any","any","any"]},
        {"topic":"PUSH_MESSAGE","partition":4,"replicas":[2,0,1],"log_dirs":["any","any","any"]},
        {"topic":"PUSH_MESSAGE","partition":1,"replicas":[2,0,1],"log_dirs":["any","any","any"]},
        {"topic":"PUSH_MESSAGE","partition":3,"replicas":[1,2,0],"log_dirs":["any","any","any"]},
        {"topic":"PUSH_MESSAGE","partition":0,"replicas":[1,2,0],"log_dirs":["any","any","any"]},
        {"topic":"PUSH_MESSAGE","partition":5,"replicas":[0,1,2],"log_dirs":["any","any","any"]}
    ]
}
```
4. 运行:`kafka-reassign-partitions.sh --zookeeper zk:2181 --reassignment-json-file reassignment.json --execute`