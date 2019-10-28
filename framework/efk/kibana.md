kibana搜索语法
1. 直接短语搜：
    hello 全文搜索
    hello world 搜索hello，或者world
    "hello world"， 添加双引号表示精确匹配

2. 限定字段全文搜索：field:value
    字段本身是否存在
    _exists_:http：返回结果中需要有http字段
    _missing_:http：不能含有http字段
    field支持层次。
    {
        level1_a:{
            level2:"xxx"
        },
        level1_b:{
            xxx:yyy
        }
    }
    搜索如下： level1_a.level1:xxx

3. 模糊搜索：
    ? 匹配单个
    * 匹配0或者多个
    ~ Fuzzy Searches模糊词查询： key~[0-1模糊系数] 相似度，1表示完全匹配， test~0.8
    ~ Proximity Searches邻近词查询, "hello world"~10 这两个单词中间可以有一部分内容（这部分内容通过字符个数限制）
    {}[] Range Searches范围查询, 大括号表示不包含最小值和最大值, 方括号表示包含最小值和最大值，
        如：version:[1 TO 3]
    ^ Boosting a Term词语相关度查询，如果单词的匹配度很高，一个文档中或者一个字段中可以匹配多次，那么可以提升该词的相关度。使用符号^提高相关度

3. Boolean Operator布尔操作符 AND OR NOT, 必须大写
    + 必须包含后面的搜索条件，类似AND
    - 排除，类似NOT
    如：+apache -jakarta test aaa bbb 表示结果中必须存在apache，不能有jakarta，剩余部分尽量都匹配到
    () 分组

4. 特殊字符  + - && || ! ( ) { } [ ] ^ " ~ * ? : \
    如： \(1\+1\)\=2 用来查询 (1+1)=2
