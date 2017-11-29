#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-27 18:48:55
# @Author  : TaoYuan (1876665310@qq.com)
# @Link    : http://blog.csdn.net/lftaoyuan  Python互助学习qq群：315857408
# @Version : $Id$


def calc_sum(*args):
    x = 0
    for n in args:
        x = x + n
    return x


def lazy_sum(*args):
    def in_sum():
        x = 0
        for n in args:
            x = x + n
        return x
    return in_sum


if __name__ == '__main__':
    f = calc_sum(1, 3, 5, 7, 9)
    print(f)

    f = lazy_sum(1, 3, 5, 7, 9)
    print(f)
    print(f())
