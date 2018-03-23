#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-16 10:23:35
# @Author  : TaoYuan (1876665310@qq.com)
# @Link    : https://github.com/seeways or http://blog.csdn.net/lftaoyuan
# @Version : $Id$

#  请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：

#  ax2 + bx + c = 0(a!=0)的两个解。
import math


def quadratic(a, b, c):
    for i in a, b, c:
        if not isinstance(i, (int, float)):
            raise TypeError('int or float')

    if a == 0:
        raise SyntaxError("error! a != 0")

    d = b ** 2 - 4 * a * c
    if d < 0:
        return print('error')
    elif d >= 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return x1, x2


if __name__ == '__main__':
    print(quadratic(2, 3, 1))  # => (-0.5, -1.0)
    print(quadratic(1, 3, -4))  # => (1.0, -4.0)
