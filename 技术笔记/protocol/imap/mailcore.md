## AbstractPart
- IMAPPart
- AbstractMessagePart:增加了header和mainPart
    - IMAPMessagePart:增加了size
- AbstractMultipart:增加parts()方法用来存放子part
    - IMAPMultipart