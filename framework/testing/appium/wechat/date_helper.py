import re
import time
import datetime


def date_fix(text):
    """
    修正微信消息的时间，使用统一格式
    :param text:
    :return:
    """
    # 当天: 10:10
    # 昨天: 昨天 10:10
    # 上周: 周一 10:10, 周二 10:10, 周三 10:10, 周四 10:10, 周五 10:10, 周六 10:10, 周日 10:10
    # 日期: 01月02日 10:10, 01月02日 晚上10:10
    # 往年日期: 2020年01月02日 10:10, 2020年01月02日 晚上10:10
    today_re = re.compile(r"\d{,2}:\d{,2}")
    result = today_re.match(text)
    if result:
        full_time = "{} {}".format(datetime.date.today(), result.group())
        return full_time
    yesterday_re = re.compile(r"昨天\s(\d{,2}:\d{,2})")
    result = yesterday_re.match(text)
    if result:
        day = datetime.date.today() - datetime.timedelta(days=1)
        full_time = "{} {}".format(day, result.group(1))
        return full_time
    this_week_re = re.compile(r"(周.?)\s(\d{,2}:\d{,2})")
    result = this_week_re.match(text)
    if result:
        week_str = result.group(1)
        cur_week_index = datetime.date.today().weekday()
        old_week_index = 0
        if week_str == "周一":
            old_week_index = 0
        elif week_str == "周二":
            old_week_index = 1
        elif week_str == "周三":
            old_week_index = 2
        elif week_str == "周四":
            old_week_index = 3
        elif week_str == "周五":
            old_week_index = 4
        elif week_str == "周六":
            old_week_index = 5
        elif week_str == "周日":
            old_week_index = 6
        if cur_week_index > old_week_index:
            diff_days = cur_week_index - old_week_index
        else:
            diff_days = cur_week_index + 7 - old_week_index
        day = datetime.date.today() - datetime.timedelta(days=diff_days)
        full_time = "{} {}".format(day, result.group(2))
        return full_time
    full_time_re = re.compile(r"(\d{2,4}年)?(\d{1,2})月(\d{1,2})日.+?(\d{,2}:\d{,2})")
    result = full_time_re.match(text)
    if result:
        if result.group(1):
            year = int(result.group(1)[:-1])
        else:
            year = datetime.date.today().year
        day = datetime.date(year, int(result.group(2)), int(result.group(3)))
        full_time = "{} {}".format(day, result.group(4))
        return full_time
    full_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    return full_time


def datefstr(date_str):
    date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M")
    return date


def date2str(date):
    date_str = date.strftime("%Y-%m-%d %H:%M")
    return date_str


if __name__ == "__main__":
    # print(date_fix("10:10"))
    # print(date_fix("昨天 10:10"))
    # print(date_fix("周一 10:10"))
    # print(date_fix("周二 10:10"))
    # print(date_fix("周三 10:10"))
    # print(date_fix("周四 10:10"))
    # print(date_fix("周五 10:10"))
    # print(date_fix("周六 10:10"))
    # print(date_fix("周日 10:10"))
    # print(date_fix("02月01日 10:10"))
    print(date_fix("02月01日 晚上10:10"))
    print(date_fix("2008年02月01日 晚上10:10"))
    print(date2str(datefstr("2008-02-01 10:10")))
