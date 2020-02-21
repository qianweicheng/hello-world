import time

from appium import webdriver

from wechat.driver import WechatDriver

if __name__ == "__main__":
    driver = WechatDriver()
    driver.start()
    # driver.test_selection()
    # driver.scroll_up_and_down()
    time.sleep(3)
