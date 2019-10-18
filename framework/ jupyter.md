# Jupyter
https://jupyter-notebook.readthedocs.io/en/stable/
Jupyter作为核心，有notebook(web),console, jupyterlab(web)等几种交互方式，有多种kernels(语言)支持，可以自行扩展
## Install&Run
```
核心: pip install jupyter
option1: pip install jupyterlab(JupyterLab is a next-generation web-based)
option2: pip install notebook

jupyter lab
jupyter notebook --ip=0.0.0.0 --port=8888
```
## Config
- OS X: ~/.jupyter/jupyter_notebook_config.py. 添加kernels:
  - $HOME/Library/Jupyter/kernels
  - /Library/Frameworks/Python.framework/Versions/3.7/share/jupyter/kernels
- Linux: /home/USERNAME/.jupyter/jupyter_notebook_config.py
## Multi-language support
https://github.com/jupyter/jupyter/wiki/Jupyter-kernels
- Golang
```
https://github.com/gopherdata/gophernotes
docker run -it -p 8888:8888 gopherdata/gophernotes
```
## 代码执行流程
- jupyter_core负责启动notebook们
- jupyter_client 是嫁接notebook等和kernel的一个桥梁，在manager.py:start_kernel启动一个shell/python
- notebook上启动一个新的kernel
    - notebook.services.sessions.sessionmanager.start_kernel_for_session
    - jupyter_client.multikernelmanager.start_kernel
    - jupyter_client.manager.start_kernel
    - jupyter_client.launcher.launch_kernel
```
buildin.runpy._run_module_as_main
zsh_jupyter_kernel.__main__
traitlets.config.Application.launch_instance
ipykernel.kernelapp.initialize
zsh_jupyter_kernel.kernel.ZshKernel
```
- new一个golang
```
buildin.runpy._run_module_as_main

```
## 启动不同kernel例子
```
['/xxx/python3', '-m', 'ipykernel_launcher', '-f', '~/Library/Jupyter/runtime/kernel-8554f0a5-2e9d-419a-8b07-85f480c2ee5a.json']
['/xxx/python3', '-m', 'zsh_jupyter_kernel', '-f', '~/Library/Jupyter/runtime/kernel-a7af19d4-cea4-48ef-a13e-e68061b78727.json']
['gophernotes', '~/Library/Jupyter/runtime/kernel-08b5ec6c-4fba-4f43-8f0c-071162b64283.json']
```