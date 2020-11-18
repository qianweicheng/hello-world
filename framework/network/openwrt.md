# 玩转Openwrt
## 包管理
使用`opkg`进行包管理
- update
- list:
- install: `opkg install tcpdump-mini`
- remove:
## 抓包
```
    // 直接模式
    ssh ssh用户名@ssh地址 'tcpdump -s 0 -U -n -w - -i br-lan not port 22' | wireshark -k -i -
```
```
    // 使用管道
mkfifo /tmp/fifo
ssh root@192.168.2.1 'tcpdump -s 0 -U -n -w - -i br-lan not port 2222' > /tmp/fifo &
wireshark -k -i /tmp/fifo
```
## Shadowsocks
gl-ss
gl-ss-server
## VPN
