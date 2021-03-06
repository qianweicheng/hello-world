# ES6
## var let const
## export
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
## import vs require
- require: 运行时加载	CommonJS/AMD 社区方案，提供了服务器/浏览器的模块加载方案。非语言层面的标准。只能在运行时确定模块的依赖关系及输入/输出的变量，无法进行静态优化。
- import: 编译时加载	ESMAScript6+	语言规格层面支持模块功能。支持编译时静态分析，便于JS引入宏和类型检验。动态绑定。
## class、extends、super
## arrow functions 
箭头函数会捕获其所在上下文的 this 值，作为自己的 this 值
也就是可以理解为: 箭头函数没有自己的this, 如果上下文没有this, 则this指向Window对象
lambda 函数的this跟父类绑定
function函数的this跟function绑定
## template string
```
    `Hello, ${var1}`
```
## destructuring
```
let people2 = {
name: 'ming',
age: 20,
color: ['red', 'blue']
}
 
// 变量必须与属性重名
let { name, age } = people2;
let [first, second] = people2.color;
let [a, b, c] = [1, 2, 3];
```
## default 函数默认参数
```
// ES6
function foo(num = 200) {
return num;
}
```
## rest arguments （rest参数）
```
function foo(x, y, ...rest) {
return ((x + y) * rest.length);
}
foo(1, 2, 'hello', true, 7); // 9
```
## Spread Operator （展开运算符）
针对对象: 数组，对象
- 展开操作
let a = [1,2,3];
let b = [0, ...a, 4]; // [0,1,2,3,4]
- 剩余操作
let [a,...b] = [0,1,2,3] //a=0,b=[1,2,3]
```
let color = ['red', 'yellow'];
let colorful = [...color, 'green', 'blue'];
```
## 对象
对象初始化简写
## Promise
- 传统的callback模式存在回调地狱的问题
- then可以多次调用形成一个调用链。每个then返回的都必须是一个promise
- 还是不够简洁，需要创建匿名函数，把返回值一层层传递给下一个then调用。
- 异常不会向上抛出。比如某个then里的函数抛出异常，即使没有写catch，异常也不会向上抛出，在then的调用链外面写try catch是没有效果的。
- 代码调试问题。在某个then的方法中设置断点，然后一步步往下走，你是不能步进到下一个then的方法的。只能每个then里面都设置断点，然后resume run到下一个断点。
```
let promise = new Promise((resolve,reject)=>{
    resolve('success')
    // reject('failed') = throw 'exception'
});
promise.then(res=>{
    console.log('1111:'+res)
    return new Promise((r2,e2)=>{
        r2('r2-e2')
    })
}).then(res=>{
    console.log('2222:'+res)
}).catch(err=>{
    console.log(err)
});
```
## async-await
- async-await 是 Promise的语法糖
- async是一个函数的修饰符，加上async关键词的函数会隐式地返回一个Promise，函数的返回值将作为Promise resolve的值。
- await后面跟的一定是一个Promise，await只能出现在async函数内，await的语义是:必须等到await后面跟的Promise有了返回值，才能继续执行await的下一行代码
```
async function s1(name){
    if (name) {
        return 's1:' + name
    } else {
        throw '名字空'
    }
}
async function test1(){
    let str = await s1('章三')
    console.log(str)
    try{
        let fr2 = await s1('')
        console.log(fr2)
    }catch{
        console.log('捕获到了')
    }
    //返回值自动封装成一个Promise
    return 'end'
}
let r = test1()
r.then(res=>{
    console.log(res)
}).catch(err=>{
    console.err(err)
})
```
## Generators
## 判断字符串里是否包含其他字符串
传统上，JavaScript只有indexOf方法，
新增:
includes : https://developer.mozilla.org...
startsWith : https://developer.mozilla.org...
endsWith : https://developer.mozilla.org...
includes()：返回布尔值，表示是否找到了参数字符串。
## for..of
- Object.keys() - 返回对象可枚举的键
- for(let key in obj)
## Classes - 类
#### 
```
class Rectangle {
    constructor(height, width) {
        this.height = height;
        this.width = width;
    }
    get menu(){
        return this.dishs;
    }
    set menu(dishs){
        this.dishs.push(dish)
    }
    static cook(food){
        console.log(food)
    }

}
let Rectangle = class {
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }
};
```
## Map, Array, Set, Date