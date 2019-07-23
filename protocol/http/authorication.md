# Authorication
Format: `Authorization: <type> <credentials>`
## authentication schemes
- Basic:  base64-encoded credentials. `base64(username:password)`
- Bearer: bearer tokens to access OAuth 2.0-protected resources
- Digest: 
- HOBA: HTTP Origin-Bound Authentication
- Mutual
- AWS4-HMAC-SHA256
## Response
如果验证失败则服务器必须在Header中返回: `WWW-Authenticate`
Ex:`WWW-Authenticate Basic realm="Administrator's Area"`