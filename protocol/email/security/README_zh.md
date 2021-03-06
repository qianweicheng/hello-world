# 邮件安全
- Spam垃圾广告推送等（对个人危害相对较小)
  - 不通数据来源合并导致的错发邮件
  - 图片垃圾，为了逃避基于文本的垃圾邮件检查。
  - 空邮件，
    - 为了探测有效邮件地址
    - 软件错误
    - 其实包含了隐藏内容，赚流量的
- 钓鱼邮件
  - 钓鱼邮件内容分类
    - 安全警告
    - 休假/病假政策调整
    - UPS快递单号
    - 突发新闻
    - 已尝试为您投递包裹
    - 请更新医疗信息
    - 更改密码
    - 请立刻验证密码
    - 异常登录行为警告
    - 必须立刻采取行动
- 隐私安全
  - 泄露发件人IP地址（发件人的真实IP会出现在邮件头里面，然后可以通过IP定位。部分SMTP服务商会保护发件人信息，比如通过Gmail网页版发出的）
  - 跟踪收信人IP地址和行为(可以通过tracking技术知道收件人在何时何地打开邮件，打开多少次)
## 邮件安全攻击方式
- 暴力破解密码
- 直接通过XSS/CSRF等方式窃取session（web端）
- 域名相似攻击:`biṇance.com vs binance.com` （太惊悚了U+1E47）
- 名字冒充(类似上一条)：取一个跟某人一样或相似的Display Name或者username。这是最没技术含量的方式，但数量不少。
- 正文中，文本上的url和实际url不一样
- 附件里面带有恶意软件
- 伪造return-path，通不过SPF
- Email冒充，DMARC验证通不过，需要自己搭建邮件服务器，或者使用第三方邮件服务商提供，或者受攻击的域名没有配置SPF
## 防御手段
### 邮件服务商
- 网站避免XSS/CSRF漏洞
- MFA
  - Two-Factor-Authorication/Two-Step-Authorication
  - One Time Token
  - U顿(一次性Token升级版)
- SASL认证方式升级
- 邮件联盟
- Spam识别
  - 依靠频率和内容冗余，特征分析等传统技术识别
  - 依靠AI技术识别
### 客户端
1. 相似域名提醒
  - 集成著名域名数据库
  - 对高频使用的字符进行分析，比如：l和1，unicode ṇ和n等
2. 相似/相同Display Name提醒
  - 类似域名，增加联系人里面的同名分析
3. Url和实际跳转Url不一致提醒
  - 跨域跳转提醒
  - Rule #1跳转提醒
4. SPF/DKIM/DMARC结果展示，并加强本地验证
5. 发件人IP地址隐藏
   - 通过服务器代理发送
6. 收件人IP地址隐藏，阅读邮件行为隐藏
   - 通过Anti tracking把跟踪逻辑去掉(Done)
## 流程图
![图1](./images/1.gif)
![图2](./images/2.gif)
![图3](./images/3.gif)
![SPF](./images/SPF.gif)
![DKIM](./images/DKIM.gif)
![DMARC](./images/DMARC.gif)
## 国际反垃圾邮件组织(spamhaus)
- XBL(Exploits Block List): 它是针对因为安全问题被劫持（比如僵尸机）或是蠕虫/病毒，带有内置式垃圾邮件引擎和其他类型的木马来发垃圾邮机器的实时黑名单IP列表。它的数据主要来源于两个合作组织：cbl.abuseat.org及www.njabl.org.因为被列入XBL的服务器大多为被第三方劫持利用，所以有可能导致误判断。
- SBL(The Spamhaus Block List)：它是已经经过验证的垃圾邮件源及确有垃圾邮件发送行为的实时黑名单列表。它也是spamhaus最主要的项目之一，由分布在全世界9个国家的,每周7天，每天24小时进行列入新记录和删除记录的工作。所以，这个列表可信度高使用人数也多。如果你被列入算是严重事件，被列入后，需要你的ISP（电信或是网通）的IP管理人员去和Spamhaus联系才有可能移除。
- PBL(The Policy Block List):它主要是包含动态IP及哪些允许未经验证即可发送邮件的SMTP服务器的IP地址段。这一个列表最明显的特点就是提供了一个IP地址移除的自助服务，IP它列入后，可以自己申请移除。所以就算是被PBL列入，影响并不大，请要使用移除功能移除即可。
- ZEN: 是上面三个的合集，即包括上面XBL，SBL，PBL的数据。
- DBL:(The Domain Block List)：它是针对因垃圾邮件源而建立的基于域名的黑名单列表。
- ROKSO
## 反垃圾邮件：保护自己别被列如黑名单
各大邮件服务商需要尽量避免自己成为垃圾邮件源，否则容易被标注进入黑名单
- SPF(Sender Policy Framework)
  - https://tools.ietf.org/html/rfc7208
  - SPF是为了防范伪造发件人地址发送垃圾邮件而提出的一种开放式标准，是一种以IP地址认证电子邮件发件人身份的技术。域名所有者通过在DNS中发布SPF记录来授权合法使用该域名发送邮件的IP地址。
  - 当在DNS中定义了域名的SPF记录后，为了确认邮件声称发件人不是伪造的，邮件接收方首先检查邮件域名的SPF记录，来确定发件人的IP地址是否被包含在SPF记录中，若包含，则认为是一封正确的邮件，否则认为是一封伪造的邮件并退回，或将其标记为垃圾/仿冒邮件。
  - 设置正确的SPF记录可以提高邮件系统发送外域邮件的成功率，也可以一定程度上防止被假冒域名发送邮件。
  - 在TXT中有一条记录: start with `v=spf1`. Example:`v=spf1 include:_spf.google.com ~all`
