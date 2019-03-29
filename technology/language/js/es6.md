# ES6
ES2015,ES2016
## export import
1、export与export default均可用于导出常量、函数、文件、模块等
2、你可以在其它文件或模块中通过import+(常量 | 函数 | 文件 | 模块)名的方式，将其导入，以便能够对其进行使用
3、在一个文件或模块中，export、import可以有多个，export default仅有一个
4、通过export方式导出，在导入时要加{ }，export default则不需要
```
// export 输出
var name1="李四";
export { name1}
// import 引入
import {name1} from "/.a.js" 

// export 输出
export class App extends React.Componet {
    // ..code
}

// import 引入
import {App} from './app';

// export default 输出
export default class App extends React.Componet {
    // ..code
}

// 此时import命令可以为引入的类指定任意名字。
import App from './app';
```
## lambda
lambda 函数的this跟父类绑定
function函数的this跟function绑定
## 操作符(...)
针对对象: 数组，对象
- 展开操作
let a = [1,2,3];
let b = [0, ...a, 4]; // [0,1,2,3,4]
- 剩余操作
let [a,...b] = [0,1,2,3] //a=0,b=[1,2,3]
## import vs require
- require: 运行时加载	CommonJS/AMD 社区方案，提供了服务器/浏览器的模块加载方案。非语言层面的标准。只能在运行时确定模块的依赖关系及输入/输出的变量，无法进行静态优化。
- import: 编译时加载	ESMAScript6+	语言规格层面支持模块功能。支持编译时静态分析，便于JS引入宏和类型检验。动态绑定。