# JSON WEB TOKEN(JWT)
https://tools.ietf.org/html/rfc7519
## 结构
`HEADER.PAYLOAD.SIGN`
## Header
typ: header parameter
cty: content type
## Payload
JWT Claims: iss, sub,aud,exp,nbf,iat,jti
## Kong的集成
iss: 填写jwt的key，用来查找jwt的rsa public/secret
