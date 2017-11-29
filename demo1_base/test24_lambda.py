#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-28 14:16:26
# @Author  : TaoYuan (1876665310@qq.com)
# @Link    : http://blog.csdn.net/lftaoyuan  Python互助学习qq群：315857408
# @Version : $Id$
# #des: 匿名函数

# 在Python中，对匿名函数提供了有限支持。还是以map()函数为例，计算f(x)=x2时，除了定义一个f(x)的函数外，还可以直接传入匿名函数：
from typing import Iterator


# l = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))


# print(l)


def build(x, y):
    return lambda: x * x + y * y


def is_odd(n):
    return n % 2 == 1


if __name__ == '__main__':
    # print(f)
    # print(f(2, 3))
    L = list(filter(is_odd, range(1, 20)))
    print(L)
    L2 = list(filter(lambda n: n % 2, range(1, 20)))
    print(L2)
