#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/15 0015.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408
# 利用Python提供的itertools模块，我们来计算这个序列的前N项和
import itertools


def pi(N):
    """
    step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.  for x in range(2 * N) if x % 2
    step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...  itertools.cycle((4, -4))
    step 4: 求和:sum()
    感觉水平还是不行
    """
    n = itertools.cycle((4, -4))
    return sum((next(n) / x) for x in range(2 * N) if x % 2)


# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')
