# iptables的4表5链
iptables的结构：iptables -> Tables -> Chains -> Rules

iptables具有Filter, NAT, Mangle, Raw四种内建表：
1. Filter表
Filter表示iptables的默认表，因此如果你没有自定义表，那么就默认使用filter表，它具有以下三种内建链：
INPUT链 – 处理来自外部的数据。
OUTPUT链 – 处理向外发送的数据。
FORWARD链 – 将数据转发到本机的其他网卡设备上。

2. NAT表
NAT表有三种内建链：
PREROUTING链 – 处理刚到达本机并在路由转发前的数据包。它会转换数据包中的目标IP地址（destination ip address），通常用于DNAT(destination NAT)。
POSTROUTING链 – 处理即将离开本机的数据包。它会转换数据包中的源IP地址（source ip address），通常用于SNAT（source NAT）。
OUTPUT链 – 处理本机产生的数据包。

3. Mangle表
Mangle表用于指定如何处理数据包。它能改变TCP头中的QoS位。Mangle表具有5个内建链：
PREROUTING
OUTPUT
FORWARD
INPUT
POSTROUTING

4. Raw表
Raw表用于处理异常，它具有2个内建链：
PREROUTING chain
OUTPUT chain

二、IPTABLES 规则(Rules)
牢记以下三点式理解iptables规则的关键：
Rules包括一个条件和一个目标(target)
如果满足条件，就执行目标(target)中的规则或者特定值。
如果不满足条件，就判断下一条Rules。

iptables -P 设置默认策略
-A append
-I insert
-j jump
