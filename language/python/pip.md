# Pip
## Install
`curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`
## 命令
- `python -m pip xxx`(推荐) 保证与当前python版本一致
- `pip xxx`
- `pip install --user` 安装到当前用户目录。 macos:`~/Library/Python/3.7/lib/python/site-packages`
- 源码安装
    ```
    cd google-auth
    pip install .
    ```
- 编辑模式: `pip install -e .`就是修改了源码之后不需要重新安装