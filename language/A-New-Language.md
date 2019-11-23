# A New Language
## Concept
## 定义一门语言的过程
- 语言的描述——BNF范式
  - 使用LL(1)递归下降词法解析器
  - 词法分析器（lexer）或者扫描器（scanner）： lex等工具
- 抽象语法树（AST）
  - 语言解释分为前后端，前端语言 java,c,php,js。后端主要是指编译器 例如 GJC,GCC 等。
  - 抽象语法树，相当于一个后端解释器给前端定制的一个规范，无论语言规范怎么变动，只需要改变将源代码解析为抽象语法树的解析器就行了，解析抽象语法树的解释器并不用改动。
  - 前端领域使用抽象语法树极为广泛，将js代码转换为抽象语法树后，可以很轻松的对语法树进行分析与优化
  - 转换为AST语法树的工具比较多，v8,Esprima,UglifyJS2,Acorn 等。能转换抽象语法树的也不只是 java,js ,php 等，html,css,sql,json,这些都可转换为抽象语法树
- 文法识别 (解释器)
## 抽象语法树作用
- 格式化存储（存储网页，存储sql 语句，描述json 的json）
- 语法检查、格式化、高亮、错误提示、代自动补全
  - ide 功能糖
- 代码混淆
  - uglifyjs
  - CssMinify
- 代码优化
  - webpack 梳理依赖关系
  - amd,cmd 规范相互转换
  - bable 编译 es6
  - CoffeeScript、TypeScript、JSX等转化为原生Javascript

## 工具
http://ast.nln.me/