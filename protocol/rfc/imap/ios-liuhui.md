fetch流程：
1、比对local uids和server拉下来的uids，只拉取server独有的msgs的header&Body structure
2、保存msgs：格式转换，MCOIMAPMessage->EdoMessage,
3、每个msg的save中，保存之前先查看此msg的pid（gmailMsgId或path+uid）是否存在DB，如果存在，merge，如果不存在，add
4、merge过程：
	4.1、用server msg的flag覆盖local的flag（如果本地没有pending action-delete，flag，超过10秒以服务器的状态为准）
	4.2、如果是gmail 邮件 gmailThreadID>0，addCurrFolderInConv(将当前folder添加到EdoConversation表中的folder list，可以在当前folder中查看到邮件所在的conversation)；接着updateGmailIMAPRef，更新gmail msg的ref，比如db中原来的ref是label1，label2，更新之后变为INBOX，更新ref的同时，维护EdoFolder表中的message list，更新ref减少的label，需要在那个label（folder）下删除该msg，增加亦是如此
	4.3、如果是普通IMAP邮件，updateIMAPRef,赋值当前path的uid，如果没有移除之前的ref，新增ref
5、如果没有此msg的pid，就add，add过程：
	5.1、添加msg到DB-db.add(msg),
	5.2、添加到EdoFolder中的msg list—folder.addMessage(msg)，
	5.3、把当前folder添加到EdoConversation表中的folder list字段—addCurrFolderInConv，一并更新cnv的flag，lastxxxdate
	5.4、如果是gmail msg，updateGmailIMAPRef
	5.5、如果是普通IMAP msg，updateIMAPRef


update(sync)流程：
1、用msgIdInfos中的uids去拉取flag和gmail label，比对本地和server的uids，本地去掉（subtract）server之后剩下的uids，需要删掉(普通IMAP邮件），对于gmail邮件(由于msg有多个ref，主体只有一个)判断其ref是否为1个并且等于当前的path，则删除msg主体，否则保留msg主体只删除msg的一个ref。
2、删除msgs：
	2.1、根据threadID把msg分组，
	2.2、如果是IMAP普通邮件，删除msg的ref，删除msg，最后删除该msg的conversation
	2.3、如果是gmail邮件，conversation表反查的msg list去除（subtract）要删掉的msg后，msg数是否为0，为0，需要删除这个conversation，除了删除msg的refs和msg本身以外，不为0，则删除msg的refs和msg本身，重建conversation表中的folder list--rebuildFoldersOfConv，（因为不知道删除的msg会导致conversation表中的哪个folder会被删除）
3、server拉下来的msg调用update：
	3.1、如果flag相同，label也没变化（labelChanged），直接返回，
	3.2、否则调用EmailConversation.update，update方法中 setflag,update ref--updateGmailIMAPRef/updateIMAPRef，重建conversation的folder list—rebuildFoldersOfConv
4、需要删除的msg中，选出不删除msg主体，只需要删除ref的msg，这些msg只删除当前path的ref，从当前folder表中删除该msg—removeFolderMsgsByRef，重建conversation-folderlist关系—rebuildFoldersOfConv