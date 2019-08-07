# IMAP
## 命令行登录IMAP邮箱
#### 非TLS使用`telnet`
> telnet imap.126.com 143
#### TLS使用`openssl`
> openssl s_client -connect imap.126.com:993 -crlf
#### DEMO
- 部分邮件服务商必须在使用`ID`命令
```
C1 ID ("name" "Edison")
C2 LOGIN edotest1@126.com A1234567
C3 CAPABILITY
C4 LIST "" *
* LIST (\HasNoChildren) "/" "A002_updated"
* LIST (\HasNoChildren) "/" "A003"
* LIST (\Archive \HasNoChildren) "/" "Archive"
* LIST (\Junk \HasNoChildren) "/" "Bulk Mail"
* LIST (\Drafts \HasNoChildren) "/" "Draft"
C5 STATUS "INBOX" (MESSAGES RECENT UIDVALIDITY)
C6 SELECT "INBOX"
C7 FETCH 1:32 (UID)
* BYE IMAP4rev1 Server logging out
```
#### CAPABILITY