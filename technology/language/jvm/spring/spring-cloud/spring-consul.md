# [官网文档](https://www.consul.io/docs)
8500，客户端http api接口
8600，客户端DNS服务端口
8400，客户端RPC通信端口
8300，集群server RPC通信接口
8301，集群DC内部通信接口
8302，集群DC之间通信接口
### [Go Library](https://github.com/hashicorp/consul)
### [Python Library](https://github.com/cablehead/python-consul)
## Consul Template
- 配置文件模板是："./config.ctmpl"
`
iplist = [ {{range service "bottle"}} "{{.Address}}",{{end}} ]
`
- 需要生成的配置文件是："./config.py"
`
consul {
    address = "127.0.0.1:8500"
}
template {
source = "./config.ctmpl"
destination = "./config.py"
command = "python ./config.py"
}
`
- 运行:`consul-template -config ./tmpl.json -once`
