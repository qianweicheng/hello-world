# Netstat
## 流量分析
- 查看tpc连接:`netstat -ant|awk '/^tcp/ {++S[$NF]} END {for(a in S) print (a,S[a])}'`