# Request For Comments(RFC)
官网: https://tools.ietf.org/html/ or https://tools.ietf.org/rfc/
## 语法规范
- 巴科斯范式 BNF
- 扩展的巴科斯范式 ABNF
#### RFC
- RFC2234(1997)
- RFC4234(2005) 废弃前者
- RFC5234(2008) 废弃前者 [地址](https://tools.ietf.org/html/rfc5234)
- RFC7405(2014) 更新前者
#### Rule Definition
- Rule Naming: 大小写不敏感
- Rule Form: `name = elements crlf`
- Terminal Values
  ```
        b           =  binary
        d           =  decimal
        x           =  hexadecimal
   Hence:
        CR          =  %d13
        CR          =  %x0D
        CRLF        =  %d13.10
  ```
- External Encodings
#### Operators
- Concatenation: Rule1 Rule2
  ```
        foo         =  %x61           ; a
        bar         =  %x62           ; b
        mumble      =  foo bar foo
  ```
- Alternatives: Rule1 / Rule2
- Incremental Alternatives: Rule1 =/ Rule2
    相当于a+=b
    ```
         ruleset     =  alt1 / alt2
         ruleset     =/ alt3
         ruleset     =/ alt4 / alt5
   is the same as specifying
         ruleset     =  alt1 / alt2 / alt3 / alt4 / alt5
    ```
- Value Range Alternatives: %c##-##
- Sequence Group
    ```
         elem (foo / bar) blat
   matches (elem foo blat) or (elem bar blat), and
         elem foo / bar blat
   matches (elem foo) or (bar blat).
    ```
- Variable Repetition:  *Rule
    ```
         <a>*<b>element
        where <a> and <b> are optional decimal values, indicating at least
        <a> and at most <b> occurrences of the element.
    ```
- Specific Repetition:  nRule
    ```
   A rule of the form:
         <n>element
   is equivalent to
         <n>*<n>element
    ```
- Optional Sequence:  [RULE]
  ```
     Square brackets enclose an optional element sequence:
         [foo bar]
        is equivalent to
         *1(foo bar).
  ```
- Comment:  ; Comment