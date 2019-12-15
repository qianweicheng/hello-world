# Mailcore2
## 发布的时候需要修改的宏定义
- MCAssert.c: MCDisabledAssert
- MCLog.c:  MCLogEnabled
## AbstractPart
- IMAPPart
- AbstractMessagePart:增加了header和mainPart
    - IMAPMessagePart:增加了size
- AbstractMultipart:增加parts()方法用来存放子part
    - IMAPMultipart
## 下载解析
(mailcore2)
    fetchMessages
(libetpan)
    mailimap_fetch
    mailimap_fetch_changedsince
    mailimap_fetch_qresync_vanished
    mailimap_parse_response
    ...
(mailcore2)
    msg_att_handler