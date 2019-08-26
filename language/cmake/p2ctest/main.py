#!/usr/bin/env python3
import ctypes
l1=ctypes.cdll.LoadLibrary
lib=l1("./pcallc.so")
a = lib.hello(3)
print(a)
print('****finsh****')