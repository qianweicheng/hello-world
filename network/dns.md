# DNS
- A: ipv4
- TXT: 存储简短的文本，可以用于多种用途，比如公钥等
- CNAME: alias
- AAAA: ipv6
- PTR: 反向查询
- NS: 名字服务器
- SRV: 记录用来标识某台服务器使用了某个服务
- SOA
## RFC1123
- host 必须支持63 bytes，建议支持255 bytes
- 
## Dig
`dig yourdomain ANY`
`dig _sip._udp.sip.voice.google.com SRV`