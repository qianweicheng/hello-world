# 源码分析
## library
- jupyter
- notebook
- jupyter_client
- ipykernel
- tornado
## Application
Jupyter_core:JupyterApp(Application)的子类
    jupyter_client:KernelApp(JupyterApp)
    jupyter_client:RunApp(JupyterApp, JupyterConsoleApp):
    QtConsoleApp:JupyterQtConsoleApp(JupyterApp, JupyterConsoleApp):
    jupyter_console:ZMQTerminalIPythonApp(JupyterApp, JupyterConsoleApp)
    notebook:NotebookApp(JupyterApp)
    jupyterlab:LabExtensionApp(JupyterApp)
## 代码执行流程
注意需要调试的话使用`notebook`,而不是`jupyter notebook`
- jupyter_core负责启动notebook们，并且准备各种目录
- jupyter_client 是嫁接notebook等和kernel的一个桥梁，在manager.py:start_kernel启动一个shell/python
- notebook上启动一个新的kernel
  - 创建阶段
    - webbrowser发起请求
      ```
      POST   /api/contents
      ```
    - notebook.services.sessions.sessionmanager.create_session
    - notebook.services.sessions.sessionmanager.start_kernel_for_session
    - jupyter_client.multikernelmanager.start_kernel
    - jupyter_client.IOLoopKernelManager(KernelManager)
    - jupyter_client.manager.start_kernel: 这里准备好启动kernel的配置，并保存成json文件
        ```
        IOLoopKernelManager:connect_xxx
        connect_xxx = as_zmqstream(KernelManager.connect_xxx)
        ConnectionFileMixin:connect_xxx 连接到ZMQ server
        return ZMQStream(socket, self.loop)
        ```
    - jupyter_client.launcher.launch_kernel。 最后在这里启动`proc = Popen(cmd, **kwargs)`
       启动shell/python跟golang的区别，有两种方式:
      - 一种是直接通过ipython进行包装，ipython跟ZMQ通信，ipython内部跟对应的kernel交互。如python/shell等，实现简单
      - 一种是通过协议通信，如golang等
      ```
        ['/xxx/python3', '-m', 'ipykernel_launcher', '-f', '~/Library/Jupyter/runtime/kernel-8554f0a5-2e9d-419a-8b07-85f480c2ee5a.json']
        ['/xxx/python3', '-m', 'zsh_jupyter_kernel', '-f', '~/Library/Jupyter/runtime/kernel-a7af19d4-cea4-48ef-a13e-e68061b78727.json']
        ['gophernotes', '~/Library/Jupyter/runtime/kernel-08b5ec6c-4fba-4f43-8f0c-071162b64283.json']
      ```
    - 启动对于zsh shell/python之类的kernel则
      ```kernel需要实现这三个函数
        IPKernelApp.launch_instance(kernel_class = ZshKernel)
            app = cls.instance(**kwargs)
            app.initialize(argv)
            app.start()
      ```
    - 启动kernel的时候会根据上一步配置的端口，启动一个ZMQ的实例.
    - 当浏览器发起ws请求之后，初始化一个`ZMQChannelsHandler(AuthenticatedZMQStreamHandler)`
      ```
      全局的notebook.services.kernels.kernelmanager.MappingKernelManager有个字典，通过kernelid找到对应的kernel配置文件，然后初始化4个socket,用于链接kernel监听的端口
      ```
    - 执行阶段主要通过ws进行:notebook.servies.kernels.handlers.on_message
  - 浏览器角度
    - `POST    /api/contents/`新建一个ipynb，也就是session
    - `GET    /api/contents/` 刷新各个ipynb的状态，也就是session的状态
    - `/notebooks/Untitled.ipynb` 点击已有的则直接到这一步，进入到一个session
    - `/api/session`， 获取到这个session对应kernel的详细信息
    - `/channels?session_id=xxx` 建立websocket，进行实时通信