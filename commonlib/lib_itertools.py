#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/15 0015.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408
# Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数
import itertools

# count()会创建一个无限的迭代器
natuals = itertools.count(1)
for n in natuals:
    print(n)

# cycle()会把传入的一个序列无限重复下去
# cs = itertools.cycle("ABC")
# for c in cs:
#     print(c)

# repeat()负责把一个元素无限重复下去,arg2限定次数
# ns = itertools.repeat("ABC", 3)
# for n in ns:
#     print(n)

# takewhile()函数根据条件判断来截取出一个有限的序列
# natuals = itertools.count(1)
# ns = itertools.takewhile(lambda x: x <= 10, natuals)
# print(list(ns))

# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
# for c in itertools.chain("ABC", "XYZ"):
#     print(c)

# groupby()把迭代器中相邻的重复元素挑出来放在一起
# for key, group in itertools.groupby("ABBASID"):
#     print(key, list(group))
# # A ['A', 'a', 'a']
# # B ['B', 'B', 'b']
# # C ['c', 'C']
# # A ['A', 'A', 'a']