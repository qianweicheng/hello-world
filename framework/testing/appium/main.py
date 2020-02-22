import time

from wechat.driver import WechatDriver
from wechat.driver2 import WechatDriver2

if __name__ == "__main__":
    driver = WechatDriver2()
    driver.start()
    input("按任意键推出...")
    print("正在推出...")
