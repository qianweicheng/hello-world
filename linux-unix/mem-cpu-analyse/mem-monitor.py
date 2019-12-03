#!/usr/bin/env python3
import subprocess
from io import StringIO
from time import sleep

keys = [
    "VmPeak",
    "VmSize",
    "VmHWM",
    "VmRSS",
    "VmData",
    "VmStk",
    "VmLib",
    "Threads"
]


# apt-get update -y && apt-get install vim, python3 -y
def getinfo(pid=None):
    pretty_print_header()
    if not pid:
        cmd = "ps aux | awk '$11~/java/{print $2}'"
        # cmd = "ps aux | awk '$11~/ss/{print $2}'"
        result = subprocess.getoutput(cmd)
        lines = result.splitlines()
        if len(lines) == 0:
            return
        pid = lines[0]
    while True:
        result = subprocess.getoutput("cat /proc/{}/status".format(pid))
        lines = result.splitlines()
        info = {}
        for line in lines:
            index = line.find(":")
            if index < 1:
                continue
            first = line[0:index]
            if first in keys:
                info[first] = line[index + 1:].strip()
        pretty_print_result(info)
        sleep(3)


def pretty_print_header():
    line = StringIO()
    hasvalue = False
    for key in keys:
        if hasvalue:
            line.write(",")
        else:
            hasvalue = True
        line.write(key)
    line.seek(0)
    print(line.readline())


def pretty_print_result(info):
    line = StringIO()
    hasvalue = False
    for key in keys:
        if hasvalue:
            line.write(",")
        else:
            hasvalue = True
        if info.get(key):
            line.write(info.get(key))
        else:
            pass
    line.seek(0)
    print(line.readline())


if __name__ == "__main__":
    getinfo()
