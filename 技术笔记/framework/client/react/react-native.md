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
#### debug
本地启动一个webserver, 通过watchman监控文件变化，实时编译/打包, 上传到device中去，bundle本身不在apk包里面
- 启动web server，并编译apk: `react-native run-android` or `react-native run-android --variant=release`
- 只负责启动web server: `npm start`
#### relese
直接把js打包成bundle放到apk的资源包里