from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait

from wechat import post_runnable


class WechatDriver2(object):
    # https://appium.io/docs/en/writing-running-appium/caps/
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'HUAWEI',
        'platformVersion': '10',
        'appPackage': 'com.tencent.mm',
        'appActivity': 'com.tencent.mm.ui.LauncherUI',
        'newCommandTimeout': 120,
        # 'unid':'CLB7N18B07008885',
        'noReset': True,
        # 'app':'the-apk-path-if-appPackage-or-appActivity-is-not-specialfied'
    }

    def __init__(self):
        # Espresso,UIAutomator2,UIAutomator
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        self.conversions = {}
        self.wait = WebDriverWait(self.driver, 300)
        self.wait_list_page()

    def raw_driver(self):
        return self.driver

    def wait_list_page(self):
        print(self.driver.current_activity)
        self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/bw')))

    def select_tab(self, tab_name, count=1):
        # 底部的
        # RelativeLayout(com.tencent.mm:id/bw)->LinearLayout->RelativeLayout(点击区域)->LinearLayout->RelativeLayout,TextView(com.tencent.mm:id/dkb)
        # bottom = self.driver.find_element_by_id('com.tencent.mm:id/bw')
        # tabs = bottom.find_elements_by_xpath('//*[@resource-id="com.tencent.mm:id/dkb"]/../..')
        # bottom.screenshot("bottom.png")
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
                print("unknown {} tab".format(tab_name))
        else:
            print("tab数不对")
        if not selected_tab:
            return
        if count == 2:
            ActionChains(self.driver).move_to_element(selected_tab).click().pause(0.25).click().perform()
        else:
            ActionChains(self.driver).move_to_element(selected_tab).click().perform()
        time.sleep(0.1)

    def conversion_list(self):
        self.select_tab("消息", count=2)
        listview = self.driver.find_element_by_id("com.tencent.mm:id/dcf")
        rows = listview.find_elements_by_id("com.tencent.mm:id/bah")
        has_new_message = False
        for row in rows:
            r = self.conversion_detail(row)
            has_new_message = has_new_message or r
        if has_new_message:
            post_runnable(self.conversion_list)

    def conversion_detail(self, row):
        message_count = ""
        title = ""
        last_message = ""
        # 单聊消息数
        els = row.find_elements_by_id("com.tencent.mm:id/op")
        if len(els) > 0:
            message_count = els[0].get_attribute("text")
        # 群聊新消息标记
        els = row.find_elements_by_id("com.tencent.mm:id/bai")
        if len(els) > 0:
            message_count = "1+"
        # 标题
        els = row.find_elements_by_id("com.tencent.mm:id/baj")
        if len(els) > 0:
            title = els[0].get_attribute("text")
        row.find_elements_by_id("com.tencent.mm:id/bal")
        if len(els) > 0:
            last_message = els[0].get_attribute("text")
        print("Title:{}\nCount:{}\nLast message:{}\n".format(title, message_count, last_message))
        # row.click()
        if message_count:
            TouchAction(self.driver).tap(row).perform()
            # 进入了详情页面
            self.conversion_detail_messages(title)
            # 回调列表页面
            self.driver.press_keycode(4)
        return message_count

    def conversion_detail_messages(self, room):
        # TODO
        rows = self.driver.find_elements_by_id("com.tencent.mm:id/ab")
        a = self.driver.device_time
        print("current time:{}".format(a))
        current_time = ''
        user = ''
        message = ''
        if not self.conversions.get(room):
            self.conversions[room] = []
        for row in rows:
            el = row.find_elements_by_id("com.tencent.mm:id/ai")
            if len(el) > 0:
                current_time = el[0].text
            el = row.find_elements_by_id("com.tencent.mm:id/pp")
            if len(el) > 0:
                user = el[0].text
            el = row.find_elements_by_id("com.tencent.mm:id/pq")
            if len(el) > 0:
                try:
                    ActionChains(self.driver).move_to_element(el[0]).click().pause(0.25).click().perform()
                    full_screen_message_el = self.driver.find_element_by_id("com.tencent.mm:id/awl")
                    message = full_screen_message_el.text
                    TouchAction(self.driver).tap(self.driver.find_element_by_id("com.tencent.mm:id/awk")).perform()
                except Exception as e:
                    print(e)
            print("Time:{}\nUser:{}\nMessage:{}\n".format(current_time, user, message))
            self.conversions[room].append({"user": user, "time": current_time, "message": message})
        print("==================================")

    def conversion_detail_send(self, text):
        # TODO
        edit = self.driver.find_elements_by_id("com.tencent.mm:id/aqe")
        edit.send_keys(text)

    def search(self, text):
        search_btn = self.driver.find_element_by_id("com.tencent.mm:id/c8")
        actions = TouchAction(self.driver)
        actions.tap(search_btn)
        actions.perform()

    def exec(self, cmd):
        try:
            # An unknown server-side error occurred while processing the command.
            # Original error: Appium server must have relaxed security flag set in order to run any shell commands
            result = self.driver.execute_script('mobile: shell', {
                'command': 'sh',
                'args': [cmd],
                'includeStderr': True,
                'timeout': 5000
            })
            print(result['stdout'])
        except Exception as e:
            print(e)

    def scroll_top(self):
        try:
            el = self.driver.find_element_by_id("com.tencent.mm:id/l2")
            if el.get_attribute("clickable"):
                ActionChains(self.driver).move_to_element(el).click().pause(0.25).click().perform()
            else:
                print("can't find title bar")
        except Exception as e:
            print(e)

    def start(self):
        self.select_tab('消息')
        self.conversion_list()
        # 回到顶部，准备下一轮
        self.scroll_top()
        time.sleep(3)

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
            print(e)