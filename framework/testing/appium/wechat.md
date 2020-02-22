# 方案
API方式确定不可靠，决定使用自动化方式。
## adb
`adb shell am start com.tencent.mm/com.tencent.mm.ui.LauncherUI`
`com.alibaba.android.rimet:.biz.LaunchHomeActivity`
`com.huawei.android.launcher:.unihome.UniHomeLauncher`
`uni.cycmsuni:io.dcloud.PandoraEntryActivity`
## Appium框架
[文档](`https://appium.io/docs/en/writing-running-appium/caps/index.html`)
步骤
1. 使用`$ANDROID_HOME/tools/bin/uiautomatorviewer`分析目标程序的界面结构
2. 通过appt工具获取package、activity，cmd运行  `aapt dump badging  xxx.apk`
3. 编写脚本进行自动化处理
4. 启动Appium Server:`appium &`
5. 运行脚本。


## 使用python uiautomator2
这个库底层使用android自带的uiautomator
`pip3 install --pre -U uiautomator2`
```
python3 -m uiautomator2 init
import uiautomator2 as u2  //依赖包
d = u2.connect('10.242.23.215')
# or
d = u2.connect_usb('xxxxx')
```
### 识别元素
`pip3  install --pre weditor`
## script
- 包`selenium.webdriver.common.touch_actions.TouchActions`不可用
- 使用`appium.webdriver.common.touch_action.TouchAction`里面的点击事件
- 如果需要双击可以考虑使用`selenium.webdriver.ActionChains`这个底层的对象