import datetime
import logging
import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from wechat import post_runnable
from wechat.date_helper import date_fix
from wechat.messager import Messager


class WechatDriver2(object):
    # https://appium.io/docs/en/writing-running-appium/caps/
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'HUAWEI',
        # 'platformVersion': '10',
        # 'unid':'CLB7N18B07008885',
        'appPackage': 'com.tencent.mm',
        'appActivity': 'com.tencent.mm.ui.LauncherUI',
        'newCommandTimeout': 30,
        # "deviceId": "192.168.2.241:5555",
        'noReset': True,
        # 'app':'the-apk-path-if-appPackage-or-appActivity-is-not-specialfied'
    }

    def __init__(self):
        self.logger = logging.getLogger("wechat")
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        self.wait = WebDriverWait(self.driver, 30)
        self.wait_list_page()
        self.messager = Messager("钱炜铖")  # 自己
        self.rooms = ["盼盼", "成云机器人"]  # 只记录指定的对话，如果为空则全部记录
        self.full_log = True  # 只记录新消息
        self.wechat_file_path = "/sdcard/tencent/MicroMsg/WeiXin/"

    def wait_list_page(self):
        self.logger.info(self.driver.current_activity)
        self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/bw')))
        # self.driver.wait_activity(".ui.LauncherUI", 30)
        self.logger.info(self.driver.current_activity)

    def select_tab(self, tab_name, count=1):
        # 底部的
        # RelativeLayout(com.tencent.mm:id/bw)->LinearLayout->RelativeLayout(点击区域)->LinearLayout->RelativeLayout,TextView(com.tencent.mm:id/dkb)
        # bottom = self.driver.find_element_by_id('com.tencent.mm:id/bw')
        # tabs = bottom.find_elements_by_xpath('//*[@resource-id="com.tencent.mm:id/dkb"]/../..')
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
            ActionChains(self.driver).move_to_element(selected_tab).click().perform()

    def conversion_list(self):
        """
        需要监控的会话必须置顶，这样可靠性更高
        :return:
        """
        row_index = 0
        while True:
            try:
                time.sleep(0.3)
                listview = self.driver.find_element_by_id("com.tencent.mm:id/dcf")
                rows = listview.find_elements_by_id("com.tencent.mm:id/bah")
                row_count = len(rows)
                if row_index < row_count:
                    row = rows[row_index]
                    row_index += 1
                else:
                    if row_index > 0 and row_count == 0:
                        self.logger.error("Last Index:{}".format(row_index))
                    break
                message_count = ""
                last_message = ""
                # 标题
                els = row.find_elements_by_id("com.tencent.mm:id/baj")
                if els:
                    room = els[0].get_attribute("text")
                    if self.rooms and room not in self.rooms:
                        self.logger.info("skip conversion: " + room)
                        continue
                else:
                    continue
                if not message_count:
                    # 单聊消息数
                    els = row.find_elements_by_id("com.tencent.mm:id/op")
                    if els:
                        message_count = els[0].get_attribute("text")
                        has_new_message = True
                if not message_count:
                    # 群聊新消息标记
                    els = row.find_elements_by_id("com.tencent.mm:id/bai")
                    if els:
                        message_count = "1+"
                        has_new_message = True
                # 对话的最后一条
                els = row.find_elements_by_id("com.tencent.mm:id/bal")
                if els:
                    last_message = els[0].get_attribute("text")
                if message_count or self.full_log:
                    self.logger.info("Title:{}\tCount:{}\tLast message:{}".format(room, message_count, last_message))
                    row.click()
                    # TouchAction(self.driver).tap(row).perform()
                    # 进入了详情页面
                    try:
                        self.conversion_detail_messages_pages(room)
                    except Exception as e:
                        self.logger.error(e)
                    # 返回到列表页面
                    self.driver.press_keycode(4)
            except Exception as e:
                # 这里是订阅消息等异常情况
                self.logger.error(e)
        self.select_tab('消息')
        post_runnable(self.conversion_list, delay=3)

    def conversion_detail_messages_pages(self, room):
        # self.driver.flick(100, 300, 100, 1000)
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
            rows = self.driver.find_elements_by_xpath("//*[@resource-id='com.tencent.mm:id/ab']/..")
            row_count = len(rows)
            if row_count > 2:
                first_row = rows[0]
                last_row = rows[row_count - 1]
                tag = first_row.get_attribute("bounds")
                self.driver.scroll(last_row, first_row, duration=2000)
                rows2 = self.driver.find_elements_by_xpath("//*[@resource-id='com.tencent.mm:id/ab']/..")
                row_count2 = len(rows)
                if row_count2 > 2:
                    tag2 = rows2[0].get_attribute("bounds")
                    if tag == tag2:
                        return True
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
            time.sleep(0.1)
            rows = self.driver.find_elements_by_xpath("//*[@resource-id='com.tencent.mm:id/ab']/..")
            row_count = len(rows)
            if row_index < row_count:
                row = rows[row_index]
                row_index += 1
            else:
                if row_index > 0 and row_count == 0:
                    self.logger.error("Last Index:{}".format(row_index))
                break
            el = row.find_elements_by_id("com.tencent.mm:id/ai")
            if el:
                current_time = date_fix(el[0].text)
            elif not current_time:
                current_time = date_fix(self.driver.device_time)
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
            elif message == "":
                continue
            message, path = self.process_image_message(row)
            if message:
                reply = self.messager.append(room, current_time, user, "image", message, path)
                if reply:
                    self.reply_message(reply)
                continue
            elif message == "":
                continue
            message, path = self.process_video_message(row)
            if message:
                self.messager.append(room, current_time, user, "video", message, path)
                continue
            elif message == "":
                continue
            message, path = self.process_voice_message(row)
            if message:
                self.messager.append(room, current_time, user, "voice", message, path)
                continue
            elif message == "":
                continue
            message, path = self.process_other_message(row)
            if message:
                self.messager.append(room, current_time, user, "other", message, path)
                continue
            elif message == "":
                continue
            # RelativeLayout
            # --（可能）TextViewcom.tencent.mm:id/ai
            # --LinearLayout(ab)
            # ----(文字)LinearLayout()->pq
            # ----(图片)LinearLayout(aw3)->atb
            # ----(视频)LinearLayout()->gi9->abt->av.->aw.
            # ----(语音)LinearLayout(atb)->awh,awg
            # ----(分享)LinearLayout(abv)->ata->atb...->atj

    def process_text_message(self, row):
        try:
            el = row.find_elements_by_id("com.tencent.mm:id/pq")
            if el:
                ActionChains(self.driver).move_to_element(el[0]).click().pause(0.25).click().perform()
                full_screen_message_el = self.driver.find_element_by_id("com.tencent.mm:id/awl")
                message = full_screen_message_el.text
                TouchAction(self.driver).tap(self.driver.find_element_by_id("com.tencent.mm:id/awk")).perform()
                return message, None
        except Exception as e:
            self.logger.error(e)
            return "[文本消息]", None
        return None, None

    def process_image_message(self, row):
        try:
            el = row.find_elements_by_id("com.tencent.mm:id/aw3")
            if el:
                ActionChains(self.driver).move_to_element(el[0]).click().perform()
                # full_screen_message_el = self.driver.find_element_by_class_name("com.tencent.mm.ui.mogic.WxViewPager")
                # TouchAction(self.driver).long_press(full_screen_message_el).perform()
                # TouchAction(self.driver).tap(self.driver.find_element_by_xpath('//*[@text="保存图片"]/../../..')).perform()
                TouchAction(self.driver).tap(self.driver.find_element_by_id('com.tencent.mm:id/cqq')).perform()
                toast = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(@text,'图片已保存至')]")))
                toast_message = toast.text
                self.driver.press_keycode(4)
                if toast_message:
                    # file name:  2020-02-13 13:14 wx_camera_1581570852980.jpg
                    # tencent/MicroMsg/WeiXin/ -> /sdcard/tencent/MicroMsg/WeiXin/
                    # 获取到这个文件夹的最后一个文件就可以
                    filename = self.exec("ls -t {}| head -n1".format(self.wechat_file_path))
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
                # gi9->com.tencent.mm:id/atb
                ActionChains(self.driver).move_to_element(
                    el[0].find_element_by_id("com.tencent.mm:id/atb")).click().perform()
                # 视频页面: 点击更多
                ActionChains(self.driver).move_to_element(
                    self.driver.find_element_by_id("com.tencent.mm:id/gig")).click().perform()
                # 视频页面: 点击保存按钮
                TouchAction(self.driver).tap(self.driver.find_element_by_xpath('//*[@text="保存视频"]/../../..')).perform()
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
            el = row.find_elements_by_id("com.tencent.mm:id/awh")
            if el:
                return "[语音消息]" + el[0].get_attribute("text"), None
        except Exception as e:
            self.logger.error(e)
            return "[语音消息]", None
        return None, None

    def process_other_message(self, row):
        try:
            # el = row.find_elements_by_id("com.tencent.mm:id/abv")
            return "[其它消息]", None
        except Exception as e:
            self.logger.error(e)
            return "[其它消息]", None
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
            el = self.driver.find_element_by_id("com.tencent.mm:id/l2")
            ActionChains(self.driver).move_to_element(el).click().pause(0.25).click().pause(1).perform()
        except Exception as e:
            self.logger.error(e)

    def start(self):
        # self.select_tab('消息')
        # self.scroll_top()
        self.conversion_list()
        # 回到顶部，准备下一轮
        input("按任意键推出...")

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
