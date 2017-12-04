#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/4 0004.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408
from functools import reduce


def str2num(s):
    try:
        n = int(s)
    except ValueError as e:
        print("Not Integer,Will Be Convert To Float:", e)
        n = float(s)
    return n


def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    print("---------------------------")
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)


main()
