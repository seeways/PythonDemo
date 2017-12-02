#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/1 0001.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408

import inspect

class G(object):
    pass

class D(object):
    def __init__(self):
        print("D")


class E(object):
    def __init__(self):
        print("E")


class F(object):
    def __init__(self):
        print("F")


class C(D, F):
    def __init__(self):
        print("C")


class B(E, G):
    def __init__(self):
        print("B")


class A(B, C):
    def __init__(self):
        print("A")


if __name__ == '__main__':
    print(inspect.getmro(A))
