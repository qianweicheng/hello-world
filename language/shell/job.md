# Job
## Job管理
bg %[number] 后台启动一个暂停的任务，默认1
fg %[number] 将一个后台的任务挪到前台，默认1
kill -9 %[number]
jobs 查看后台任务列表
注：bg/fg的%可以省略

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
- at
  - -f 指定文件
  - -t 指定时间,格式如:`[[CC]YY]MMDDhhmm[.SS]`
  - -c：打印任务的内容到标准输出
- atq: `at -l`
- atrm: `at -r`,`atq the-job-id`
### 两种方式指定时间
- -t 参数，见上。`at -t 11070101 -f cmd.txt`
- 直接指定:`at [time]`,格式如下:
```
Minute    at now + 5 minutes   任务在5分钟后运行
Hour      at now + 1 hour      任务在1小时后运行
Days      at now + 3 days      任务在3天后运行
Weeks     at now + 2 weeks     任务在两周后运行
Fixed     at midnight          任务在午夜运行
Fixed     at 10:30pm           任务在晚上10点30分
```
### 两种方式指定命令
- -f 指定文件
    ```
    at now + 1min -f cmd.txt
    ```
- stdin输入
    ```
    at now + 1 min
    # 进入编辑
    # 结束: ctrl+d
    ```