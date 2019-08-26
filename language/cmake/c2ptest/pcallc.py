#!/usr/bin/env python3
import ctypes
l1=ctypes.cdll.LoadLibrary
lib=l1("./libmybridge.dylib")
print('****load finsh****')
def hello(name, a=None, b=None, c=None):
    print("{}-{}-{}-{}".format(name, a, b, c))
    r = lib.pcallc("ls -l")
    print("in python:\nname:{}, result:{}".format(name,r))
    return 100
