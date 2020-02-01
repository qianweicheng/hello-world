# SPF
RFC7208: Sender Policy Framework (SPF) for Authorizing Use of Domains in Email, Version 1
## 参考文档
https://postmarkapp.com/guides/spf
## 规则
- 验证的是Return-Path,而不是From
- Received-SPF:
  - client-ip
  - envelope-from
  - helo
  - problem
  - receiver
  - identity
  - mechanism
  - name
- Authentication-Results:
  - 里面会有Received-SPF的部分摘要信息
## 局限性
- Keeping SPF records updated as brands change service providers and add mail streams is difficult due to lack of visibility.
- Just because a message fails SPF, doesn’t mean it will always be blocked from the inbox—it’s one of several factors email providers take into account.
- SPF breaks when a message is forwarded.
- SPF does nothing to protect brands against cybercriminals who spoof the display name or “header from” address in their message, which is the more frequently spoofed “from” address since it’s the address most visible to the email recipient.
- 不解决Cross-User问题，需要通过SMTP AUTH解决
- 使用了外部不可信资源（DNS）
- 隐私泄漏