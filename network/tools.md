# Useful Tools
## CURL
- 参数
    -d --data: application/x-www-form-urlencoded
    --data-urlencode: 
    --data-binary: @开头为文件
    --data-raw: 同上，不处理@
    -A: user agent
    -I: Header ONLY
    -i: Include Header
    -o: 手动指定输出到文件的名字
    -O: 自动输出到文件，可能失败
    -L: 跟随链接重定向
    -x/--proxy: <host[:port]>  在给定的端口上使用HTTP代理
    -c: 存cookie到文件cookie-jar
    -b: 取cookie-jar, 一般配合`-c`使用；如果有等号就当纯文本提交
#### 案例
`curl -H 'Content-Type: application/json' --data-raw '{xxx:yyy}' "http://xxxx"`
`curl -H 'Content-Type: application/json' -d '{xxx:yyy}' "http://xxxx"`
Multipart: `curl -F "file=@nohup.out" -F "a=b" "http://192.168.0.2/aaaa"`
下载文件: `curl -LO http://xxxx.zip`
Basic Auth: `curl -u username:password https://xxx/`
## Wget
- 参数
 -O: 手动指定文件名
 -L: 跟随链接重定向
`wget -O "Filename" url`

## 内网穿透工具(可以让外网访问内网)
- ngrok(国外)
- natapp(国内)
- 花生壳(贵)
- ssh,authssh
- Spike
- Lanproy
- [proxychains-ng](https://github.com/rofl0r/proxychains-ng):一款Hook Socket的工具，使其通过Socket5代理访问外网，对于应用本身不支持代理的应用非常有用，避免使用VPN. Mac下需要先关闭SIP，[教程](https://blog.csdn.net/king_cpp_py/article/details/79560634)
## 获取本机ip
`ifconfig | grep inet`