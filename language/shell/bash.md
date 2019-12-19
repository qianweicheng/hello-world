# Bash
## shopt vs set
- set -o
- shopt -p
- set -e  遇到错误就停止
- set -u  遇到为定义的变量报错
- set -o pipefail
都是控制shell的执行，前者是标准shell支持，后缀是bash shell扩展，但10来年的发展导致这两者的界限越来越模糊