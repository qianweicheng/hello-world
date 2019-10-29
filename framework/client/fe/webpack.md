# webpack
四要素:
- entry - webpack打包的入口，并非代码执行的入口；
- output - webpack打包后生成的静态资源文件，它是最终会被html引用的文件；
- loader - 对于非js的模块(或说文件)，转化成webpack能够处理的js文件；对于还要进一步处理的js文件进行加工处理；
- plugins - 参与到整个webpack打包的过程（webpack打包的各个生命周期），可与loader结合使用，提供相应/辅助的功能。