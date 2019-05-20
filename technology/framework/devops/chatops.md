# Hubot vs Errbot
## 开源地址
https://github.com/errbotio/errbot
https://github.com/hubotio/hubot
## Hubot
#### Install 
```
    npm install -g yo generator-hubot
    mkdir myhubot
    cd myhubot
    yo hubot 
```
#### 源码分析
- bin/hubot -> bin/hubot.js -> index.js(将js包装给CoffeeScript) -> es2015.js(暴露对外对象，初始化Hubot.loadBot)->src/Robot.js
- Robot做了最中要的事情，加载Adapter，脚本等
  - listenerMiddleware
  - responseMiddleware
  - receiveMiddleware
- Middleware.execute({ response: new Response(this, message) }, this.processListeners.bind(this), cb)
- processListeners
- listener.call
  - listener.match
  - listener.callback()
- Response.send/reply/emit
- Adaper.send/reply/emit



user = {"id":"2","name":"Weicheng","room":"Shell"}
self.robot.receive new TextMessage(user, req.body.message)