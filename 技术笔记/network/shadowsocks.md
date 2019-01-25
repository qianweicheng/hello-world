# Shadowsocks
## Client
https://shadowsocks.org/en/download/clients.html
## Server
核心项目：https://github.com/shadowsocks/shadowsocks-libev
周边项目：https://github.com/shadowsocks/shadowsocks-android
#### 配置文件
```
{
    "server":"0.0.0.0",
    //单用户模式
    "password":"aes_password",
    "server_port":8389,
    //"local_address":"127.0.0.1",
    //"local_port":1081,
    //多用户模式，这里是静态多用户。 动态多用户使用--manager-address
    "port_password": {
        "8381": "foobar1",
        "8382": "foobar2",
        "8383": "foobar3",
        "8384": "foobar4"
    },
    "timeout":60,
    "method":"aes-256-gcm",
    "fast_open":true
}
```
启动服务器（参考docker启动脚本）：
`ss-server  -s 0.0.0.0 -p 8388 -k A1234567 -m aes-256-cfb -t 300 --fast-open`
`ss-server  -s 0.0.0.0 -c /data/shadowsocks.json --manager-address 0.0.0.0:8080`
## Shadowsocks Manager
https://github.com/shadowsocks/shadowsocks-manager