# React native
继承自android/ios的原生view，建立了一套自己的控件。
https://reactnative.cn
## Install
`brew install watchman flow`
`npm install -g yarn react-native-cli`
升级：
`react-native upgrade`
## Create Project
`react-native init AwesomeProject`
## Run
#### Debug
本地启动一个webserver, 通过watchman监控文件变化，实时编译/打包, 上传到device中去，bundle本身不在apk包里面
- 启动web server，并编译apk: `react-native run-android`
- 只负责启动web server: `npm start`
- `adb shell input keyevent 82` reload or `CMD+M`
>Debug模式下，是否打包bundle不影响热部署，只影响断网环境是否可以运行
#### pre-release 可以把资源放如了apk，但apk本身属于debug模式
`react-native run-android --variant=release`
#### Relese
两种方式:
- 把js打包成bundle放到apk的资源包里，然后安装传统方式
`react-native bundle --platform android --dev false --entry-file index.js --bundle-output android/app/src/main/assets/index.android.bundle --assets-dest android/app/src/main/res/`
`react-native bundle --platform ios --dev false --entry-file index.js --bundle-output RCT.jsbundle`
- 运行`./gradlew assembleRelease`
    关键在于:`apply from: "../../node_modules/react-native/react.gradle"`
    此脚本会编译出一个bundle放在`build/generated/assets/react/release/index.xxx.bundle`,然后将其放入apk中。debug环境由`bundleInDebug`控制是否放入