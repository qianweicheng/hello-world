import logging


class Messager(object):
    def __init__(self, me):
        self.logger = logging.getLogger("messager")
        self.conversions = {}
        self.me = me
        self.message_id = 0

    def append(self, room, sender, message, message_type, date):
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
        # 如果需要回复信息，则返回信息内容
        if not message.startswith("回复"):
            self.message_id += 1
            return "回复 {}:{}".format(self.message_id, message)
        # TODO: 存到数据库中，并需要做去重处理
        return None
