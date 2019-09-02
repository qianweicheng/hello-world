# Encod&Decod
## Unicode
- 字符平面
- 新版的Unicode一个字符最多四个字节
- 各种语言取substr的时候注意截取
## 存储/传输方式
- UTF-8 就是在互联网上使用最广的一种 Unicode 的实现方式. 将Unicode编码存储/传输
- UTF-16(UCS-2)
- UTF-32(UCS-4)
- GB2312: 1981年5月1日,包括6763个
- GBK编码：1995年12月发布的汉字编码国家标准，是对GB2312编码的扩充，对汉字采用双字节编码。GBK字符集共收录21003个汉字，包含国家标准GB13000-1中的全部中日韩汉字，和BIG5编码中的所有汉字。
- GB18030编码：2000年3月17日发布的汉字编码国家标准，是对GBK编码的扩充，覆盖中文、日文、朝鲜语和中国少数民族文字，其中收录27484个汉字。GB18030字符集采用单字节、双字节和四字节三种方式对字符编码。兼容GBK和GB2312字符集。
## 大头小头
- Little endian: FFFE
- Big endian: FEFF
## 编码方式
- Base64
    每三个字节为一组(24bite),不够后面补0
    然后填充成4个字节，也就是只用低6位，有64个状态；编码后内容增加33%
    标准的base64编码最后一定是4的整数倍长度，不够后面加'=',解码的时候自动去掉
  - 有两种Base64编码规范
    - 标准的base64:A-Za-z0-9+/
    - Urlsafe base64: 又叫百分号编码，是统一资源定位(URL)编码方式。
        URL地址（常说网址）规定数字，字母可以直接使用，另外一批作为特殊用户字符也可以直接用（/,:@等），剩下的其它所有字符必须通过%xx编码处理
        UrlEncode指解决传输问题，不指定编码，它指是讲编码好的字节传递出去
  - 两种Base64编码转换关系
    - +，/分别变成-，_ 
    - 去掉=
## 其他
MySQL中： utf8是ucs-2，utf8mb4是ucs-4