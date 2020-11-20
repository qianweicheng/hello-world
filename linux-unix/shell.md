# shell
## 是否可登录
- 登录shell
  1. 用户通过输入用户名/密码（或证书认证）后启动的shell；
  2. 通过带有-l|--login参数的bash命令启动的shell。
- 非登录shell
   从图形界面启动终端、使用su切换用户、通过bash命令启动bash等。
## 判断方法
我们可以通过在shell中echo $0查看，显示-bash的一定是“登陆shell”，反之显示bash的则不好说。
## 是否可交互
交互shell
非交互shell