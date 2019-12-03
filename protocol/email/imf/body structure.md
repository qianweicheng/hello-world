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