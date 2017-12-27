#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/27 0027.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408


def addlist(alist):
    for i in alist:
        yield i + 1


alist = [1, 2, 3, 4]
for x in addlist(alist):
    print(x)

print("--------------")


def h():
    print('study yield')
    yield 5
    print('go on!')


c = h()
h_d1 = next(c)  # study yield
c.close()
# h_d2 = next(c)
"""
study yield
go on!
Traceback (most recent call last):
  File "D:/idea/workspace/pythonSpace/PythonDemo/static/yield_demo.py", line 35, in <module>
    h_d2 = next(c)
StopIteration
"""

print("--------------")


def s():
    print('study yield')
    m = yield 5
    print(m)
    d = yield 16
    print('go on!')


c = s()
s_d1 = next(c)  # 相当于send(None)
s_d2 = c.send('Fighting!')  # (yield 5)表达式被赋予了'Fighting!'
print('My Birth Day:', s_d1, '.', s_d2)
"""
study yield
Fighting!
My Birth Day: 5 . 16
"""