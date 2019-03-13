# JSON Web Token(JWT)
参考:https://jwt.io/
## Header
{
  "alg": "HS256",
  "typ": "JWT"
}
## Payload
{
  "sub": "1234567890",
  "name": "John Doe",
  "iat": 1516239022,
  "iss":"issuer, kong通过它确定使用哪个secret"
}
## SIGNATURE
HMACSHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
  "!!!SECRET!!!"
)
## Result is
base64UrlEncode(header).base64UrlEncode(payload).!!!SIGNATURE!!!

