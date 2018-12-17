# VPN
- PPTP:只能在IP网络上，建立单一隧道,不安全
- L2TP:各种网路上，多隧道，不提供加密。 IPSEC和IKEv2是加密协议
- OpenVPN
- PPP：对数据进行封装

## 搭建VPN:https://github.com/hwdsl2/setup-ipsec-vpn
>目前K8s,Aws 对UDP支持有限，把docker放k8s还不成熟

vpn.env:
```
VPN_IPSEC_PSK=xxx
VPN_USER=xxx
VPN_PASSWORD=xxx
```
运行：
```
docker run \
--name ipsec-vpn-server  \
--env-file ./vpn.env \
--restart=always \
-p 500:500/udp  \
-p 4500:4500/udp \
-v /lib/modules:/lib/modules:ro \
-d --privileged  \
hwdsl2/ipsec-vpn-server
```




