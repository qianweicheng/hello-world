#!/usr/bin/env python3
import subprocess


def pull_files_from_device(filepath):
    # 单个文件: adb pull /sdcard/tencent/MicroMsg/WeiXin/${filepath} .
    # 文件夹: adb pull /sdcard/tencent/MicroMsg/WeiXin .
    status = subprocess.call("adb pull {} ../images/".format(filepath), shell=True)
    return status


if __name__ == "__main__":
    pull_files_from_device("/sdcard/tencent/MicroMsg/WeiXin/wx_camera_1545546944630.jpg")
