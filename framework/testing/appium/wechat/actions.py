#!/usr/bin/env python3
import signal
import subprocess


def pull_files_from_device(filepath, dest="./attachments/"):
    # 单个文件: adb pull /sdcard/tencent/MicroMsg/WeiXin/${filepath} .
    # 文件夹: adb pull /sdcard/tencent/MicroMsg/WeiXin .
    cmd = "adb pull {} {}".format(filepath, dest)
    status = subprocess.call(cmd, shell=True)
    return status


def read_input_with_timeout(prompt, timeout=3):
    class InputTimeoutError(Exception):
        pass

    def interrupted(signum, frame):
        raise InputTimeoutError("timeout:{},{}".format(signum, frame))

    signal.signal(signal.SIGALRM, interrupted)
    signal.alarm(timeout)
    try:
        value = input(prompt)
        signal.alarm(0)
        return value
    except InputTimeoutError:
        pass
    return None


if __name__ == "__main__":
    # pull_files_from_device("/sdcard/tencent/MicroMsg/WeiXin/wx_camera_1545546944630.jpg")
    while True:
        data = read_input_with_timeout("是否继续", timeout=3)
        print(data)
