#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-20 11:21:52
# @Author  : TaoYuan (1876665310@qq.com)
# @Link    : http://blog.csdn.net/lftaoyuan  Python互助学习qq群：315857408
# @Version : $Id$
# 迭代

# 判断迭代
from collections import Iterable


d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key, d[key])

print("\n")
for k, v in enumerate(d):
    print(k, v)

print(isinstance(d, Iterable))

print(isinstance("123", Iterable))

print(isinstance(123, Iterable))
