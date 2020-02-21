# Testing
## 集成测试
- Selenium1
  使用JS注入技术，把一个JS库注入到受访问的网站，并对其进行操作。Selenium测试直接运行在浏览器中，就像真正的用户在操作一样。
- Selenium2
  WebDriver+Selenium1。将浏览器原生的API封装成WebDriver API ，webdriver 是基于 http协议的。
- Nightwatch
- Cypress: 直接运行在浏览器内部
- Robot Framework
    Python语言, 不光测试Web，可以测试FTP，XMPP等
- appium
   扩展了webdriver协议添加对移动设备自动化api扩展而成的
   主要通过Selenium / WebDriver and the OS X Accessibility API等方式控制App的UI
  ```
    npm install -g appium  # get appium
    appium &               # start appium
    # 使用nodejs client（可选）
    npm install wd         # appium nodejs client
    node your-appium-test.js
    # 使用Python client(可选)
    pip install Appium-Python-Client
    pip install pytest（python自动化测试框架）
  ```
- Citrus Framework
Citrus is an open-source framework that will help you automate integration tests for pretty much any messaging protocol or data format. If you have a test flow that requires that your application interact with other services, then APIs and components using functional test tools such as Selenium can’t help.
- RedwoodHQ
- Sahi 
- CasperJS
## 性能测试工具
- tsung
- jmeter
- wrk HTTP 压测推荐
- ab 默认使用HTTP 1.0
- dtrace(mac)
## 性能测试方法论
基准测试Base
Solution A
Solution B
(SA-Base) vs (SB-Base)
## WebDriver API