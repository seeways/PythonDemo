#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-15 15:42:56
# @Author  : TaoYuan (1876665310@qq.com)
# @Link    : https://github.com/seeways or http://blog.csdn.net/lftaoyuan
# @Version : $Id$

# bmi低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖

height = 1.75
weight = 80.5

bmi = weight / (height ** 2)
print(bmi)

if bmi < 18.5:
    print("so light!")
elif 18.5 <= bmi < 25:
    print("nice!")
elif 25 <= bmi < 28:
    print("little heavy!")
elif 28 <= bmi < 32:
    print("fat!")
elif bmi > 32:
    print("so fat!!!")
