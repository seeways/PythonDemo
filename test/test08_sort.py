#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/20 0020.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408


list1 = [7, -8, 5, 4, 0, -2, -5]

result1 = sorted(list1)  # 从小到大
result2 = sorted(list1, key=lambda x: (x < 0, abs(x)))  # 先排正负，再拍大小
result3 = sorted(list1, key=lambda x: (x < 0))  # 从大到小

print(result1)
print(result2)
print(result3)
"""
[-8, -5, -2, 0, 4, 5, 7]
[0, 4, 5, 7, -2, -5, -8]
[7, 5, 4, 0, -8, -2, -5]
"""