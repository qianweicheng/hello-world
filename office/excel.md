# Excel
## 引用
- 绝对引用: `=$A$1*$A$2` 复制A4中的公式到任何一个单元格其值都不会改变
- 相对引用: 单元格或单元格区域的相对引用是指相对于包含公式的单元格的相对位置
## 公式
- 文本处理
  - SEARCH(find_text,within_text,start_num)返回一个指定字符或文本字符串在字符串中第一次出现的位置，从左到右查找(忽略大小写).支持通配符
  - FIND(find_text,within_text,start_num)：返回一个字符串在另一个字符串中出现的起始位置，大小写敏感，不支持通配符
  - MID(text, start_num, num_chars)，字符串处理substring
  - LEFT，RIGHT
  - REPLACE
  - LEN
- 数学计算
  - SUMIF(range，criteria，sum_range)
  - MOD 取余数
  - INT函数用于舍去数值的小数部分保留整数部分
  - TRUNC
  - ROUND
  - RAND
  - PRODUCT相当于乘
- 统计分析
  - COUNT函数是最常见的统计函数，主要用于统计单元格区域或数组中数值的个数，文本、空白单元格、逻辑值或错误值无法用COUNT函数来统计。
  - COUNTA函数可以返回非空文本的单元格个数
  - COUNTBLANK函数可以计算指定单元格区域中空白单元格的个数
  - COUNTIF(DATA,criteria)
  ```
    1. 返回包含值12的单元格数量      =COUNTIF（DATA,12） 
    2. 返回包含负值的单元格数量     =COUNTIF（DATA，"<0"） 
    3. 返回不等于0的单元格数量 　　=COUNTIF（DATA，"<>0"） 
    4. 返回大于5的单元格数量 　　=COUNTIF（DATA，">5"） 
    5. 返回等于单元格A1中内容的单元格数量 　　=COUNTIF（DATA，A1） 
    6. 返回大于单元格A1中内容的单元格数量 　　=COUNTIF（DATA，">''&A1） 
    7. 返回包含文本内容的单元格数量 　　=COUNTIF（DATA,''*''） 
    8. 返回包含三个字符内容的单元格数量 　　=COUNTIF（DATA，''???''） 
    9. 返回包含单词"GOOD"(不分大小写)内容的单元格数量 　　=COUNTIF（DATA,''GOOD''） 
    10. 返回在文本中任何位置包含单词"GOOD"字符内容的单元格数量 　　=COUNTIF（DATA,"*GOOD*"） 
    11(1). 返回包含以单词"AB"(不分大小写)开头内容的单元格数量 　　=COUNTIF（DATA,"AB*"） 
    11(2). 返回包含以单词"AB"(不分大小写)结尾内容的单元格数量 　　=COUNTIF（DATA,"*AB"） 
    1.  返回包含当前日期的单元格数量 　　=COUNTIF（DATA，TODAY()） 
    2.  返回大于平均值的单元格数量 　　=COUNTIF（DATA，">"&AVERAGE(DATA)) 
    3.  返回平均值上面超过三个标准误差的值的单元格数量 　　=COUNTIF（DATA,">"&AVERAGE(DATA)+STDEV(DATA)*3) 
    4.  返回包含值为3或-3的单元格数量 　　=COUNTIF（DATA，3）+COUNIF（DATA，-3） 
    5.  返回包含值;逻辑值为TRUE的单元格数量 　　=COUNTIF（DATA，TRUE） 
    6.  统计区域中不为空的单元格个数（数值,文本,空格都算）——（上述第3条：文本也算不等于0，空格不算）=Countif(DATA,"<>") 
    7.  只统计文本单元格数量，不统计数值和空格——（上述第7条统计含空格） =COUNTIF(DATA,"><") 
    8.  求真空单元格单个数:=COUNTIF(data,"=")
    9.  真空+假空单元格个数:=COUNTIF(data,"")相当于countblank()函数
    10. 非真空单元格个数:=COUNTIF(data,"<>")相当于counta()函数
    11. 文本型单元格个数:=COUNTIF(data,"*")假空单元格也是文本型单元格
    12. 区域内所有单元格个数:=COUNTIF(data,"<>""")
    13. 逻辑值为TRUE的单元格数量：=COUNTIF(data,TRUE)
    ```
  - AVERAGEIF
  - SUMIF
- IF(logical_test,value_if_true,value_if_false),
- ISERROR（）函数是用来返回TRUE或FALSE的，与IF结合使用是一个经典的防报错公式
- 逻辑信息函数，AND/OR函数
- 时间，TODAY、NOW、YEAR、MONTH、DAY、WEEKDAY
  - TODAY(),NOW(),YEAR/MONTH(TODAY())
  - DATEIF计算时间差
- 查找引用函数
  - MATCH(lookup_value, lookup_array, [match_type]) 返回符合特定值特定顺序的项在数组中的相对位置.
  - INDEX(values,row_index,col_index)：在给定的单元格区域中，返回特定行列交叉处单元格的值或引用.一般与MATCH结合
  - VLOOKUP (lookup_value,table_array,col_index_num,range_lookup)，HLOOKUP
  - LOOKUP(lookup_value,lookup_vector,result_vector)，类似Map做key-value映射
- IS类判断函数
  - ISBLANK
  - ISERR
  - ISLOGICAL
  - ISNA
  - ISNOTTEXT
  - ISNUMBER
  - ISREF
  - ISTEXT
