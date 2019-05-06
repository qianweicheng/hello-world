# Javascript
基础:http://www.w3school.com.cn/jsref/index.asp
高级:http://www.w3school.com.cn/js/index_pro.asp
## 数据类型
- 字符串
- 数字: JavaScript 数字均为 64 位, 转换： Number(value)
- 布尔: Boolean(value);	Boolean.valueOf() 返回原始值
- 数组: http://www.w3school.com.cn/jsref/jsref_obj_array.asp
- 对象:
- Null
- Undefined
#### 其他内置数据类型
Date: http://www.w3school.com.cn/js/js_obj_date.asp
Math: http://www.w3school.com.cn/jsref/jsref_obj_date.asp
RegExp: 
顶层函数: http://www.w3school.com.cn/jsref/jsref_obj_global.asp
## var let const
## import、export
## class、extends、super
## arrow functions 
- 箭头函数会捕获其所在上下文的 this 值，作为自己的 this 值
- 也就是可以理解为: 箭头函数没有自己的this, 如果上下文没有this, 则this指向Window对象
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
```
let color = ['red', 'yellow'];
let colorful = [...color, 'green', 'blue'];
```
## 对象
对象初始化简写
## Promise
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