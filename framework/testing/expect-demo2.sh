#!/usr/bin/env bash
# 这里演示如何将一段expect脚本嵌入到sh中
expect << EOF
log_file ./expect.log
set timeout 1
spawn bash
send "echo weicheng\r"
expect EOF
EOF
echo back to top