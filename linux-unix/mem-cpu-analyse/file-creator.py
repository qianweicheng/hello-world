#!/usr/bin/env python3
import time
import datetime
import os


def looper():
    index = 0
    while True:
        index = index + 1
        filename = "{}.txt".format(index)
        with open(filename, mode='w') as file:
            file.write("{}".format(datetime.datetime.now()))
            print("{}\tcreate file:{}".format(index, filename))
        time.sleep(1)
        # os.remove(filename)


if __name__ == "__main__":
    looper()
