# Intent Message Format
第一封邮件
- 说法1: 1969年10月，由计算机科学家Leonard K 教授发的一条简短消息
- 说法2: 1971年，美国国防部资助的阿帕网(ARPA)
## RFC
[HTTP Protocol](https://www.w3.org/Protocols/)  
- Internet Message Format
    - RFC561(1973): Standardizing Network Mail Headers
    - RFC680(1975): Message Transmission Protocol
    - RFC733(1977): ARPA.
    - RFC822(1982): Standard for ARPA Internet text messages(正式标准化)
        - RFC1123(1989)， RFC2156(1998)
    - RFC2822(2001): 废弃RFC822
        - RFC5335(2008) Internationalized Email Headers
        - RFC4952(2007) Overview and Framework for Internationalized Email
        - RFC5336(2008) SMTP Extension for Internationalized Email Addresses
        - RFC6530(2012) Overview and Framework for Internationalized Email
    - RFC5322(2008): 废弃RFC2822, [链接](https://www.ietf.org/rfc/rfc5322.txt)
        - RFC6854(2013): Update to Internet Message Format to Allow Group Syntax in the "From:" and "Sender:" Header Fields
- SMTP
    RFC5321(2008) 
- MIME
    RFC2045 MIME Part 1: Format of Internet Message Bodies 
    RFC2046 MIME Part 2: Media Types 
    RFC2047 MIME Part 3: Header Extensions for Non-ASCII Text 
    RFC2048 MIME Part 4: Registration Procedures 
    RFC2049 MIME Part 5: Conformance Criteria and Examples
    RFC4288 
    RFC4289 
RFC4021: Registration of Mail and MIME Header Fields
RFC5322: Internet Message Format. 
RFC6532: Internationalized Email Headers.
RFC6854: Update to Internet Message Format to Allow Group Syntax in the
     "From:" and "Sender:" Header Fields.
## Header
- Header Fields
    name : value CRLF;  name 33 and 126 字节
- Unstructured Header Field Bodies
    没有语法约束
- Structured Header Field Bodies
    有语法约束
- Long Header Fields
  - 每行最多998，建议78字节，(不包括CRLF)
  - 多于998则需要换行"folding", 第二行必须空格(WSB)开始
    ```
        Subject: This is a test
    can be represented as:
        Subject: This
            is a test
    ```
## Body
CR, LF, CRLF, HTAB, SP, WSP, DQUOTE, DIGIT, ALPHA, and VCHAR
- Quoted characters
- Folding White Space and Comments
- Atom
- Quoted Strings
- Miscellaneous Tokens
- Date and Time Specification
- Address Specification
    ```
    address         =   mailbox / group
    mailbox         =   name-addr / addr-spec
    name-addr       =   [display-name] angle-addr
    angle-addr      =   [CFWS] "<" addr-spec ">" [CFWS] /
                        obs-angle-addr
    group           =   display-name ":" [group-list] ";" [CFWS]
    display-name    =   phrase
    mailbox-list    =   (mailbox *("," mailbox)) / obs-mbox-list
    address-list    =   (address *("," address)) / obs-addr-list
    group-list      =   mailbox-list / CFWS / obs-group-list
    ```
## Field Definitions
```
fields  =   *(trace
        *optional-field /
        *(resent-date /
        resent-from /
        resent-sender /
        resent-to /
        resent-cc /
        resent-bcc /
        resent-msg-id))
    *(orig-date /
    from /
    sender /
    reply-to /
    to /
    cc /
    bcc /
    message-id /
    in-reply-to /
    references /
    subject /
    comments /
    keywords /
    optional-field)
```
```
   +----------------+--------+------------+----------------------------+
   | Field          | Min    | Max number | Notes                      |
   |                | number |            |                            |
   +----------------+--------+------------+----------------------------+
   | trace          | 0      | unlimited  | Block prepended - see      |
   |                |        |            | 3.6.7                      |
   | resent-date    | 0*     | unlimited* | One per block, required if |
   |                |        |            | other resent fields are    |
   |                |        |            | present - see 3.6.6        |
   | resent-from    | 0      | unlimited* | One per block - see 3.6.6  |
   | resent-sender  | 0*     | unlimited* | One per block, MUST occur  |
   |                |        |            | with multi-address         |
   |                |        |            | resent-from - see 3.6.6    |
   | resent-to      | 0      | unlimited* | One per block - see 3.6.6  |
   | resent-cc      | 0      | unlimited* | One per block - see 3.6.6  |
   | resent-bcc     | 0      | unlimited* | One per block - see 3.6.6  |
   | resent-msg-id  | 0      | unlimited* | One per block - see 3.6.6  |
   | orig-date      | 1      | 1          |                            |
   | from           | 1      | 1          | See sender and 3.6.2       |
   | sender         | 0*     | 1          | MUST occur with            |
   |                |        |            | multi-address from - see   |
   |                |        |            | 3.6.2                      |
   | reply-to       | 0      | 1          |                            |
   | to             | 0      | 1          |                            |
   | cc             | 0      | 1          |                            |
   | bcc            | 0      | 1          |                            |
   | message-id     | 0*     | 1          | SHOULD be present - see    |
   |                |        |            | 3.6.4                      |
   | in-reply-to    | 0*     | 1          | SHOULD occur in some       |
   |                |        |            | replies - see 3.6.4        |
   | references     | 0*     | 1          | SHOULD occur in some       |
   |                |        |            | replies - see 3.6.4        |
   | subject        | 0      | 1          |                            |
   | comments       | 0      | unlimited  |                            |
   | keywords       | 0      | unlimited  |                            |
   | optional-field | 0      | unlimited  |                            |
   +----------------+--------+------------+----------------------------+
```
- Originator Fields
```
   from            =   "From:" mailbox-list CRLF
   sender          =   "Sender:" mailbox CRLF
   reply-to        =   "Reply-To:" address-list CRLF
```
- Destination Address Fields
```
    to              =   "To:" address-list CRLF
    cc              =   "Cc:" address-list CRLF
    bcc             =   "Bcc:" [address-list / CFWS] CRLF
```
- Identification Fields
```
   message-id      =   "Message-ID:" msg-id CRLF
   in-reply-to     =   "In-Reply-To:" 1*msg-id CRLF
   references      =   "References:" 1*msg-id CRLF
   msg-id          =   [CFWS] "<" id-left "@" id-right ">" [CFWS]
   id-left         =   dot-atom-text / obs-id-left
   id-right        =   dot-atom-text / no-fold-literal / obs-id-right
   no-fold-literal =   "[" *dtext "]"
```
- Informational Fields
```
    subject         =   "Subject:" unstructured CRLF
    comments        =   "Comments:" unstructured CRLF
    keywords        =   "Keywords:" phrase *("," phrase) CRLF
```
- Resent Fields
- Trace Fields