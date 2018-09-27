#### message
message是一种基本推送消息方法，它不要求响应。主要用于IM、groupChat、alert和notification之类的应用中
属性：type, body, subject
type属性，它主要有5种类型：
normal：类似于email，主要特点是不要求响应；
chat：类似于qq里的好友即时聊天，主要特点是实时通讯；
groupchat：类似于聊天室里的群聊；
headline：用于发送alert和notification；
error：如果发送message出错，发现错误的实体会用这个类别来通知发送者出错了
#### presence
presence用来表明用户的状态，如：online、away、dnd(请勿打扰)等。当改变自己的状态时，就会在stream的上下文中插入一个Presence元素，来表明自身的状态。要想接受presence消息，必须经过一个叫做presence subscription的授权过程。 
属性：
type属性，非必须。有以下类别
    subscribe：订阅其他用户的状态
    probe：请求获取其他用户的状态
    unavailable：不可用，离线（offline）状态
to属性：标识消息的接收方。
from属性：指发送方的名字或标示。
载荷（payload）： 
    show：
    chat：聊天中
    away：暂时离开
    xa：eXtend Away，长时间离开
    dnd：勿打扰
status：格式自由，可阅读的文本。也叫做rich presence或者extended presence，常用来表示用户当前心情，活动，听的歌曲，看的视频，所在的聊天室，访问的网页，玩的游戏等等。
priority：范围-128~127。高优先级的resource能接受发送到bare JID的消息，低优先级的resource不能。优先级为负数的resource不能收到发送到bare JID的消息。
<presence from="alice@wonderland.lit/pda">
    <show>xa</show>
    <status>down the rabbit hole!</status>
</presence>
<presence type="subscribe" to="1007@duimy" id="3C1090D3-BF41-4CF3-8034-A6DFEACC118B">
  <extra xmlns="http://www.duimy.com/presence-extra">
    <message>请求加个好友呗</message>
    <timestamp>2017-06-20 17:56:26</timestamp>
  </extra>
</presence>

#### iq
一种请求／响应机制，从一个实体从发送请求，另外一个实体接受请求，并进行响应。例如，client在stream的上下文中插入一个元素，向Server请求得到自己的好友列表，Server返回一个，里面是请求的结果。 
主要的属性是type。包括: 
    Get :获取当前域值。类似于http get方法。
    Set :设置或替换get查询的值。类似于http put方法。
    Result :说明成功的响应了先前的查询。类似于http状态码200。
    Error: 查询和响应中出现的错误。
<iq type="set">
  <query xmlns="jabber:iq:roster">
    <item jid="1001@duimy" subscription="remove"/>
  </query>
</iq>