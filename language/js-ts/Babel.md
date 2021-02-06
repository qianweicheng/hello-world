# Install
npm install --save-dev @babel/core
npm install --save-dev @babel/core @babel/cli // 安装babel命令行
npm install --save-dev @babel/preset-env // 安装babel转换器


# Babel
`npx babel src --out-dir lib`
`babel src -d lib --presets=es2015`

## 翻译器
babel-preset-es2015
转译器，将es2015版本的js代码转译为es5代码，对于es2016版本的代码或者es2017版本的代码不转译。
5.3、babel-preset-latest
转译器，将最新版本的js代码转译为es5代码。不推荐使用，已经废除。建议使用babel-preset-env代替
5.4、babel-preset-react
转译器，剥离流类型并将JSX转换为createElement调用，主要在转译react代码的时候使用。

## 配置 babel

babel.config.json（官方推荐）
.babelrc 是 .babelrc.json的别名，，
package.json 中创建 “babel” 属性
.babelrc.json
使用 webpack 的 loader 的配置。
也可以使用js文件动态生成，只要文件export导出的符合babel配置即可，但是由于配置是动态生成的，只有在运行时才获取到配置，所以可能会影响缓存以及IDE自动补全等功能。