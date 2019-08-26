# IMAP
## 命令行登录IMAP邮箱
- 非TLS使用`telnet`
    `telnet imap.126.com 143`
- TLS使用`openssl`
    `openssl s_client -connect imap.126.com:993 -crlf`
## DEMO
- Request
```
# 部分邮件服务商必须在使用`ID`命令
C1 ID ("name" "Edison")
C2 LOGIN edotest1@126.com A123456
C3 CAPABILITY
C4 LIST "" *
C5 STATUS "INBOX" (MESSAGES RECENT UIDVALIDITY)
C6 SELECT "INBOX"
C7 FETCH 1:32 (UID FLAGS)
C8 UID FETCH 200:* (UID FLAGS)
C9 SEARCH UNSEEN
C9 FETCH 1:10 (FULL)
```
- Request & Response
```
C1 ID ("name" "Edison")
* ID ("name" "Coremail Imap" "vendor" "Mailtech" "TransID" "tm0koAC346coSGNd")
C1 OK ID completed
C2 LOGIN edotest1@126.com A1234567
C2 OK LOGIN completed
C3 CAPABILITY
* CAPABILITY IMAP4rev1 XLIST SPECIAL-USE ID LITERAL+ STARTTLS XAPPLEPUSHSERVICE UIDPLUS X-CM-EXT-1
C3 OK CAPABILITY completed
C4 LIST "" *
* LIST () "/" "INBOX"
* LIST (\Drafts) "/" "&g0l6P3ux-"
* LIST (\Sent) "/" "&XfJT0ZAB-"
* LIST (\Trash) "/" "&XfJSIJZk-"
* LIST (\Junk) "/" "&V4NXPpCuTvY-"
* LIST () "/" "&dcVr0pCuTvY-"
* LIST () "/" "&Xn9USpCuTvY-"
* LIST () "/" "&i6KWBZCuTvY-"
* LIST () "/" "F1_updated"
* LIST () "/" "Snoozed"
* LIST () "/" "Archive"
* LIST () "/" "Packages"
* LIST () "/" "&Ti1lhw-"
* LIST () "/" "&2D3eAQ-"
* LIST () "/" "Folder1"
* LIST () "/" "Spambox"
* LIST () "/" "weicheng"
* LIST () "/" "betterx"
* LIST () "/" "F234"
* LIST () "/" "F110"
* LIST () "/" "#002"
C4 OK LIST Completed
C5 STATUS "INBOX" (MESSAGES RECENT UIDVALIDITY)
* STATUS "INBOX" (MESSAGES 267 RECENT 0 UIDVALIDITY 1)
C5 OK STATUS completed
C6 SELECT "INBOX"
* 267 EXISTS
* 0 RECENT
* OK [UIDVALIDITY 1] UIDs valid
* FLAGS (\Answered \Seen \Deleted \Draft \Flagged)
* OK [PERMANENTFLAGS (\Answered \Seen \Deleted \Draft \Flagged)] Limited
C6 OK [READ-WRITE] SELECT completed
```
#### 
C9 FETCH 268:* (UID)
C9 FETCH 200:* (UID FLAGS)

C10 UID FETCH 1433920980:* (UID FLAGS)