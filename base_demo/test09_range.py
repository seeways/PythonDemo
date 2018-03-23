#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-15 17:26:16
# @Author  : TaoYuan (1876665310@qq.com)
# @Link    : https://github.com/seeways or http://blog.csdn.net/lftaoyuan
# @Version : $Id$

sum = 0

# range(101) 也可以
for x in range(0, 101):
    sum += x

print("for:%d" % sum)

sum = 0
n = 100
while n > 0:
    sum += n
    n -= 1

print("while:%d" % sum)

L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print("Hello", name)
