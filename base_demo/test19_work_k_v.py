#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-20 17:23:30
# @Author  : TaoYuan (1876665310@qq.com)
# @Link    : http://blog.csdn.net/lftaoyuan  Python互助学习qq群：315857408
# @Version : $Id$


def test_d(d):
    for k, v in d.items():
        return k, '=', v


def test_s(L):
    L2 = []
    for s in L:
        if isinstance(s, str):
            L2.append(s.lower())
    return L2


if __name__ == '__main__':
    # 测试:
    L1 = ['Hello', 'World', 18, 'Apple', None]
    L2 = test_s(L1)
    if L2 == ['hello', 'world', 'apple']:
        print('测试通过!')
    else:
        print('测试失败!')
