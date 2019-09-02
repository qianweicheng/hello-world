# Checking list
- Group address支持
- 代发代收邮件导致的Sender/From不一致
- 邮件Part嵌套问题
- 邮件安全(垃圾邮件检查spf)
- 对于有UIDNEXT的邮箱， 可以有效探测是否有新邮件，从而较少网络请求次数（RFC2060）
- 对于有UIDVALIDITY, 检测Folder 是否重新创建， 防治ABA问题（RFC2060）
- HIGHESTMODSEQ 可以用来检查之前的Flag是否有变化,(RFC4549) If the client receives NOMODSEQ OK untagged response instead of
   HIGHESTMODSEQ, it MUST remove the last known HIGHESTMODSEQ value from
   its cache and follow the more general instructions
- STATUS 命令谨慎使用
# CAPABILITY
- CAPABILITY需要记录两次，
  - 未登录的情况，主要用来获取登录方式
  - 登录的情况（重要），探测各种插件功能
- SELECT之后，记录支持的各种flag
  - Flag的能力探测（比如yahoo），可以标志是否$Forwarded等自定义
- XLIST和SPECIAL-USE是两个类似的东西，
  - 直接用rfc6154， 获取 Folder的Type（比如网易，QQ等）
- CHILDREN: 目前网易邮箱没有CHILDREN
- COMPRESS 压缩
-  If the action implies opening a new mailbox (any operation that
         operates on messages), open the mailbox.  Check its UID
         validity value (see Section 4.1 for more details) returned in
         the UIDVALIDITY response code.  If the UIDVALIDITY value
         returned by the server differs, the client MUST empty the local
         cache of the mailbox and remove any pending "actions" that
         refer to UIDs in that mailbox (and consider them failed).  Note
         that this doesn't affect actions performed on client-generated
         fake UIDs (see Section 5).

- Perform the action.  If the action is to delete a mailbox
         (DELETE), make sure that the mailbox is closed first (see also
         Section 3.4.12 of [RFC2683]).