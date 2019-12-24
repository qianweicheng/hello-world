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
## 文件同步
  - scp
  - rsync (`yum install -y rsync`or `brew install rsync`)
### 实时同步
- 当同步的目录数据量不大时，建议使用Rsync+Inotify-tools；
- 当数据量很大（几百G甚至1T以上）、文件很多时，建议使用Rsync+sersync
## Other
- command
- which
- whereis