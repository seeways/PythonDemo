#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-20 17:02:00
# @Author  : TaoYuan (1876665310@qq.com)
# @Link    : http://blog.csdn.net/lftaoyuan  Python互助学习qq群：315857408
# @Version : $Id$
from collections import Iterable


def findMinAndMax(L):
    if not isinstance(L, Iterable):
        raise TypeError("L not Iterable!")

    if 0 == len(L):
        return None, None

    min_num = L[0]
    max_num = L[0]
    for i in L:
        if i < min_num:
            min_num = i
        elif i > max_num:
            max_num = i
    return min_num, max_num


if __name__ == '__main__':
    # 测试
    if findMinAndMax([]) != (None, None):
        print('测试失败1!')
    elif findMinAndMax([7]) != (7, 7):
        print('测试失败2!')
    elif findMinAndMax([7, 1]) != (1, 7):
        print('测试失败3!')
    elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
        print('测试失败4!')
    elif findMinAndMax((1, 2, 3, 4, 5, 6)) != (1, 6):
        print('测试失败5!')
    else:
        print('测试成功!')
