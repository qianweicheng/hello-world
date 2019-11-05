# VPN
- PPTP:只能在IP网络上，建立单一隧道,不安全
- L2TP:各种网路上，多隧道，不提供加密。 IPSEC和IKEv2是加密协议
- OpenVPN
- PPP：对数据进行封装
## 搭建VPN:https://github.com/hwdsl2/setup-ipsec-vpn
- 配置文件
    ```vpn.env:
        VPN_IPSEC_PSK=xxx
        VPN_USER=xxx
        VPN_PASSWORD=xxx
    ```
- 运行：
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
## AWS cloudformation
模版: https://s3.amazonaws.com/webdigi/VPN/Unified-Cloud-Formation.json
官网: https://us-west-2.console.aws.amazon.com/cloudformation/home
教程: https://blog.csdn.net/uuihoo/article/details/80980628


