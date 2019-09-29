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
C2 LOGIN edotest1@126.com A1234567
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
C5 STATUS "INBOX" (MESSAGES RECENT UIDNEXT UIDVALIDITY UNSEEN)
* STATUS "INBOX" (MESSAGES 267 RECENT 0 UIDNEXT 100 UIDVALIDITY 1 UNSEEN 2)
C5 OK STATUS completed
C6 SELECT "INBOX"
* 267 EXISTS
* 0 RECENT
* OK [UIDVALIDITY 1] UIDs valid
* FLAGS (\Answered \Seen \Deleted \Draft \Flagged)
* OK [PERMANENTFLAGS (\Answered \Seen \Deleted \Draft \Flagged)] Limited
C6 OK [READ-WRITE] SELECT completed
```

## PLUGINS
SASL-IR 一种安全验证插件
X-MSG-EXT
OBJECTID: 类似message-id，folder之间移动保持不变
ESEARCH: 返回UID最大/最小/总数， 主要用于控制返回条数，用来翻页
LIST-STATUS
LIST-EXTENDED
LOGIN-REFERRALS
WITHIN
ENABLE
AUTH=LOGIN vs AUTH=PLAIN
## IMAP LOGIN
- Login Gmail
https://developers.google.com/gmail/imap/xoauth2-protocol
```
echo -n "user=lucky20191123@gmail.com\x01auth=Bearer ya29.ImCRB89jLjPMTmoKU8izlZP9b-VaT84Bd3-S3KJKfkI51Upb6IxWAZY8V3tad61tIOF7ESjD6wA3-AFyiB9QmwRjB35zrksboVu0MifHG5uo2vdUcboDWV4KZqq6pFx08fE\x01\x01" | base64
```
```OK
A01 AUTHENTICATE XOAUTH2 dXNlcj13ZWljaGVuZ0BlZGlzb24udGVjaAFhdXRoPUJlYXJlciB5YTI5LkdsdHlCeDJWX1hWSGZDQm44Rk9ReW53dGVPN3FuSkdfTzRjeUVxYmtvRkFIcUNWZ29HTVRMVUlIN2RER3JxWmV4Rmxfc1lhdnlJNGpicTQyTVFXSkVNTWtrUmxCMlNSNktXWGJoRUI3YXV3TWNweDFRc0JDYkhUb21qc2IBAQ==
```


C9 FETCH 268:* (UID)
C9 FETCH 200:* (UID FLAGS)

C10 UID FETCH 1433920980:* (UID FLAGS)
3 STORE 1:2 +FLAGS (\Deleted)

## SMTP LOGIN
`echo -n "\x00username\x00password" | base64`
```
EHLO
AUTH LOGIN two steps
AUTH PLAIN username&pwd
```