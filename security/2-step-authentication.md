# MFA
## 2 step authentication / Two-factor authentication
都涉及到一个recover code, 就是当不能正常收到二次验证码的时候，使用它当作密码登录
- 使用短信方式
  - 发送一个验证码给手机
  - 手机接受这个验证码并回填网站
  - 验证回填的验证码通过则设置成功
- 使用App方式
  - 网站生成一个密钥(kabcdeig3cjgpfad)
  - 安装一个标准的密码生成器，可以离线运行，基于密钥和时间，再根据公开的算法计算出一个6位数字的一次性token。
  - 验证这个token通过，则二次验证设置成功

## 对于一些APP无法输入二次验证的处理
hushmail： 直接在密码后面+空格+Token
