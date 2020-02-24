from appium import webdriver

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait


class WechatDriver(object):
    # https://appium.io/docs/en/writing-running-appium/caps/
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'Android-HUAWEI',
        # 'platformVersion': '10',
        # 'unid':'CLB7N18B07008885',
        'appPackage': 'com.tencent.mm',
        'appActivity': 'com.tencent.mm.ui.LauncherUI',
        'newCommandTimeout': 300,
        # "deviceId": "192.168.2.241:5555",
        # "adbPort": 5555,
        # "dontStopAppOnReset": True,
        'noReset': True,
        # 'app':'the-apk-path-if-appPackage-or-appActivity-is-not-specialfied'
    }

    def __init__(self):
        # Espresso,UIAutomator2,UIAutomator
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        self.conversions = {}
        self.first_row = None
        self.last_row = None
        self.wait = WebDriverWait(self.driver, 300)
        self.wait_list_page()


    def wait_list_page(self):
        print(self.driver.current_activity)
        # timeout = 0
        # while timeout < 10:
        #     bottom = self.driver.find_elements_by_id('com.tencent.mm:id/bw')
        #     if len(bottom) == 0:
        #         timeout -= 1
        #         time.sleep(1)
        #     else:
        #         print("cost {} seconds to get into the list page.".format(timeout))
        #         break
        # else:
        #     print("Can't get into the list page.")
        #     exit(1)
        # self.driver.wait_activity()
        bottom = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/bw')))
        print(bottom)

    def select_tab(self, tab_name, count=1):
        # 底部的
        # RelativeLayout(com.tencent.mm:id/bw)->LinearLayout->RelativeLayout(点击区域)->LinearLayout->RelativeLayout,TextView(com.tencent.mm:id/dkb)
        # bottom = self.driver.find_element_by_id('com.tencent.mm:id/bw')
        # tabs = bottom.find_elements_by_xpath('//*[@resource-id="com.tencent.mm:id/dkb"]/../..')
        # bottom.screenshot("bottom.png")
        tabs = self.driver.find_elements_by_xpath('//*[@resource-id="com.tencent.mm:id/dkb"]/../..')
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
                return
        # selected_tab.click()
        action = TouchAction(self.driver)
        # action.tap(tabs[0], x=50, y=50, count=count)
        # action.wait(1000)
        # action.tap(tabs[1], x=50, y=50, count=count)
        # action.wait(1000)
        # action.tap(tabs[2], x=50, y=50, count=count)
        # action.wait(1000)
        # action.tap(tabs[3], x=50, y=50, count=count)
        # action.wait(1000)
        if count == 2:
            action.tap(selected_tab, count=count).wait(260).tap(selected_tab)
        else:
            action.tap(selected_tab)
        action.perform()
        time.sleep(0.1)

    def conversion_list(self):
        conversion_listview = self.driver.find_element_by_id("com.tencent.mm:id/dcf")
        rows = conversion_listview.find_elements_by_id("com.tencent.mm:id/bah")
        first_row = None
        last_row = None
        for row in rows:
            if not first_row:
                first_row = row
            last_row = row
            self.conversion_detail(row)
        if conversion_listview.get_attribute("scrollable") and (
                first_row != self.first_row or last_row != self.last_row):
            if first_row != last_row:
                self.scroll_down(last_row, first_row)
                self.conversion_list(last_row, first_row)
        self.first_row = first_row
        self.last_row = last_row

    def conversion_detail(self, row):
        message_count = 0
        title = ""
        last_message = ""
        els = row.find_elements_by_id("com.tencent.mm:id/op")
        if len(els) > 0:
            message_count = els[0].get_attribute("text")
        els = row.find_elements_by_id("com.tencent.mm:id/bai")
        if len(els) > 0:
            message_count = "100+"
        els = row.find_elements_by_id("com.tencent.mm:id/baj")
        if len(els) > 0:
            title = els[0].get_attribute("text")
        row.find_elements_by_id("com.tencent.mm:id/bal")
        if len(els) > 0:
            last_message = els[0].get_attribute("text")
        print("Title:{}\nCount:{}\nLast message:{}\n".format(title, message_count, last_message))
        # row.click()
        TouchAction(self.driver).tap(row).perform()
        # 进入了详情页面
        self.conversion_detail_messages(title)
        # 回调列表页面
        self.driver.press_keycode(4)

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
                actions = ActionChains(self.driver)
                actions.move_to_element(el[0])
                actions.double_click()
                actions.perform()
                TouchAction(self.driver).tap(el[0], count=2).perform()
                TouchAction(self.driver).tap(el[0]).wait(100).tap(el[0]).perform()
                TouchAction(self.driver).press(el[0]).release().wait(100).press(el[0]).release().perform()
                try:
                    full_screen_message_el = self.driver.find_element_by_id("com.tencent.mm:id/awl")
                    message = full_screen_message_el.text
                    TouchAction(self.driver).tap(self.driver.find_element_by_id("com.tencent.mm:id/awk")).perform()
                except Exception as e:
                    print(e)
            time.sleep(0.2)
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
        result = self.driver.execute_script('mobile: shell', {
            'command': 'sh',
            'args': [cmd],
            'includeStderr': True,
            'timeout': 5000
        })
        print(result['stdout'])

    def scroll_top(self):
        el = self.driver.find_element_by_id("com.tencent.mm:id/l2")
        if el.get_attribute("clickable"):
            # TouchAction(self.driver).press(el, x=200, y=100).release() \
            #     .wait(100).press(el, x=210, y=90).release().perform()
            # TouchAction(self.driver).tap(el, x=200, y=200).perform()
            # self.driver.execute_script("mobile: scroll", {"direction": "down"})
            self.driver.swipe(100, 300, 100, 1000, 200)
        else:
            print("can't find title bar")

    def scroll_down(self, from_row, to_row):
        # scroll() 与swipe()的区别: swipe是可以根据自己需要设置滑动的距离，而scroll是根据页面中两个元素位置距离进行滑动。
        # self.driver.execute_script("mobile: scroll", {"direction": "down"})
        # item = self.driver.find_element_by_android_uiautomator(
        #     'new UiScrollable(new UiSelector().scrollable(true).instance(0)).getChildByText(new UiSelector().className("android.widget.TextView"), "'
        #     + item_name + '")')
        # actions = TouchAction(self.driver)
        # actions.press(from_row)
        # actions.move_to(to_row)
        # actions.release()
        # actions.perform()
        # self.driver.swipe(x1, y1, x2, y2, duration)
        # self.driver.execute_script("mobile: scrollBackTo", {"direction": "down"})
        self.driver.scroll(from_row, to_row, duration=200)

    def scroll_up_and_down(self):
        conversion_listview = self.driver.find_element_by_id("com.tencent.mm:id/dcf")
        rows = conversion_listview.find_elements_by_id("com.tencent.mm:id/bah")
        first_row = None
        last_row = None
        if len(rows) > 3:
            first_row = rows[1]
            last_row = rows[-2]
        self.scroll_down(last_row, first_row)
        time.sleep(1)
        self.scroll_top()
        print(self.driver.current_activity)
        self.select_tab("消息", count=2)

    def screenshot(self):
        bottom = self.driver.find_element_by_id('com.tencent.mm:id/bw')
        # tab1 = bottom.find_elements_by_xpath('//*[@resource-id="com.tencent.mm:id/bw"]/android.widget.LinearLayout[1]')
        tab1 = bottom.find_elements_by_xpath('.//android.widget.LinearLayout[1]')
        # el = self.driver.find_element_by_id("")
        tab1.screenshot("tab1.png")

    # def toast_message(self):
    #     xpath = "//*[contains(@text,'图片已保存')]"
    #     toast = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    #     message = toast.text
    #     print("text:" + message)
    #     # print("class:" + toast.get_attribute("class"))
    #     toast = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "android.widget.Toast")))
    #     message = toast.text
    #     print("text:" + message)
    #     print(toast.get_attribute("class"))
    #     return message

    def start(self):
        self.select_tab('消息')
        self.conversion_list()
        # 回到顶部，准备下一轮
        self.scroll_top()
        time.sleep(3)


if __name__ == "__main__":
    driver = WechatDriver()
    driver.start()
