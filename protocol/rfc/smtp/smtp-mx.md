# MX
MX 查询出来的这些服务器，都是SMTP服务器，端口号`25`,于暴露给MUA的SMTP服务器不同的是，这些服务器是作为纯粹的MTA来使用，不能作为MSA的用途
查询命令: `dig mx yourdomain`
## 企业邮箱
企业邮箱服务商可以自定义邮件域名，我们可以通过mx记录来判断市面上较大的几个企业邮件服务商,
同一个邮箱服务商的企业邮箱和个人邮箱MX可能不一样
#### Gmail企业邮箱
所有Gmail的邮箱都是一样的MX
- edison.tech
edison.tech	mail exchanger = 1 aspmx.l.google.com.
edison.tech	mail exchanger = 5 alt1.aspmx.l.google.com.
edison.tech	mail exchanger = 10 aspmx3.googlemail.com.
edison.tech	mail exchanger = 10 aspmx2.googlemail.com.
edison.tech	mail exchanger = 5 alt2.aspmx.l.google.com.
edison.tech	text = "google-site-verification=sGM4dmZdcsdhzH27ZMfqI_BjIJKWHX29_1jzGigeQkQ"
- easilydo.com
easilydo.com.		172800	IN	MX	30 alt2.aspmx.l.google.com.
easilydo.com.		172800	IN	MX	40 aspmx2.googlemail.com.
easilydo.com.		172800	IN	MX	10 aspmx.l.google.com.
easilydo.com.		172800	IN	MX	20 alt1.aspmx.l.google.com.
easilydo.com.		172800	IN	MX	50 aspmx3.googlemail.com.
- ink-42.com
ink-42.com.		1800	IN	MX	30 aspmx2.googlemail.com.
ink-42.com.		1800	IN	MX	20 alt2.aspmx.l.google.com.
ink-42.com.		1800	IN	MX	30 aspmx3.googlemail.com.
ink-42.com.		1800	IN	MX	10 aspmx.l.google.com.
ink-42.com.		1800	IN	MX	20 alt1.aspmx.l.google.com.
- gmail.com(个人邮箱MX不一样)
gmail.com.		150	IN	MX	30 alt3.gmail-smtp-in.l.google.com.
gmail.com.		150	IN	MX	20 alt2.gmail-smtp-in.l.google.com.
gmail.com.		150	IN	MX	40 alt4.gmail-smtp-in.l.google.com.
gmail.com.		150	IN	MX	10 alt1.gmail-smtp-in.l.google.com.
gmail.com.		150	IN	MX	5 gmail-smtp-in.l.google.com.