- DKIM(DomainKeys Identified Mail)(RFC6376)
  - https://tools.ietf.org/html/rfc6376
  - DKIM verifies that message content is authentic and not changed.
  - 目前有微软推出的Sender ID作为其唯一的竞争者，不过两者应用差距明显
- DMARC(Domain-based Message Authentication, Reporting & Conformance)(2012)
  - https://tools.ietf.org/html/rfc7489
  - DMARC是一种基于现有的SPF和DKIM协议的可扩展电子邮件认证协议，在邮件收发双方建立了邮件反馈机制，便于邮件发送方和邮件接收方共同对域名的管理进行完善和监督。
  - 当Mail Receiver方（其MTA需支持DMARC协议）收到该域发送过来的邮件时，则进行DMARC校验，若校验失败还需发送一封report到指定[URI]（常是一个邮箱地址）
## PTR(反向域名解析)
国外部分邮件服务商会对收到的邮件进行反向域名解析`dig -x  IP`
PTR和SPF有部分重合，PTR是从ISP那边配置的，SPF是从域名服务商那边配置
## 当前状况
- 250OK今年8月新出的一份DMARC报告显示，律所在安全协议采用上走在各行业前列，但其采纳率也仅有1/3这么点儿。大部分其他公司的采纳率微乎其微。
- 250OK的研究与Agari早些时候的调查遥相呼应。Agari发现，财富500强企业中恰当实现了DMARC的仅占8%，仅2%的域名有所防护。
- 设置DMARC、DKIM和SPF并不容易，且易受运营商错误影响
- 国内的万网是不支持DKIM，目前新网是支持SPF和DKIM。
## 相关Header
- Return-Path: 邮件返回地址
- Received-SPF: pass 表示通过
- Authentication-Results: dkim=pass,spf=pass,dmarc=pass
- DKIM-Signature:一些配置信息提供验证邮件内容是否修改
- ARC-Authentication-Results: 有点类似Authentication-Results
- ARC-Message-Signature: 类似DKIM-Signature
- ARC-Seal:
## 帮助工具
黑名单组织: https://www.spamhaus.org/lookup/  
反馈DKARC报告: https://dmarc.postmarkapp.com/  
https://www.mail-tester.com/spf-dkim-check  
https://www.dmarcanalyzer.com/spf/checker/  
https://www.dmarcanalyzer.com/dkim/dkim-check/  
https://www.dmarcanalyzer.com/dmarc/dmarc-record-check/  
https://toolbox.googleapps.com/apps/checkmx/  
https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/how-office-365-uses-spf-to-prevent-spoofing  
## Edison
- edisonmail.com(edsionmail.app去掉)
- edison.tech
  - SPF: NEUTRAL with IP 209.85.220.41 Learn more
  - DKIM: 'PASS' with domain edison-tech.20150623.gappssmtp.com Learn more
```
dig TXT _dmarc.sendgrid.net
sendgrid.net: "v=DMARC1; p=reject; sp=none; rua=mailto:dmarc_agg@dmarc.250ok.net; ruf=mailto:dmarc_fr@dmarc.250ok.net; fo=1; pct=100; rf=afrf"
amazonses.com: "v=DMARC1; p=quarantine; rua=mailto:rua@dmarc.amazonses.com; ruf=mailto:ruf@dmarc.amazonses.com"
qq.com:"v=DMARC1; p=none; rua=mailto:mailauth-reports@qq.com"
aol.com:"v=DMARC1; p=reject; pct=100; rua=mailto:d@rua.agari.com; ruf=mailto:d@ruf.agari.com;"
zoho.com:"v=DMARC1; p=reject; sp=reject; fo=0; rua=mailto:dmarcaggregation@zoho.com; ruf=mailto:dmarcaggregation@zoho.com"  
```