# HTTP
HTTP 1.1 定义的8种方法
- OPTIONS:主要用做预请求, 不能缓存
- GET
    ## GET方法URL长度限制, [参考这里](https://stackoverflow.com/questions/417142/what-is-the-maximum-length-of-a-url-in-different-browsers) 这个限制不是HTTP协议限制，而是大部分浏览器和HTTP服务器的限制。
2000字节以内的长度是一个比较安全。
- HEAD:没有BODY
- POST:更新
- PUT:新建
- DELETE:删除
- TRACE:主要用于诊断. 用于验证请求是否如愿穿过了请求/响应链,不能缓存
- CONNECT:代理
## CROS
所有CROS的Header
* Origin(Client)
* Access-Control-Request-Headers(Client)
* Access-Control-Request-Method(Client)
* Access-Control-Allow-Credentials
* Access-Control-Allow-Headers
* Access-Control-Allow-Methods
* Access-Control-Allow-Origin
* Access-Control-Expose-Headers
* Access-Control-Max-Age

#### CORS可以分成两种：
* 简单请求
    HTTP方法是下列之一
    - HEAD
    - GET
    - POST  

    并且HTTP头包含：
    - Accept
    - Accept-Language
    - Content-Language
    - Last-Event-ID
    - Content-Type，但仅能是下列之一
            application/x-www-form-urlencoded
            multipart/form-data
            text/plain
* 复杂请求
    任何一个不满足上述要求的请求，即被认为是复杂请求。一个复杂请求不仅有包含通信内容的请求，同时也包含预请求（preflight request）。
#### 具体步骤
1. 预请求
    ```
    OPTIONS /cors HTTP/1.1
    Origin: http://api.alice.com
    Access-Control-Request-Method: PUT
    Access-Control-Request-Headers: X-Custom-Header
    Host: api.bob.com
    Accept-Language: en-US
    Connection: keep-alive
    ```
2. 预响应
    ```
    Access-Control-Allow-Origin: http://api.bob.com(必须)
    Access-Control-Allow-Methods: GET, POST, PUT(必须)
    Access-Control-Allow-Headers: X-Custom-Header（当预请求中包含Access-Control-Request-Headers时必须包含））
    Access-Control-Allow-Credentials:true(如果客户端使用了xhr.withCredentials = true;则必须包含)
    Content-Type: text/html; charset=utf-8
    ```
3. 正式请求
    ```
    PUT /cors HTTP/1.1
    Origin: http://api.alice.com
    Host: api.bob.com
    X-Custom-Header: value
    Accept-Language: en-US
    Connection: keep-alive
    User-Agent: Mozilla/5.0...
    ```
4. 实际响应
    ```
    Access-Control-Allow-Origin: http://api.bob.com
    Content-Type: text/html; charset=utf-8
    ```
* 客户端代码:
    ```
    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://example.com/', true); 
    xhr.withCredentials = true; 
    xhr.send(null);
    ```
## CORB
- 如果 response 包含 X-Content-Type-Options: nosniff 响应头部，那么如果 Content-Type 是以下几种的话， response 将受 CORB 保护：
    html mime type
    xml mime type（除了 image/svg+xml）
    json mime type
    text/plain
- 如果 response 的状态是 206，那么如果 Content-Type 是以下几种的话， response 将受 CORB 保护：
    html mime type
    xml mime type（除了 image/svg+xml）
    json mime type
- 否则，CORB 将尝试探测 response 的 body：
    html mime type，并且探测结果是 html 内容格式，response 受 CORB 保护
    xml mime type（除了 image/svg+xml）, 并且探测结果是 xml 内容格式，response 受 CORB 保护
    json mime type，并且探测结果是 json 内容格式，response 受 CORB 保护
    text/plain，并且探测结果是 json、html 或者 xml 内容格式，response 受 CORB 保护任何以 JSON security prefix 开头的 response（除了 text/css）受 CORB 保护
## 缓存
- 强制缓存
    如果本地缓存没有过期，则直接使用,浏览器返回200
- 协商缓存
    在本地数据库拿到资源的ETAG/Last-Modified-Since,去服务器比较一次，如果没有改变则返回304