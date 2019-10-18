# subprocess
开启子进程
- subprocess
    这个库替换了老的如下一些库
    os.system
    os.spawn*
    os.popen*
    popen2.*
    commands.*
- pexpect
  这个库主要用于人机对话模拟
## subprocess
### usage
subprocess.call(["ls", "-l"])
subprocess.call("exit 1", shell=True)
subprocess.check_output(["echo", "Hello World!"])
### replace
```
# old
status = os.system("mycmd" + " myarg")
# new
status = subprocess.call("mycmd" + " myarg", shell=True)
```
```
pid = os.spawnlp(os.P_NOWAIT, "/bin/mycmd", "mycmd", "myarg")
==>
pid = Popen(["/bin/mycmd", "myarg"]).pid
```
```
pipe = os.popen("cmd", 'r', bufsize)
==>
pipe = Popen("cmd", shell=True, bufsize=bufsize, stdout=PIPE).stdout
```
## pexpect
### usage
```
process = pexpect.spawn("ftp sw-tftp")
logFileId = open("logfile.txt", 'w')
process.logfile = logFileId
process.logfile_read=sys.stdout - 获取标准输出的内容
process.logfile_send=sys.stdout - 在屏幕上打印向程序发送的内容
```