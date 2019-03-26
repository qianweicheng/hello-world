# Mock
`npm install mockjs`
```
var Mock = require('mockjs');
var mock = Mock.mock({
    ...
})
```
## 配置
Mock.setup({
    timeout:200
})
## Basic
直接生产制定类型的数据，可以通过参数控制格式

```
var bool1 = Random.boolean();      //true false各一半
var bool2 = Random.boolean(1,2，false)    //1/3的可能性是false 2/3是true
Random.date(format?)
```
## Random
如下类型
Basic	boolean natural integer float character string date datename now
Date	date datetime time now
Image	image dataImage
Color	color hex rgb rgba hsl
Text	paragraph sentence word title cparagraph csentence cword ctitle
Name	first last name cfirst clast cname
Web	url domain email ip tld
Address	area region city county zip
Helper	capitalize upper lower pick shuffle
Miscellaneous	guid id

```
var Random = Mock.Random;
var em1 = Mock.email();
var em2 = Mock.mock('@email');
var em3 = Mock.mock({
    email:'@email'
})
```
## 数据占位符DPD
- 用@标识符标识后面的字符串是占位符
- 占位符的值是从Mock.Random方法中引用的
- 可以通过Mock.Random.extend()来扩展自定义占位符
- 占位符可以引用数据模板中的属性
- 占位符优先引用数据模板中的属性
- 占位符支持相对路径和绝对路径

