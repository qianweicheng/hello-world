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
#### 启动服务器（参考docker启动脚本）：
- Run directly
`ss-server  -s 0.0.0.0 -p 8388 -k A1234567 -m aes-256-cfb -t 300 --fast-open`
`ss-server  -s 0.0.0.0 -c /data/shadowsocks.json --manager-address 0.0.0.0:8080`
- Run in Docker
`docker run -e METHOD=aes-256-gcm -e PASSWORD=edison@bj -p 8388:8388 -p 8388:8388/udp -d shadowsocks/shadowsocks-libev`
## Shadowsocks Manager
https://github.com/shadowsocks/shadowsocks-manager

## Shadowsocks三种模式
- PAC
    PAC 是一套智能选择模式，会根据配置文件选择是否使用代理
- 全局模式
    所有指向本代理的模式均走代理服务器
- 手动模式
    Shadowsocks会在本地启动ss-local，但不会把它设置成系统代理，浏览器得手动配置。前两种方式会设置成系统代理，浏览器默认会使用系统代理，故无需额外配置