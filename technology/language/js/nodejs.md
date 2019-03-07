# NodeJS
三种主要包管理: npm,yarn,pnpm
## NPM：NodeJS自带的包管理器
npm-shrinkwrap.json 记录确切的版本号，但不记录内容，存在安全风险。
npm3 会采用扁平化的依赖目录结构，所有node_modules 都存放在顶层目录下
npm5 开始使用了package-lock.json 基本抵消了yarn的优势
    加快了npm install 的速度，因为 package-lock.json 文件中已经记录了整个node_modules文件的树状结构，甚至连模块的下载地址都记录了，再重新安装的时候只需要直接下载文件即可
- npm 国内镜像: npm install cnpm（淘宝镜像）
- 安装之后锁定包的版本(package-lock.json)
    手动更改package.json文件安装将不会更新包，直接执行`npm install`**不会**安装新指定的版本,想要更新只能使用:`npm install xxx@1.0.0`这种方式来进行版本更新package-lock.json
- 开发测试的静态服务器
    - webpack-dev-server
    - http-server: 
        npm i -g http-server
        运行：hs->http-server
- 安装路径: `/usr/local/lib/node_modules/`,软连接到`/usr/local/bin`
#### 常用命令
```
npm init 创建package.json
npm install 根据当前package.json 安装所有依赖(递归)
npm install 
        --save选项为默认行为
        -g 全局安装
        -P 安装到dependencies
        -D devDependencies
        -O optionalDependencies
        --no-save 不保存到dependencies， 默认save会生成package-lock.json 
npm uninstall
npm update create-react-app        
npm ls 
    查看package.json和node_modules里面安装的所有模块, 
    -g 查看全局安装的模块
    --depth=0 查看顶级直接依赖模块
npm update xxx
npm run
npm start 对象中没有定义 "start" 属性， 默认执行 node server.js 命令。
npm start === npm run start, 类似的还有stop, test
```    
## Yarn [参考](https://yarnpkg.com/zh-Hans/docs/migrating-from-npm)
    Facebook出品的一个类似npm的包管理器。[npm vs yarn](https://yarnpkg.com/zh-Hans/docs/migrating-from-npm)
    安装路径:`~/.config/yarn/global/node_modules`
    软连接到:`/usr/local/bin`
## pnpm
## 模块管理
- [Webpack](https://github.com/ruanyf/webpack-demos)
    [参考](https://www.cnblogs.com/wangyingblog/p/7027540.html)
    - Loaders are preprocessors which transform a resource file of your app (more info) before Webpack's building process.
    - 打包方式（每个module会封装到 eval 里包裹起来执行，并且会在末尾追加注释 ）
        source-map	生成一个SourceMap文件.
        hidden-source-map	和 source-map 一样，但不会在 bundle 末尾追加注释.
        inline-source-map	生成一个 DataUrl 形式的 SourceMap 文件.
        eval-source-map	每个module会通过eval()来执行，并且生成一个DataUrl形式的SourceMap.
        cheap-source-map	生成一个没有列信息（column-mappings）的SourceMaps文件，不包含loader的 sourcemap（譬如 babel 的 sourcemap）
        cheap-module-source-map	生成一个没有列信息（column-mappings）的SourceMaps文件，同时sourcemap也被简化为只包含对应行的
        >webpack 不仅支持这 7 种，而且它们还是可以任意组合上面的inline、hidden关键字
- Browserify
    Browserify本身不是模块管理器，只是让服务器端的CommonJS格式的模块可以运行在浏览器端。这意味着通过它，我们可以使用Node.js的npm模块管理器
- Bower
    为模块的安装、升级和删除，提供一种统一的、可维护的管理模式。
- Component
- Duo
## nvm
https://github.com/creationix/nvm/blob/master/README.md
- Install: `curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.34.0/install.sh | bash`
- Source: `source ~/.bashrc`
- Help: `nvm --help`
```
  nvm install node                      Install 最新版本
  nvm install 8.0.0                     Install a specific version number
  nvm use 8.0                           Use the latest available 8.0.x release
  nvm run 6.10.3 app.js                 Run app.js using node 6.10.3
  nvm exec 4.8.3 node app.js            Run `node app.js` with the PATH pointing to node 4.8.3
  nvm alias default 8.1.0               Set default node version on a shell
  nvm alias default node                Always default to the latest available node version on a shell
```
> 使用前最好清理下node_modules
