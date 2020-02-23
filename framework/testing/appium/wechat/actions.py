#!/usr/bin/env python3
import subprocess


def pull_files_from_device(filepath, dist="./images/"):
    # 单个文件: adb pull /sdcard/tencent/MicroMsg/WeiXin/${filepath} .
    # 文件夹: adb pull /sdcard/tencent/MicroMsg/WeiXin .
    cmd = "adb pull {} ./images/".format(filepath)
    status = subprocess.call(cmd, shell=True)
    return status


if __name__ == "__main__":
    pull_files_from_device("/sdcard/tencent/MicroMsg/WeiXin/wx_camera_1545546944630.jpg", "../images")
