import logging

from wechat.actions import pull_files_from_device


class Messager(object):

    def __init__(self, me):
        self.logger = logging.getLogger("messager")
        self.conversions = {}
        self.me = me
        self.message_id = 0

    def append(self, room, date, sender, message_type, message, path):
        self.logger.info(
            "Room:{}\tTime:{}\tType:{}\tSender:{}\tMessage:{}".format(room, date, message_type, sender, message))
        conversion = self.conversions.get(room)
        if not conversion:
            conversion = []
        conversion.append({
            "room": room,
            "date": date,
            "sender": sender,
        })
        if path:
            pull_files_from_device(path)
        # 如果需要回复信息，则返回信息内容
        # if not message.startswith("回复"):
        #     self.message_id += 1
        #     return "回复 {}:{}".format(self.message_id, message)
        # TODO: 存到数据库中，并需要做去重处理
        return None
