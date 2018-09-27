####Job管理
bg %[number] 后台启动一个暂停的任务，默认1
fg %[number] 将一个后台的任务挪到前台，默认1
kill -9 %[number]
jobs 查看后台任务列表
注：bg/fg的%可以省略
####UBUNTU安装工具集
apt-get update
apt-get install -y vim wget python2.7 python-pip redis-tools dnsutils
apt-get purge / apt-get –purge remove 
删除已安装包（不保留配置文件)。 
如软件包a，依赖软件包b，则执行该命令会删除a，而且不保留配置文件
apt-get autoremove 
删除为了满足依赖而安装的，但现在不再需要的软件包（包括已安装包），保留配置文件。

####LANG问题:locale
1）对于CentOS，可以直接编辑/etc/sysconfig/i18n文件，将LANG="en_US.UTF-8"设置成LANG="zh_CN.UTF-8"
localedef -i en_US -f UTF-8 en_US.UTF-8

####Etc
source = .
nohub xxx &