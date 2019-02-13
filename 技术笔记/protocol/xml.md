# XML
## DTD(文档类型定义)
#### 要素
- 元素
    - <!ELEMENT 元素名称 类别>
    - <!ELEMENT 元素名称 (元素内容)>
        只有 PCDATA 的元素： <!ELEMENT 元素名称 (#PCDATA)>
    - 空元素：<!ELEMENT 元素名称 EMPTY>
    - <!ELEMENT note (to,from,header,(message|body))>
- 属性
    <!ATTLIST 元素名称 属性名称 属性类型 默认值>
    <!ATTLIST 元素名称 属性名称 属性类型 #IMPLIED>
- 实体
    XML里有5个预定义转意，HTML里面更多，也可以自定义
    <!ENTITY 实体名称 "实体的值">
    ```
    <!ENTITY writer "Bill Gates">
    <!ENTITY copyright "Copyright W3School.com.cn">
    <author>&writer;&copyright;</author>
    ```
- PCDATA
    PCDATA 的意思是被解析的字符数据（parsed character data）
    可把字符数据想象为 XML 元素的开始标签与结束标签之间的文本，被解析的字符数据不应当包含任何 &、< 或者 > 字符；需要使用 &amp;、&lt; 以及 &gt; 实体来分别替换它们
- CDATA
    CDATA 的意思是字符数据（character data）。
    CDATA 是不会被解析器解析的文本。在这些文本中的标签不会被当作标记来对待，其中的实体也不会被展开。
#### DOCTYPE
引用路径    
- 内部：<!DOCTYPE 根元素 [元素声明]>
    HTML 5: `<!DOCTYPE html>`
    ```
        <?xml version="1.0"?>
        <!DOCTYPE note [
        <!ELEMENT note (to,from,heading,body)>
        <!ELEMENT to      (#PCDATA)>
        <!ELEMENT from    (#PCDATA)>
        <!ELEMENT heading (#PCDATA)>
        <!ELEMENT body    (#PCDATA)>
        ]>
        <note>
            <to>George</to>
            <from>John</from>
            <heading>Reminder</heading>
            <body>Don't forget the meeting!</body>
        </note>
    ```
- 外部：<!DOCTYPE 根元素 SYSTEM "文件名">
    Tsung: `<!DOCTYPE tsung SYSTEM "/usr/local/tsung/share/tsung/tsung-1.0.dtd" >`
    HTML 4.1 strict: `<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">`
## Schema
XML Schema 是 DTD 的继任者
- XML Schema 可针对未来的需求进行扩展
- XML Schema 更完善，功能更强大
- XML Schema 基于 XML 编写
- XML Schema 支持数据类型
- XML Schema 支持命名空间