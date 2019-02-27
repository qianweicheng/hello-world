# Utils
## checksum
- (linux)sha256sum校验(注意*号):`echo "$KONG_SHA256 *kong.tar.gz" | sha256sum -c`
    生成校验码:`sha256sum kong.tar.gz >kong.sha256sum`
    校验: `sha256sum -c <(grep kong.tar.gz kong.sha256sum)`
- (macos)shasum
## File System
- `mount` `umount`
- `df -h` `du -h`
- `cat /proc/self/mountstats`
- `resize2fs`
- `lsblk --list block devices`
## Linux终端
#### 终端命令
- 查看当前终端: `tty`
- 查看当前登录终端: (/var/run/utmp) `who`, `w`(详细), `users`
- 查看历史登陆记录: last (/var/log/wtmp)
- 查看历史登陆失败记录: `lastb` (/var/log/btmp)
- SSH日记: `tail -f /var/log/secure`
- 修改终端设置:`stty`
#### 终端
终端: /dev/tty
伪终端: /dev/[pts|pty]
- 向自己发送信息: `echo xxx > /dev/tty`
- 向另外一个终端发送: `echo xxx > /dev/pts/x`
当前tty设备:/dev/tty
当前终端设备文件的别名: /dev/tty0
/dev/console: 是个只输出的设备，功能很简单，只能在内核中访问；tty是char设备，可以被用户程序访问。
##
which
whereis
command