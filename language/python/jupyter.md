# Jupyter
## Install
```
    python3 -m pip install --upgrade pip
    python3 -m pip install jupyter
```
## 修改启动参数
- 创建配置文件:
    ```
        # 也可以手动创建
        jupyter notebook --generate-config
        vim ~/.jupyter/jupyter_notebook_config.py
    ```
- 修改配置文件
    ```
        c.NotebookApp.ip='*' #外部IP地址客户端可以访问
    ```
## 运行
`jupyter notebook [password]`
