## crontab命令
crontab -l -e -r
/etc/crontab
/var/spool/cron
crontab服务
/sbin/service crond start    //启动服务
/sbin/service crond stop     //关闭服务
/sbin/service crond restart  //重启服务
/sbin/service crond reload   //重新载入配置
/sbin/service crond status   //查看服务状态 
例子
* * * * *
第一个表示分钟 0-59
第二个表示小时 0-23
第三个表示几号 1-31
第四个表示月份 1-12
第五个表示星期 星期0～6（0表示星期天） 
第六列表示允许命令的用户身份，可以省略

*/N 每隔N个单位
N-M 表示N到M
N,M 表示N或M


## at命令
格式如下：
at 时间 命令

AT Time中的时间表示方法
　　Minute    at now + 5 minutes   任务在5分钟后运行

　　Hour      at now + 1 hour      任务在1小时后运行

　　Days      at now + 3 days      任务在3天后运行

　　Weeks     at now + 2 weeks     任务在两周后运行

　　Fixed     at midnight          任务在午夜运行

　　Fixed     at 10:30pm           任务在晚上10点30分