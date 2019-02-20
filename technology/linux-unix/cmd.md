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
## Linux终端命令
- 查看当前终端：tty
- 查看当前登录终端：who
- 查看当前登录终端，并且展示他们正在做什么：w
## who、w、users、last和ac