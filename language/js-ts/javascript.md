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
## 其他内置数据类型
Date: http://www.w3school.com.cn/js/js_obj_date.asp
Math: http://www.w3school.com.cn/jsref/jsref_obj_date.asp
RegExp: 
顶层函数: http://www.w3school.com.cn/jsref/jsref_obj_global.asp
## apply vs call vs bind
call和apply可以用来重新定义函数的执行环境，也就是this的指向；call和apply都是为了改变某个函数运行时的context，即上下文而存在的，换句话说，就是为了改变函数体内部this的指向。
语法：foo.call(this, arg1,arg2,arg3) == foo.apply(this, arguments) == this.foo(arg1, arg2, arg3);
#### bind
```
var test=function(a,b,c){
    console.log("a="+a,"b="+b,"c="+c);
}
var o={
    x:1
}
test.bind(o)(1,2,3) //a=1 b=2 c=3
test.bind(o,1)(2,3) //a=1 b=2 c=3
test.bind(o,1)(); //a=1 b=undefined c=undefined
test.bind(o,1,2)();//a=1 b=2 c=undefined
test.bind(o,1,2,3)(); //相当于调用test(1,2,3)   a=1 b=2 c=3
```