核心项目：https://github.com/shadowsocks/shadowsocks-libev
周边项目：https://github.com/shadowsocks/shadowsocks-android
启动服务器（参考docker启动脚本）：
`ss-server  -s 0.0.0.0 -p 8388 -k A1234567 -m aes-256-cfb -t 300 --fast-open`