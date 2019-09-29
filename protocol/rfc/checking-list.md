# 优化列表
- ID 命令规范：a003 ID ("name" "edison mail for android" "version" "1.2.3" "vendor" "edison" "contact" "support@edison.tech")
  - 需要填写contact，方便邮件服务上有修改主动通知我们。
- 登录优化，添加mx查询，识别企业邮箱
- 发送邮件的时候
  - 添加一个“X-Mailer: Android/iOS/Desktop(1.0.0)“,方便后续做统计分析
  - 添加一个”X-Edison-MID(用Message-ID也可以): UUID", 改进auto-cope-on-sent功能（通过`UID Search HEADER X-Edison-Id xxxxx`代替配置文件）
- 使用XLIST和LIST替代配置文件获取Folder list及其Flag， 只是提升，不能彻底解决问题
- Group address支持
- 邮件Part嵌套问题(Desktop 目前没有实现)
- 特殊邮件标记
  - 代发代收邮件导致的Sender/From不一致
  - 邮件安全(垃圾邮件检查spf)，对于SPF/DKIMDMARC验证失败的邮件进行标注
- IMAP相关优化见imap/rfc3501.md

