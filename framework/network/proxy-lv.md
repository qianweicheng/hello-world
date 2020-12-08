# Proxy&LV
## 四种种代理方案
- Nginx
    工作在第7层，主要是Web Proxy, 支持Web Cache, 新版本支持Stream Proxy, 工作在第4层.
    Nginx 单位时间处理的最大请求数为10000个
    升级方案: Openresty
- HAProxy
    HAProxy 单位时间处理的最大请求数为20000个,可以同时维护40000-50000个并发连接，最大数据处理能力为10Gbps. HAProxy的优点能够补充Nginx的一些缺点，比如支持Session的保持，Cookie的引导；同时支持通过获取指定的url来检测后端服务器的状态。HAProxy跟LVS类似，本身就只是一款负载均衡软件；单纯从效率上来讲HAProxy会比Nginx有更出色的负载均衡速度，在并发处理上也是优于Nginx的。有强大的管理监控页面
    两种模式：
    1. 工作在第4层
    2. 工作在第7层
- LVS
  - 模式
      - NAT
      - DR
      - TUN
  - Install
    shell: `yum install ipvsadm -y`
- Hardward(NetScaler、F5、Radware)
## 比较
效率从低到高ngix<HAProxy<LVS<Hardward, 衡量负载均衡器好坏的几个重要因素： 
- 会话率 ：单位时间内的处理的请求数 
- 会话并发能力：并发处理能力 
- 数据率：处理数据能力 
## 访问流
Array/LVS — Nginx/Haproxy — Squid/Varnish — AppServer。