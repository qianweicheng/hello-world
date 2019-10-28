# Definition
## 字段定义
```
WS
SP		= %d32 		        ; space, ASCII value 32
WSP		=  SP / TAB 		; white space
CR		= %d13		        ; carriage return, ASCII value 13
LF		= %d10		        ; new line feed, ASCII value 10
CRLF		= CR LF		    ;  internet standard newline
CWF
FWS		= ([*WSP CRLF] 1*WSP) / obs-FWS ; Folding white space    
HTAB:	= %d9			    ; horizontal tab, ASCII value 9
CFWS		
DQUOTE	= %d34		        ; double quote,  ASCII value34
VCHAR	= %d33-126		    ; visible (printing) character
CHAR	= %d1-127		    ; any 7-bit US-ASCII character, excluding NUL
CTL		= %d0-31/%d127	    ; controls
DIGIT	= %d48-57		    ; 0-9
HEXDIG  = DIGIT/“A”/“B”/“C”/“D”/“E”/“F”
ALPHA	= %d65-90 / %97-122	; A-Z/a-z
specials        =         "(" / ")" /     		; Special characters used in
                          "<" / ">" /    		;  other parts of the syntax
                          "[" / "]" /
                          ":" / ";" /
                          "@" / "\" /
                          "," / "." /
                          DQUOTE
text    =   %d1-9 /        	 ; Characters excluding CR and LF
            %d11 /
            %d12 /
            %d14-127 /
            obs-text
atext   = ALPHA / DIGIT /	    ; Printable US-ASCII
            "!" / "#" /     	; characters not including
            "$" / "%" /    		; specials. Used for atoms.
            "&" / "'" /
            "*" / "+" /
            "-" / "/" /
            "=" / "?" /
            "^" / "_" /
            "`" / "{" /
            "|" / "}" /
            "~"
atom	= [CFWS] 1*atext [CFWS]
ctext	=   %d33-39 /		; Printable US-ASCII
            %d42-91 /	   	; characters not including
            %d93-126 /  	; "(", ")", or "\"
            obs-ctext
dtext           =   %d33-90 /          ; Printable US-ASCII
                    %d94-126 /         ;  characters not including
                    obs-dtext          ;  "[", "]", or "\"
comment	= "(" *([FWS] ccontent) [FWS] ")"
ccontent= ctext / quoted-pair / comment
word    = atom / quoted-string
phrase  = 1*word / obs-phrase
dot-atom-text	= 1*atext *("." 1*atext)
dot-atom 	    = [CFWS] dot-atom-text [CFWS]
quoted-pair	    = “\”(VCHAR/WSP)/ obs-qp
qtext   =   %d33  /     		; Printable US-ASCII
            %d35-91/     	    ; characters not including
            %d93-126/   	    ; “\” or the quote character
            obs-qtext
qcontent        = qtext /quoted-pair
quoted-string   = [CFWS]  DQUOTE *([FWS] qcontent )[FWS]DQUOTE [CFWS]
word    	    = atom / quoted-string
phrase  	    = 1*word / obs-phrase
unstructured 	= (*([FWS] VCHAR) *WSP) / obs-unstruct
```
## 总结
VTEXT: 所有可见字符
QTEXT: VTEXT-"\"和引号两个特殊字符
CTEXT: VTEXT-"()\"三个特殊字符
DTEXT: VTEXT-"[]\"三个特殊字符
ATEXT: VTEXT-Specials
范围: `VTEXT>QTEXT>CTEXT>ATEXT`
## 不推荐但合法的定义
```
obs-NO-WS-CTL   =  %d1-8 /           	; US-ASCII control
                    %d11 /            	 	;  characters that do not
                    %d12 /             	;  include the carriage
                    %d14-31 /        	;  return, line feed, and
                    %d127              	;  white space characters

obs-FWS        = 1*WSP *(CRLF 1*WSP)		; folding white space
obs-qtext      = obs-NO-WS-CTL
obs-phrase     = word *(word / "." / CFWS)
obs-unstruct   = *((*LF *CR *(obs-utext *LF *CR)) / FWS)
obs-qp         = "\" (%d0 / obs-NO-WS-CTL / LF / CR)
```