# Sender Policy Framework(SPF)
发件人策略框架 (SPF) 
RFC7208: Sender Policy Framework (SPF) for Authorizing Use of Domains in Email, Version 1
RFC: https://tools.ietf.org/html/rfc7208
白话版: https://postmarkapp.com/guides/spf
## 规则
- 验证的是Return-Path,而不是From
- Received-SPF:
  - client-ip
  - envelope-from
  - helo
  - problem
  - receiver
  - identity
  - mechanism
  - name
- Authentication-Results:
  - 里面会有Received-SPF的部分摘要信息
## 局限性
- Keeping SPF records updated as brands change service providers and add mail streams is difficult due to lack of visibility.
- Just because a message fails SPF, doesn’t mean it will always be blocked from the inbox—it’s one of several factors email providers take into account.
- SPF breaks when a message is forwarded.
- SPF does nothing to protect brands against cybercriminals who spoof the display name or “header from” address in their message, which is the more frequently spoofed “from” address since it’s the address most visible to the email recipient.
- 不解决Cross-User问题，需要通过SMTP AUTH解决
- 使用了外部不可信资源（DNS）
- 隐私泄漏
## Example
### SMTP
我们通过`nslookup smtp.126.com`查询得到网易的
smtp服务器列表:`220.181.15.111-114`
MX的服务器列表:`220.181.15.131-209`
网易邮箱禁止了使用MX的邮箱当成SMTP邮箱发送邮件
`Local user is not allowed,126 mx1,H8mowADXbKL72nFdnOR5CQ--.47537S2 1567742717`
### MX and SPF
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
省略...
```
其中我们126.com常用的IP发送地址`220.181.15.111`属于`220.181.12.0/22`段号.
```
前22位为网络号，后10位为机器号
xxxxxxxx.xxxxxxxx.xxxxxxxx.xxxxxxxx
                  00001100
220.181.12-15.xxx
```