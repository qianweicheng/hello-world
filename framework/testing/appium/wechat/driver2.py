import logging
import re
import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from wechat.actions import read_input_with_timeout
from wechat.date_helper import date_fix
from wechat.messager import Messager


class WechatDriver2(object):
    # https://appium.io/docs/en/writing-running-appium/caps/
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'Android-HUAWEI',
        # 'platformVersion': '10',
        # 'unid':'CLB7N18B07008885', # 如果同时登录多台设备使用这个区分
        'appPackage': 'com.tencent.mm',
        'appActivity': 'com.tencent.mm.ui.LauncherUI',
        'newCommandTimeout': 300,  # 下一个命令的最大等待时间
        # "deviceId": "192.168.2.241:5555",
        # "adbPort": 5555,
        # "dontStopAppOnReset": True,
        'noReset': True,
        # 'app':'the-apk-path-if-appPackage-or-appActivity-is-not-specialfied'
    }

    def __init__(self):
        self.logger = logging.getLogger("wechat")
        self.messager = Messager("钱炜铖")  # 自己
        # 只记录指定的对话，如果为空则监控全部对话
        self.rooms = ["弹性开发部"]
        # 进入到消息列表页面后的消息处理模式:
        # 1. 完整模式,包括历史记录
        # 2. 新消息，在开启应用之后收到的消息
        # 3. 不处理任何消息，只是用来调试作用，或者用来消除未读取消息数
        self.message_log_mode = 1
        self.scroll_conversion_list = False  # 会话是否需要滚动
        # ======配置文件到此结束=====
        self.wechat_file_path = "/sdcard/tencent/MicroMsg/WeiXin/"
        self.wechat_attachment = "/sdcard/tencent/MicroMsg/Download/"
        self.driver = None
        self.wait = None
        self.conversion_map = None
        self.reset_driver()

    def reset_driver(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        self.wait = WebDriverWait(self.driver, 30)
        self.wait_list_page()

    def wait_list_page(self):
        self.logger.info(self.driver.current_activity)
        # self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/bw')))
        self.driver.wait_activity(".ui.LauncherUI", 30)
        self.logger.info(self.driver.current_activity)

    def select_tab(self, tab_name, count=1):
        # 底部的
        # RelativeLayout(com.tencent.mm:id/bw)->LinearLayout->RelativeLayout(点击区域)->LinearLayout->RelativeLayout,TextView(com.tencent.mm:id/dkb)
        # bottom = self.driver.find_element_by_id('com.tencent.mm:id/bw')
        # tabs = bottom.find_elements_by_xpath('//*[@resource-id="com.tencent.mm:id/dkb"]/../..')
        try:
            self.wait.until(EC.presence_of_element_located((By.ID, "com.tencent.mm:id/bw")))
            tabs = self.driver.find_elements_by_xpath('//*[@resource-id="com.tencent.mm:id/dkb"]/../..')
            selected_tab = None
            if len(tabs) == 4:
                if tab_name == "消息":
                    selected_tab = tabs[0]
                elif tab_name == "联系人":
                    selected_tab = tabs[1]
                elif tab_name == "发现":
                    selected_tab = tabs[2]
                elif tab_name == "我":
                    selected_tab = tabs[3]
                else:
                    self.logger.error("unknown {} tab".format(tab_name))
            else:
                self.logger.error("tab数不对")
            if not selected_tab:
                return
            if count == 2:
                ActionChains(self.driver).move_to_element(selected_tab).click().pause(0.25).click().perform()
            else:
                TouchAction(self.driver).tap(selected_tab).perform()
        except Exception as e:
            self.logger.error(e)

    def conversion_list_pages(self, mode=2):
        # 确保回到顶部
        self.scroll_top()
        self.conversion_map = set()
        while True:
            self.conversion_list()
            if self.scroll_conversion_list:
                reach_bottom = self.conversion_list_scroll(mode=mode)
                if reach_bottom:
                    break
            else:
                break
        # index = 0
        # for conversion in self.conversion_map:
        #     index += 1
        #     self.logger.info("{}\t{}".format(index, conversion))
        self.conversion_map = None
        self.logger.info("==================================")

    def conversion_list_scroll(self, mode):
        if mode == 1:
            self.select_tab("消息", count=2)
        else:
            try:
                # 对于是否滑倒底部做二次确认
                retry_count = 2
                while retry_count:
                    list_view = self.wait.until(EC.presence_of_element_located((By.ID, "com.tencent.mm:id/dcf")))
                    rows = list_view.find_elements_by_id("com.tencent.mm:id/bah")
                    row_count = len(rows)
                    if row_count > 5:
                        first_row = rows[2]
                        last_row = rows[row_count - 3]
                        tag = first_row.get_attribute("bounds")
                        self.driver.scroll(last_row, first_row, duration=2000)
                        rows2 = list_view.find_elements_by_id("com.tencent.mm:id/bah")
                        row_count2 = len(rows)
                        if row_count2 > 2:
                            tag2 = rows2[2].get_attribute("bounds")
                            if tag == tag2:
                                retry_count -= 1
                            else:
                                return False
                return retry_count == 0
            except Exception as e:
                self.logger.error(e)
            return False

    def conversion_list(self):
        """
        需要监控的会话必须置顶，这样可靠性更高
        :return:
        """
        row_index = 0
        bounds_rex = re.compile(r"\[(\d{,4}),(\d{,4})\]\[(\d{,4}),(\d{,4})\]")
        list_top = 0
        list_bottom = 0
        while True:
            list_view = self.wait.until(EC.presence_of_element_located((By.ID, "com.tencent.mm:id/dcf")))
            rows = list_view.find_elements_by_id("com.tencent.mm:id/bah")
            row_count = len(rows)
            if row_index < row_count:
                row = rows[row_index]
                row_index += 1
            else:
                if row_index > 0 and row_count == 0:
                    self.logger.error("Conversion List: last index is {}".format(row_index))
                break
            # 修正点击区域，划出屏幕的不点击
            if not list_bottom:
                # '[0,2187][1080,2244]'
                bottom_bounds = self.driver.find_element_by_id("com.tencent.mm:id/bw").get_attribute("bounds")
                title_bounds = self.driver.find_element_by_id("com.tencent.mm:id/l2").get_attribute("bounds")
                result = bounds_rex.match(bottom_bounds)
                list_bottom = int(result.group(2))
                result = bounds_rex.match(title_bounds)
                list_top = int(result.group(2))
            row_bounds = row.get_attribute("bounds")
            result = bounds_rex.match(row_bounds)
            row_top = int(result.group(2))
            row_bottom = int(result.group(4))
            row_middle = (row_bottom + row_top) / 2
            if row_middle > list_bottom or row_middle < list_top:
                continue
            # 标题
            els = row.find_elements_by_id("com.tencent.mm:id/baj")
            room = els[0].text if els else ""
            if not room:
                # 列表控件回收导致的
                continue
            elif room in self.conversion_map:
                # 滚动的时候接上一屏幕的重复数据
                continue
            elif self.rooms and room not in self.rooms:
                self.logger.info("{}\tskip conversion".format(room))
                self.conversion_map.add(room)
                continue
            self.conversion_map.add(room)
            els = row.find_elements_by_id("com.tencent.mm:id/bal")
            last_message = els[0].text if els else None
            els = row.find_elements_by_id("com.tencent.mm:id/bak")
            last_message_time = date_fix(els[0].text) if els else None
            message_count = ""
            if not message_count:
                # 单聊消息数
                els = row.find_elements_by_id("com.tencent.mm:id/op")
                message_count = els[0].get_attribute("text") if els else 0
            if not message_count:
                # 群聊新消息标记
                els = row.find_elements_by_id("com.tencent.mm:id/bai")
                message_count = "1+" if els else 0
            self.logger.info("{}\t{}\t{}\t{}".format(room, message_count, last_message_time, last_message))
            if message_count or self.message_log_mode != 2:
                # row.click()
                TouchAction(self.driver).tap(row).perform()
                try:
                    # 进入了详情页面
                    self.conversion_detail_messages_pages(room)
                except Exception as e:
                    self.logger.error(e)
                # 返回到列表页面
                if self.driver.find_elements_by_id("com.tencent.mm:id/dcf") and \
                        self.driver.find_elements_by_id("com.tencent.mm:id/bw"):
                    # 已经在当前页，防止点击失效的情况
                    continue
                else:
                    self.driver.press_keycode(4)

    def conversion_detail_messages_pages(self, room):
        # self.driver.flick(100, 300, 100, 1000)
        if self.message_log_mode == 3:
            return
        els = self.driver.find_elements_by_id("com.tencent.mm:id/apo")
        if els:
            TouchAction(self.driver).tap(els[0]).perform()
        while True:
            self.conversion_detail_messages(room)
            reach_bottom = self.conversion_detail_scroll()
            if reach_bottom:
                break
        self.logger.info("==================================")

    def conversion_detail_scroll(self):
        try:
            # 对于是否滑倒底部做二次确认
            retry_count = 2
            while retry_count:
                rows = self.driver.find_elements_by_xpath("//*[@resource-id='com.tencent.mm:id/ab']/..")
                row_count = len(rows)
                # TODO
                if row_count > 3:
                    first_row = rows[1]
                    last_row = rows[row_count - 1]
                    tag = first_row.get_attribute("bounds")
                    self.driver.scroll(last_row, first_row, duration=3000)
                    rows2 = self.driver.find_elements_by_xpath("//*[@resource-id='com.tencent.mm:id/ab']/..")
                    row_count2 = len(rows)
                    if row_count2 > 2:
                        tag2 = rows2[1].get_attribute("bounds")
                        if tag == tag2:
                            retry_count -= 1
                        else:
                            return False
            return retry_count == 0
        except Exception as e:
            # 其它类型的列表有:
            # 订阅号：com.tencent.mm:id/a9x
            # 其它：com.tencent.mm:id/ag
            self.logger.error(e)
        return False

    def conversion_detail_messages(self, room):
        row_index = 0
        current_time = ""
        while True:
            time.sleep(0.5)
            rows = self.driver.find_elements_by_xpath("//*[@resource-id='com.tencent.mm:id/ab']/..")
            row_count = len(rows)
            if row_index < row_count:
                row = rows[row_index]
                row_index += 1
            else:
                if row_index > 0 and row_count == 0:
                    self.logger.error("Conversion Detail: last index:{}".format(row_index))
                break
            el = row.find_elements_by_id("com.tencent.mm:id/ai")
            if el:
                current_time = date_fix(el[0].text)
            elif not current_time:
                current_time = date_fix(self.driver.device_time)
            el = row.find_elements_by_id("com.tencent.mm:id/pp")
            user = ""
            if el:
                user = el[0].text
            if not user:
                el = row.find_elements_by_id("com.tencent.mm:id/po")
                if el:
                    user = el[0].get_attribute("content-desc")
                    if user:
                        if user.endswith("头像"):
                            user = user[:-2]
                    else:
                        user = room
                else:
                    user = room
            message, _ = self.process_text_message(row)
            if message:
                reply = self.messager.append(room, current_time, user, "text", message, None)
                if reply:
                    self.reply_message(reply)
                continue
            message, path = self.process_image_message(row)
            if message:
                reply = self.messager.append(room, current_time, user, "image", message, path)
                if reply:
                    self.reply_message(reply)
                continue
            message, path = self.process_voice_message(row)
            if message:
                self.messager.append(room, current_time, user, "voice", message, path)
                continue
            message, path = self.process_video_message(row)
            if message:
                self.messager.append(room, current_time, user, "video", message, path)
                continue
            message, path = self.process_call_message(row)
            if message:
                self.messager.append(room, current_time, user, "call", message, path)
                continue
            message, path = self.process_file_message(row)
            if message:
                self.messager.append(room, current_time, user, "file", message, path)
                continue
            message, path = self.process_other_message(row)
            if message:
                self.messager.append(room, current_time, user, "other", message, path)
                continue
            message, path = self.process_unknown_message(row)
            if message:
                self.messager.append(room, current_time, user, "unknown", message, path)

    def process_text_message(self, row):
        try:
            el = row.find_elements_by_id("com.tencent.mm:id/pq")
            a = row.find_elements_by_id("com.tencent.mm:id/awb")
            # 排查带有pq的语音消息
            if el and not a:
                ActionChains(self.driver).move_to_element(el[0]).click().pause(0.25).click().perform()
                text_view = self.wait.until(EC.presence_of_element_located((By.ID, "com.tencent.mm:id/awl")))
                message = text_view.text
                self.driver.press_keycode(4)
                return message, None
        except Exception as e:
            self.logger.error(e)
            return "[文本消息]", None
        return None, None

    def process_image_message(self, row):
        try:
            el = row.find_elements_by_id("com.tencent.mm:id/aw3")
            if el:
                # 附加条件
                a = row.find_elements_by_id("com.tencent.mm:id/atb")
                b = row.find_elements_by_id("com.tencent.mm:id/av0")
                c = row.find_elements_by_id("com.tencent.mm:id/av4")
                if not a or not b or not c:
                    return None, None
                ActionChains(self.driver).move_to_element(el[0]).click().perform()
                # full_screen_message_el = self.driver.find_element_by_class_name("com.tencent.mm.ui.mogic.WxViewPager")
                # TouchAction(self.driver).long_press(full_screen_message_el).perform()
                # TouchAction(self.driver).tap(self.driver.find_element_by_xpath('//*[@text="保存图片"]/../../..')).perform()
                # 下载按钮
                TouchAction(self.driver).tap(self.driver.find_element_by_id('com.tencent.mm:id/cqq')).perform()
                toast = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(@text,'图片已保存至')]")))
                toast_message = toast.text
                self.driver.press_keycode(4)
                if toast_message:
                    # file name:  2020-02-13 13:14 wx_camera_1581570852980.jpg
                    # tencent/MicroMsg/WeiXin/ -> /sdcard/tencent/MicroMsg/WeiXin/
                    # 获取到这个文件夹的最后一个文件就可以
                    filename = self.exec("ls -t {}| head -n1".format(self.wechat_file_path)).strip()
                    return "[图片消息]", "{}{}".format(self.wechat_file_path, filename)
        except Exception as e:
            self.logger.error(e)
            return "[图片消息]", None
        return None, None

    def process_video_message(self, row):
        try:
            el = row.find_elements_by_id("com.tencent.mm:id/gi9")
            if el:
                # 点击视频播放
                click_btn = el[0].find_elements_by_id("com.tencent.mm:id/atb")
                # 附加条件
                a = row.find_elements_by_id("com.tencent.mm:id/av0")
                b = row.find_elements_by_id("com.tencent.mm:id/av4")
                c = row.find_elements_by_id("com.tencent.mm:id/av3")
                if not click_btn or not a or not b or not c:
                    return None, None
                ActionChains(self.driver).move_to_element(click_btn[0]).click().perform()
                # 视频页面: 点击更多
                more_btn = self.wait.until(EC.presence_of_element_located((By.ID, "com.tencent.mm:id/gig")))
                ActionChains(self.driver).move_to_element(more_btn).click().perform()
                # 视频页面: 点击保存按钮
                save_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@text="保存视频"]/../../..')))
                TouchAction(self.driver).tap(save_btn).perform()
                toast = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(@text,'视频已保存至')]")))
                toast_message = toast.text
                self.driver.press_keycode(4)
                if toast_message:
                    # filename = self.exec("ls -t {}| head -n1".format(self.wechat_file_path)).strip()
                    # return "[视频消息]", "{}{}".format(self.wechat_file_path, filename)
                    return "[视频消息]", toast_message[6:]
        except Exception as e:
            self.logger.error(e)
            return "[视频消息]", None
        return None, None

    def process_voice_message(self, row):
        try:
            el = row.find_elements_by_id("com.tencent.mm:id/awb")
            if el:
                a = row.find_elements_by_id("com.tencent.mm:id/awc")
                title1 = row.find_elements_by_id("com.tencent.mm:id/awd")
                title2 = row.find_elements_by_id("com.tencent.mm:id/pq")
                if not a or not title1 or not title2:
                    return None, None
                return "[语音消息]{} {}".format(title1[0].text, title2[0].text), None
        except Exception as e:
            self.logger.error(e)
            return "[语音消息]", None
        return None, None

    def process_call_message(self, row):
        try:
            el = row.find_elements_by_id("com.tencent.mm:id/awh")
            a = row.find_elements_by_id("com.tencent.mm:id/awg")
            if el and a:
                return "[电话]" + el[0].get_attribute("text"), None
        except Exception as e:
            self.logger.error(e)
            return "[电话]", None
        return None, None

    def process_file_message(self, row):
        try:
            # ----(文件)LinearLayout(ata)->ats,att,atv(文件大小)
            abv = row.find_elements_by_id("com.tencent.mm:id/abv")
            el = row.find_elements_by_id("com.tencent.mm:id/ata")
            if abv and el:
                a = row.find_elements_by_id("com.tencent.mm:id/atb")
                b = row.find_elements_by_id("com.tencent.mm:id/atp")
                title_view = el[0].find_elements_by_id("com.tencent.mm:id/ats")
                file_size = el[0].find_elements_by_id("com.tencent.mm:id/att")
                icon = el[0].find_elements_by_id("com.tencent.mm:id/atv")
                if not a or not b or not title_view or not file_size or not icon:
                    return None, None
                TouchAction(self.driver).tap(a[0]).perform()
                title_textview = self.driver.find_elements_by_id("com.tencent.mm:id/bgc")
                file_size = self.driver.find_elements_by_id("com.tencent.mm:id/bgd")
                if title_textview and file_size:
                    message = "[文件]{}({})".format(title_textview[0].text, file_size[0].text)
                    path = title_textview[0].text
                else:
                    message = "[文件]"
                    path = None
                self.driver.press_keycode(4)
                return message, "{}{}".format(self.wechat_attachment, path)
        except Exception as e:
            self.logger.error(e)
            return "[文件]", None
        return None, None

    def process_other_message(self, row):
        try:
            abv = row.find_elements_by_id("com.tencent.mm:id/abv")
            el = row.find_elements_by_id("com.tencent.mm:id/ata")
            if abv and el:
                b = el[0].find_elements_by_id("com.tencent.mm:id/atb")
                c = el[0].find_elements_by_id("com.tencent.mm:id/atp")
                title = el[0].find_elements_by_id("com.tencent.mm:id/atq")
                if not b or not c or not title:
                    return None, None
                return "[其它消息]" + title[0].text, None
        except Exception as e:
            self.logger.error(e)
            return "[其它消息]", None
        return None, None

    def process_unknown_message(self, row):
        try:
            self.logger.warning("Unsupported message")
            row.screenshot("./images/001.png")
            return "[未知消息]", None
        except Exception as e:
            self.logger.error(e)
            return "[未知消息]", None
        return None, None

    def reply_message(self, text):
        try:
            edit = self.driver.find_element_by_id("com.tencent.mm:id/aqe")
            edit.click()
            edit.set_value(text)
            # edit.send_keys(text)
            context2 = edit.get_attribute('text')
            self.logger.info("Sending:" + context2)
            send_btn = self.driver.find_element_by_id("com.tencent.mm:id/aql")
            TouchAction(self.driver).tap(send_btn).perform()
            # back_btn = self.driver.find_element_by_id("com.tencent.mm:id/lr")
            # TouchAction(self.driver).tap(back_btn).perform()
            # 只收回键盘
            self.driver.press_keycode(4)
        except Exception as e:
            self.logger.error(e)

    def search(self, text):
        search_btn = self.driver.find_element_by_id("com.tencent.mm:id/c8")
        actions = TouchAction(self.driver)
        actions.tap(search_btn)
        actions.perform()

    def exec(self, cmd, *args):
        try:
            # An unknown server-side error occurred while processing the command.
            # Original error: Appium server must have relaxed security flag set in order to run any shell commands
            result = self.driver.execute_script('mobile: shell', {
                'command': cmd,
                'args': [*args],
                'includeStderr': True,
                'timeout': 5000
            })
            return result['stdout']
        except Exception as e:
            self.logger.error(e)
        return ""

    def scroll_top(self):
        try:
            el = self.wait.until(EC.presence_of_element_located((By.ID, "com.tencent.mm:id/l2")))
            # TouchAction(self.driver).tap(el, x=10, y=10).wait(100).tap(el, x=10, y=10).perform()
            ActionChains(self.driver).move_to_element(el).click().pause(0.25).click().pause(1).perform()
        except Exception as e:
            self.logger.error(e)

    def start(self):
        error_count = 0
        stop = False
        while not stop:
            try:
                while not stop:
                    self.select_tab("消息")
                    self.conversion_list_pages()
                    data = read_input_with_timeout("按回车键退出.否则5秒后继续下一轮\n", timeout=5)
                    if data is not None:
                        stop = True
                        break
                    else:
                        # 重置错误次数
                        error_count = 0
            except Exception as e:
                logging.error(e)
                error_count += 1
                if error_count < 10:
                    logging.info("程序出错{}次，10s后重试".format(error_count))
                    time.sleep(10)
                    self.reset_driver()
                else:
                    logging.error("程序连续出错{}次，放弃重试".format(error_count))
                    # stop = True
                    break

    def start2(self):
        try:
            el = self.driver.find_element_by_id("com.tencent.mm:id/l2")
            # TouchActions(self.driver).tap_and_hold(100, 100).move(50, 50).perform()
            # TouchActions(self.driver).scroll_from_element(el, 10, 100).scroll(10, 1000).perform()
            TouchAction(self.driver).long_press(el).perform()
            # TouchAction(self.driver).flick_element(el, 1, 10, 10).perform()
            ActionChains(self.driver).move_to_element(el).click_and_hold().perform()
            ActionChains(self.driver).move_to_element(el).click_and_hold().move_by_offset(100, 100).release().perform()
        except Exception as e:
            self.logger.error(e)


if __name__ == "__main__":
    driver = WechatDriver2()
    driver.start()
