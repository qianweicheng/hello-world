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