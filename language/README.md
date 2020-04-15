# Language
## GPPL(General Purpose Programming Language) or GPL(General Purpose Language)
## Common Expression Language -- specification and binary representation
https://github.com/google/cel-spec
https://opensource.google.com/projects/cel
## DSL(Domain Specific Language)
在组内促进了重要问题的沟通(BA,QA,DEV).
### 特征
- 语言特征(language nature), 具备连贯的表达能力.
- 受限的表达力(limited expressiveness), 只支持特定领域所需特征的最小集.
- 专注于特定领域(domain focus), 只有在一个明确的小领域下,才有意义.
### 分类
- 外部DSL.
    通常使用自定义语法(或XML等), 宿主应用会采用文本解析技术, 对外部DSL 脚本进行解析.
    例如: 正则表达式, SQL, Awk.
- 内部DSL.
    通用语言的特定用法, 其脚本是具有特定风格的合法的程序.
    与外部DSL 的区别: 内部DSL 使用可执行的语言编写,然后在该语言中解析.
    例如: Lisp,Rails.
- 语言工作台. 专用的IDE, 用以定义和构建DSL.
### 处理步骤编辑
- DSL脚本；
- 解析脚本；
- 语义模型；
- 生成代码或者执行模型。
### 抽象: 将DSL看做一种处理抽象的方式.
建立抽象的方式是程序库或框架. 通过命令/查询式API调用来操作框架.
- DSL是程序的前端, 提供了不同于命令/查询式API风格的操作方式.
- 程序库成为DSL的”语义模型”.
- 通常以DSL加程序库的方式出现.
- API和DSL的核心区别为: DSL 具有语言性.
### DSL的问题
- 语言噪音. 学习DSL 应该比学习底层模型的代价小.
- 构建成本. 可维护性是重要的考量.
- 语言集中营. 分离关注点来让DSL有清晰的受限范围; 自行构造应从外部获得的东西.
- DSL是”不断演化,尚未完结”的事物.
- 遇到不符合抽象的事物,应该修改抽象,让其更容易的接纳新事物.
## A New Language
### Concept
### 定义一门语言的过程
- 语言的描述——BNF范式
  - 使用LL(1)递归下降词法解析器
  - 词法分析器（lexer）或者扫描器（scanner）： lex等工具
- 抽象语法树（AST）
  - 语言解释分为前后端，前端语言 java,c,php,js。后端主要是指编译器 例如 GJC,GCC 等。
  - 抽象语法树，相当于一个后端解释器给前端定制的一个规范，无论语言规范怎么变动，只需要改变将源代码解析为抽象语法树的解析器就行了，解析抽象语法树的解释器并不用改动。
  - 前端领域使用抽象语法树极为广泛，将js代码转换为抽象语法树后，可以很轻松的对语法树进行分析与优化
  - 转换为AST语法树的工具比较多，v8,Esprima,UglifyJS2,Acorn 等。能转换抽象语法树的也不只是 java,js ,php 等，html,css,sql,json,这些都可转换为抽象语法树
- 文法识别 (解释器)
- [参见llvm](./llvm/llvm.md)
### 抽象语法树作用
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
