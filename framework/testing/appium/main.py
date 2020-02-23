import logging

from wechat.driver2 import WechatDriver2

logging.basicConfig(level=logging.INFO)
if __name__ == "__main__":
    driver = WechatDriver2()
    driver.start()
    logging.info("正在退出...")
