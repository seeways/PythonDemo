#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-29 11:57:01
# @Author  : TaoYuan (1876665310@qq.com)
# @Link    : http://blog.csdn.net/lftaoyuan  Python互助学习qq群：315857408
# @Version : $Id$
# @des     : 使用模块

import sys

__author__ = "TaoYuan"


def test():
    args = sys.argv
    if len(args) == 1:
        print("Hello {0}".format(args[0]))
    elif len(args) == 2:
        print("Hello {0}".format(args[1]))
    else:
        print("args too much!")


def _private_1(name):
    return "Hello {0}".format(name)


def _private_2(name):
    return 'Hi {0}'.format(name)


def public_one(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)


if __name__ == '__main__':
    test()
    print('----------')
    print(public_one("123"))
    print(public_one("123456"))
