# Client
## iOS
## Android
## Fuchsia
主要的想用统一的OS来操作IOT设备，移动设备，PC等。Fuchsia采用Magenta kernel，这是一个“Little Kernel”，与Android，chromeOS采用的 Linux kernel的不同。Magenta kernel 是更轻量，更底层，更通用的
下一代操作系统
## Web
#### 几大流行前端框架:
- VUE
- React (Native)
- Angularjs2
- layui等
#### 工具集
- (ACE)[https://alibaba.github.io/ice]
## 跨平台解决方案
#### 技术
- Web
- 语言转换
- 中间件
- 虚拟机
#### 框架
- PhoneGap/Cordova
    早期浏览器实现比较差，没有进行优化
    CSS 过于复杂，计算起来更耗时
    DOM 提供的接口太有限，使得难以进行优化
- Titanium
- React Native
- Flutter
## 设计模式
#### MVC
两种模式
- User->C->M->V
- User->V->C->M->V（Web）
#### MVP
M<->P<->V
代码/进程跑在一起，V跟P交互频繁，适合桌面客户端等场景
#### MVVM
M<->P<->V
在概念上是真正将页面与数据逻辑分离的模式
真正将前台代码开发者（JS+HTML）与后台代码开发者分离的模式，适合和Web开发