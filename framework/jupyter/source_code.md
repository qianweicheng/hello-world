# 源码分析
## library
- jupyter
- notebook
- jupyter_client
- ipykernel
- tornado
## Application
Jupyter_core:JupyterApp(Application)
    jupyter_client:KernelApp(JupyterApp)
    jupyter_client:RunApp(JupyterApp, JupyterConsoleApp):
    QtConsoleApp:JupyterQtConsoleApp(JupyterApp, JupyterConsoleApp):
    jupyter_console:ZMQTerminalIPythonApp(JupyterApp, JupyterConsoleApp)
    notebook:NotebookApp(JupyterApp)
    jupyterlab:LabExtensionApp(JupyterApp)
## 新建一个Kernel
POST http://localhost:8888/api/contents
    /api/contents/xxx.ipynb
IOLoopKernelManager:connect_xxx
    connect_xxx = as_zmqstream(KernelManager.connect_xxx)
        ConnectionFileMixin:connect_xxx 连接到ZMQ server
    return ZMQStream(socket, self.loop)