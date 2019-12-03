# jq
jq命令允许直接在命令行下对JSON进行操作，包括分片、过滤、转换等
## 命令
`jq [options] filter [files]`
- options
```
--raw-input/-R：不作为JSON解析，将每一行的文本作为字符串输出到屏幕。
--null-input/ -n：不读取任何输入，过滤器运行使用null作为输入。一般用作从头构建JSON数据。
--compact-output /-c：使输出紧凑，而不是把每一个JSON对象输出在一行。
--colour-output / -C：打开颜色显示
--monochrome-output / -M：关闭颜色显示
--ascii-output /-a：指定输出格式为ASCII
```
- filter(https://stedolan.github.io/jq/manual/)
```
.   : 默认输出
.foo: 输出指定属性，foo代表属性。
.[foo] ：输出指定数组元素。foo代表数组下标。
.[]：输出指定数组中全部元素
， ：指定多个属性作为过滤条件时，逻辑或
| ： 管道， 做逻辑与
select(.A=="abc")
has: map(has(key))
in: map(in[0,1])
map: map(.A = .+1)
```
## Demo
```
cat aws-instance-info.json | jq '.Reservations[].Instances[] | select(.State.Name == "running", .State.Name == "stopped") | {id:.InstanceId, status:.State.Name, dns:.PublicDnsName,ip:.PublicIpAddress, name: .Tags[] | select(.Key=="Name") | .Value}'
```