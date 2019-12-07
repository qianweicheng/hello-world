# Command
## checksum
- (linux)sha256sum校验(注意*号):`echo "$KONG_SHA256 *kong.tar.gz" | sha256sum -c`
    生成校验码:`sha256sum kong.tar.gz >kong.sha256sum`
    校验: `sha256sum -c <(grep kong.tar.gz kong.sha256sum)`
- (macos)shasum
## File System
- `mount` `umount`
- `df -h` 
- `du -[sh] [file]`:
  - -s 只显示目录，不递归
  - -h 显示友好，
  - file 指定特定文件/目录
- `cat /proc/self/mountstats`
- `resize2fs`
- `lsblk --list block devices`
## Other
- command
- which
- whereis
