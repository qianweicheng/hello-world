大小写敏感
使用缩进表示层级关系
缩进时不允许使用Tab键，只允许使用空格。
缩进的空格数目不重要，只要相同层级的元素左侧对齐即可

对象：键值对的集合，又称为映射（mapping）/ 哈希（hashes） / 字典（dictionary）
数组：一组按次序排列的值，又称为序列（sequence） / 列表（list）
纯量（scalars）：单个的、不可再分的值

对象两种表示方式：
1) obj:
     key1:value1
     key2:value2
2) obj:{key1:value1, key2:value2}
数组两者表示方式:
1) arr:[1,2,3]
2) arr:
    - 1
    - 2
    - 3

null用~表示  parent: ~ 

字符串默认不使用引号表示。
单引号和双引号都可以使用，双引号不会对特殊字符转义。
s1: '内容\n字符串'
s2: "内容\n字符串"
JSON: { s1: '内容\\n字符串', s2: '内容\n字符串' }

单引号之中如果还有单引号，必须连续使用两个单引号转义。
str: 'labor''s day' 

字符串可以写成多行，从第二行开始，必须有一个单空格缩进。换行符会被转为空格。
str: 这是一段
  多行
  字符串
JSON: { str: '这是一段 多行 字符串' }

多行字符串可以使用|保留换行符，也可以使用>折叠换行。
this: |
  Foo
  Bar
that: >
  Foo
  Bar
JSON:{ this: 'Foo\nBar\n', that: 'Foo Bar\n' }

+表示保留文字块末尾的换行，-表示删除字符串末尾的换行。
s1: |
  Foo

s2: |+
  Foo


s3: |-
  Foo
JSON:{ s1: 'Foo\n', s2: 'Foo\n\n\n', s3: 'Foo' }


锚点&和别名*，可以用来引用。
&用来建立锚点（defaults），<<表示合并到当前数据，*用来引用锚点。
defaults: &defaults
  adapter:  postgres
  host:     localhost

development:
  database: myapp_development
  <<: *defaults

test:
  database: myapp_test
  <<: *defaults

  等同于下面的代码。
  defaults:
  adapter:  postgres
  host:     localhost

development:
  database: myapp_development
  adapter:  postgres
  host:     localhost

test:
  database: myapp_test
  adapter:  postgres
  host:     localhost