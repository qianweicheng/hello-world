#### ES6(ES2015/ES2016)
  ES5: 传统JS，几乎所有浏览器都支持
  ES6: 最新版本的浏览器支持大部分标准，但兼容性差
#### CommonJS
>   CommonJS是同步加载模块. CommonJS是一个更偏向于服务器端的规范。NodeJS采用了这个规范。CommonJS的一个模块就是一个脚本文件。require命令第一次加载该脚本时就会执行整个脚本，然后在内存中
生成一个对象。注意上面用require加载时写的是相对路径，让Nodejs去指定路径下加载模块。如果省略相对路径，默认就会在node_modules文件夹下找hi模块
``` a.js
var str = 'Hi';
function sayHi(name) {
  console.log(str + ', ' + name + '!');
}
module.exports = sayHi;
```
``` b.js
var Hi = require('./hi');
Hi('Jack');     // Hi, Jack!
```
#### AMD
>   AMD是”Asynchronous Module Definition”的缩写，即”异步模块定义”
define(id, [depends], factory);  
require([module], callback);
```
a.js
define(['dependenceModule'], function() {
  var add = function(x, y) {
    return x + y;
  }
  return  {
    add: add
  }
})
```
```
b.js
require(['math'], function(math) {
  math.add(2, 3);
})
```
#### CMD
>  CMD 推崇依赖就近，AMD 推崇依赖前置。AMD 是提前执行，CMD 是延迟执行
```
define(function(require, exports, module) {
  var a = require('./a');
  a.doSomething();
  var b = require('./b');
  b.doSomething();
})
```