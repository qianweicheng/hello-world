# Microsoft
- Outlook.com
  - 网址: https://outlook.com/, https://live.com
  - a free web based mail account, formerly known as Hotmail.
- Office365
  - https://outlook.office365.com
  - https://portal.office.com
- Office 2019 vs Office 365
  - 官网介绍：https://support.office.com/en-us/article/what-s-the-difference-between-office-365-and-office-2019-ed447ebf-6060-46f9-9e90-a239bd27eb96?ad=US&omkt=en-001&rs=en-001&ui=en-US
  - 一个是一次性买断，只包含软件。一个是订阅，并且可以多机器安装，丰富的在线服务，比如Email, OneDrive等等
## Office365
IMAP，Exchange，POP3, MAPI, Outlook Web App or Exchange ActiveSync

Domain|MX
-|-
GoDaddy.com | godaddy-com.mail.protection.outlook.com
easilydo.onmicrosoft.com | easilydo.mail.protection.outlook.com
cornell.edu | cornellprod-mail-onmicrosoft-com.mail.eo.outlook.com

## Azure
Azure portal: https://portal.azure.com/
Web Mail: https://outlook.office.com/mail/inbox
Web Mail Admin: https://admin.microsoft.com/AdminPortal/Home#/homepage
二次验证：https://account.activedirectory.windowsazure.com/UserManagement/MultifactorVerification.aspx?BrandContextID=O365
在Web Mail Admin->Active users-> Multifactor authentication
## Office365 Exchange协议
- Outlook on the Web
- Outlook desktop(MAPI)
- Exchange Web Service(EWS)
- Mobile(ActiveSync)
- IMAP
- Pop
- Authenticated SMTP
### Autodiscover
https://docs.microsoft.com/zh-cn/Exchange/architecture/client-access/autodiscover?view=exchserver-2019
1. http://your-domain/Autodiscover/Autodiscover.xml
2. http://autodiscover.your-domain/Autodiscover/Autodiscover.xml
3. 查询DNS是否注册有名称为_autodiscover的SRV服务记录，如果有，获取该服务记录所指定的主机名称（A记录）。假设找到SRV记录，指向主机mail.your-domain。那么Outlook会尝试连接：
https://mail.your-domain/autodiscover/autodiscover.xml

https://outlook.office365.com/EWS/Exchange.asmx

https://easilydo.onmicrosoft.com/EWS/Exchange.asmx

### Exchange Web Service(EWS)开发指南
https://docs.microsoft.com/zh-cn/exchange/client-developer/exchange-server-development
https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/concept-fundamentals-block-legacy-authentication
https://techcommunity.microsoft.com/t5/exchange-team-blog/upcoming-changes-to-exchange-web-services-ews-api-for-office-365/ba-p/608055
