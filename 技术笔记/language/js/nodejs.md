#### nodejs 常用命令
npm cnpm（淘宝镜像）

####初始化
npm init 创建package.json
npm install 根据当前package.json 安装所有依赖(递归)
npm install 
    -g 全局安装
    -P 默认，安装到dependencies
    -D devDependencies
    -O optionalDependencies
    --no-save 不保存到dependencies， 默认save
会生成package-lock.json    
npm init, npm i,
npm start === npm run start, 类似的还有stop, test
####依赖查看
npm ls 查看package.json里面定义的，和node_modules里面安装的所有模块
     -g 查看全局安装的模块
     --depth=0 查看顶级直接依赖模块
    当package.json 里面没有包含，但require里面引用了的话，就会报警。
用于坚持本地安装但未放置到package.json的情况
####更新
npm update xxx
####运行
npm run
npm start 对象中没有定义 "start" 属性， 默认执行 node server.js 命令。
####开发测试的静态服务器
- webpack-dev-server
- http-server: 
    npm i -g http-server
    运行：hs->http-server
####Webpack
https://www.cnblogs.com/wangyingblog/p/7027540.html
eval	每个module会封装到 eval 里包裹起来执行，并且会在末尾追加注释 //@ sourceURL.
source-map	生成一个SourceMap文件.
hidden-source-map	和 source-map 一样，但不会在 bundle 末尾追加注释.
inline-source-map	生成一个 DataUrl 形式的 SourceMap 文件.
eval-source-map	每个module会通过eval()来执行，并且生成一个DataUrl形式的SourceMap.
cheap-source-map	生成一个没有列信息（column-mappings）的SourceMaps文件，不包含loader的 sourcemap（譬如 babel 的 sourcemap）
cheap-module-source-map	生成一个没有列信息（column-mappings）的SourceMaps文件，同时sourcemap也被简化为只包含对应行的
>webpack 不仅支持这 7 种，而且它们还是可以任意组合上面的inline、hidden关键字