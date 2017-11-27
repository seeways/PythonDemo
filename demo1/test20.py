#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-23 11:24:23
# @Author  : TaoYuan (1876665310@qq.com)
# @Link    : http://blog.csdn.net/lftaoyuan  Python互助学习qq群：315857408
# @Version : $Id$


L = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def f(x):
    return x * x


from functools import reduce


def add(x, y):
    return x + y


def add2(x, y):
    return x * 10 + y


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, "6": 6, '7': 7, '8': 8, '9': 9}[s]


def str2int(s):
    def add2(x, y):
        return x * 10 + y

    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, "6": 6, '7': 7, '8': 8, '9': 9}[s]
    # return reduce(lambda x, y: x * 10 + y, map(char2num, s))  简化版
    return reduce(add2, map(char2num, s))


if __name__ == '__main__':
    print(list(map(f, L)))

    print(list(map(str, L)))

    print(sum([1, 3, 5, 7, 9]))

    print(reduce(add, [1, 3, 5, 7, 9]))
    print(reduce(add2, [1, 3, 5, 7, 9]))

    print(reduce(add2, map(char2num, '13579')))
    print(str2int('13579'))
