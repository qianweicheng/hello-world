#!/usr/bin/env python3
import logging

from wechat.driver2 import WechatDriver2

logging.basicConfig(level=logging.INFO)
if __name__ == "__main__":
    driver = WechatDriver2()
    driver.start()
    logging.info("程序退出.")
