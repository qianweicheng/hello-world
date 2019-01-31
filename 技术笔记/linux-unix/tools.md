# Utils
## checksum
- (linux)sha256sum校验(注意*号):`echo "$KONG_SHA256 *kong.tar.gz" | sha256sum -c`
    生成校验码:`sha256sum kong.tar.gz >kong.sha256sum`
    校验: `sha256sum -c <(grep kong.tar.gz kong.sha256sum)`
- (macos)shasum
    