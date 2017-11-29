#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/11/28 0028
# @Author  : TaoYuan (1876665310@qq.com)
# @Link    : http://blog.csdn.net/lftaoyuan  Python互助学习qq群：315857408
# @Version : V1.0.0

from functools import partial

print('---------无关键词参数--------')


def mod(n, m):
    return n % m


mod_by_100 = partial(mod, 100)
print(mod(100, 7))  # 2
print(mod_by_100(7))  # 2

print('---------进制转换--------')

str2int = lambda x, base=2: int(x, base)
print(str2int('10000'))
print(str2int('12345', 16))
print(str2int('123456', base=8))

bin2dec = partial(int, base=2)
print(bin2dec('0b10001'))  # 17
print(bin2dec('10001'))  # 17

hex2dec = partial(int, base=16)
print(hex2dec('0x67'))  # 103
print(hex2dec('67'))  # 103


