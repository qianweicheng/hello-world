# Postfix
## Install
`yum install -y postfix`
## Config
修改 /etc/postfix/main.cf
`myhostname`
## 启动
systemctl status postfix
systemctl start/stop/reload postfix
systemctl disable postfix
## 文档
https://blog.csdn.net/weixin_37958284/article/details/77067689?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-6.add_param_isCf&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-6.add_param_isCf
