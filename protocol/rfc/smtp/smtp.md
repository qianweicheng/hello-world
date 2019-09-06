# SMTP
MX vs SMTP
## 126
#### MX and SPF
```
C: dig MX 126.com
S:  126.com	mail exchanger = 10 126mx02.mxmail.netease.com.
    126.com	mail exchanger = 10 126mx01.mxmail.netease.com.
    126.com	mail exchanger = 50 126mx00.mxmail.netease.com.
    126.com	mail exchanger = 10 126mx03.mxmail.netease.com.
C: dig TXT 126.com
S: v=spf1 include:spf.163.com -all
C: dig TXT spf.163.com
S: v=spf1 include:a.spf.163.com include:b.spf.163.com include:c.spf.163.com include:d.spf.163.com include:e.spf.163.com -all
```
递归查询a-e.spf.163.com得到
```
v=spf1 ip4:220.181.12.0/22 ip4:220.181.31.0/24 ip4:123.125.50.0/24 ip4:220.181.72.0/24 ip4:123.58.178.0/24 ip4:123.58.177.0/24 ip4:113.108.225.0/24 ip4:218.107.63.0/24 ip4:123.58.189.128/25 ip4:123.126.96.0/24 ip4:123.126.97.0/24 -all
v=spf1 ip4:52.31.100.154 ip4:52.19.67.100 ip4:176.34.21.58 ip4:121.195.178.48/28 ip4:223.252.213.0/24 ip4:113.108.226.64/26 ip4:58.248.244.64/26 -all
v=spf1 ip4:223.252.206.0/24 ip4:43.230.90.0/27 ip4:14.29.82.0/25 ip4:122.13.158.0/25 ip4:35.154.184.19 ip4:35.158.20.192 ip4:52.198.69.159 ip4:52.221.130.187 ip4:52.56.66.10 ip4:54.219.167.112 ip4:103.129.252.0/26 -all
v=spf1 ip4:123.126.65.0/24 ip4:106.2.88.0/24 ip4:220.181.97.0/24 ip4:180.150.142.123 ip4:180.150.142.124 ip4:180.150.154.88 ip4:180.150.154.92 ip4:180.150.154.93 ip4:103.211.228.151 ip4:59.111.176.0/24 ip4:220.194.24.0/24 ip4:52.52.2.81 -all
v=spf1 ip6:2407:ae80:100:1000::/64 ip6:2407:ae80:100:1001::/64 ip6:2407:ae80:100:1002::/64 ip6:2407:ae80:300:1000::/64 ip6:2407:ae80:300:1001::/64 -all
```
其中我们126.com常用的IP发送地址`220.181.15.111`属于`220.181.12.0/22`段号.
```
前22位为网络号，后10位为机器号
xxxxxxxx.xxxxxxxx.xxxxxxxx.xxxxxxxx
                  00001100
220.181.12-15.xxx
```
#### SMTP
我们通过`nslookup smtp.126.com`查询得到网易的
smtp服务器列表:`220.181.15.111-114`
MX的服务器列表:`220.181.15.131-209`
网易邮箱禁止了使用MX的邮箱当成SMTP邮箱发送邮件
`Local user is not allowed,126 mx1,H8mowADXbKL72nFdnOR5CQ--.47537S2 1567742717`
## qq
qq.com	mail exchanger = 30 mx1.qq.com.
qq.com	mail exchanger = 10 mx3.qq.com.
qq.com	mail exchanger = 20 mx2.qq.com.
qq.com	text = "v=spf1 include:spf.mail.qq.com -all"
## edison
edison.tech	mail exchanger = 1 aspmx.l.google.com.
edison.tech	mail exchanger = 5 alt1.aspmx.l.google.com.
edison.tech	mail exchanger = 10 aspmx3.googlemail.com.
edison.tech	mail exchanger = 10 aspmx2.googlemail.com.
edison.tech	mail exchanger = 5 alt2.aspmx.l.google.com.
edison.tech	text = "google-site-verification=sGM4dmZdcsdhzH27ZMfqI_BjIJKWHX29_1jzGigeQkQ"

SPF check failed [N9UuuMUW4i/wrCLL0pwqLPLO9j/Nl5ps0Jfk0Ff3vau5vpB9oxGCIzA=  IP: 111.77.204.255]. http://service.mail.qq.com/cgi-bin/help?subtype=1&&no=1001445&&id=20022.'