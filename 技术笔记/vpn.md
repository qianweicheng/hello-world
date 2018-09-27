vpn-client: tunneblick
remote 52.43.115.194 8901
socks-proxy-retry
socks-proxy 127.0.0.1 8901



1) Obfsproxy
pip install obfsproxy

pip install --upgrade scrapy
pip install --upgrade twisted (运行报错回滚到前面的版本 pip install twisted==16.4.1)
pip install --upgrade pyopenssl

obfsproxy obfs3 --dest=52.43.115.194:8901 client 0.0.0.0:8901;
obfsproxy obfs3 --dest=127.0.0.1:1194 server 0.0.0.0:8901;
obfsproxy --log-file=obfsproxy.log --log-min-severity=info obfs3 --dest=127.0.0.1:1194 server 0.0.0.0:8901;


obfsproxy obfs2  --shared-secret=ba016a998458864983848a2a6 socks 127.0.0.1:8901
obfsproxy obfs2 --dest=127.0.0.1:1194 --shared-secret=ba016a998458864983848a2a6 server 0.0.0.0:8901

2) stunnel隧道，本质就是端口转发，只不过SSL加密，对两端来说是透明的

