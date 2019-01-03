# HTTP
## GET方法URL长度限制, [参考这里](https://stackoverflow.com/questions/417142/what-is-the-maximum-length-of-a-url-in-different-browsers)
这个限制不是HTTP协议限制，而是大部分浏览器和HTTP服务器的限制。
2000字节以内的长度是一个比较安全。

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