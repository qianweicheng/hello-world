####CROS
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

CORS可以分成两种：
* 简单请求
    HTTP方法是下列之一
    1. HEAD
    2. GET
    3. POST  

    HTTP头包含
    1. Accept
    2. Accept-Language
    3. Content-Language
    4. Last-Event-ID
    5. Content-Type，但仅能是下列之一
            application/x-www-form-urlencoded
            multipart/form-data
            text/plain
* 复杂请求
    任何一个不满足上述要求的请求，即被认为是复杂请求。一个复杂请求不仅有包含通信内容的请求，同时也包含预请求（preflight request）。

1. 预请求
>OPTIONS /cors HTTP/1.1
Origin: http://api.alice.com
Access-Control-Request-Method: PUT
Access-Control-Request-Headers: X-Custom-Header
Host: api.bob.com
Accept-Language: en-US
Connection: keep-alive

2. 预响应
>Access-Control-Allow-Origin: http://api.bob.com(必须)
Access-Control-Allow-Methods: GET, POST, PUT(必须)
Access-Control-Allow-Headers: X-Custom-Header（当预请求中包含Access-Control-Request-Headers时必须包含））
Access-Control-Allow-Credentials:true(如果客户端使用了xhr.withCredentials = true;则必须包含)
Content-Type: text/html; charset=utf-8

3. 正式请求
>PUT /cors HTTP/1.1
Origin: http://api.alice.com
Host: api.bob.com
X-Custom-Header: value
Accept-Language: en-US
Connection: keep-alive
User-Agent: Mozilla/5.0...

4. 实际响应
>Access-Control-Allow-Origin: http://api.bob.com
Content-Type: text/html; charset=utf-8

客户端:
>var xhr = new XMLHttpRequest();
xhr.open('GET', 'http://example.com/', true); 
xhr.withCredentials = true; 
xhr.send(null);
