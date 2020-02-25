# IMF Body Struct
```
(
    (
        "TEXT" //body type
        "PLAIN" // subtype
        (
            "CHARSET" "US-ASCII"
            "NAME" "001.txt"
        ) // body parameter parenthesized list
        "<cid:001@edison.tech>" // body id
        "This the description"  // body description
        "7BIT" // body encoding
        2279 // body size(编码后的)
        48 // total lines
    )
    (
        "TEXT" 
        "PLAIN" 
        (
            "CHARSET" "US-ASCII" 
            "NAME" "cc.diff"
        ) 
        NIL 
        NIL
        "BASE64" 
        4554
        73
    )
    "MIXED" // multipart subtype
    xxxx  // body parameter
    xxxx  // body disposition
    xxxx // body language
    xxxx // body location
)
```
## demo
```
(
    "image" "jpeg" ("name" "laopo.jpg") 
    NIL NIL 
    "base64" 
    78182 
    NIL
    (
        "inline" ("filename" "abcd")
    )
    NIL
)
```
## demo
```
(
    (
        (
            "Text" "Plain" ("charset" "gb2312") 
            NIL 
            "Notification" 
            "base64" 
            1300
            18 
            NIL NIL NIL
        )
        (
            "Text" "HTML" ("charset" "gb2312") 
            NIL 
            "Notification" 
            "base64" 
            9622 
            125
            NIL NIL NIL
        )
        "Alternative" 
        ("boundary" "------------Boundary-00=_V849676FXJHMYBT8WCW0") 
        NIL NIL
    )
    (
        "Message" "delivery-status" NIL
         NIL 
        "Delivery error report" 
        "7BIT"
        551
        NIL NIL NIL
    )
)
```