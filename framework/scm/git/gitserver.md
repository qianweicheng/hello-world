# Git Server
## 搭建三部曲
1. 本质就是在linux 创建一个git用户，并且配置shell和其他权限
2. 初始化一个代码库`sudo git init --bare sample.git`
3. 添加用户到`/home/git/.ssh/authorized_keys`

https://www.liaoxuefeng.com/wiki/896043488029600/899998870925664
