#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-28 17:16:24
# @Author  : TaoYuan (1876665310@qq.com)
# @Link    : http://blog.csdn.net/lftaoyuan  Python互助学习qq群：315857408
# @Version : $Id$
# @des: 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
import functools
import time

# wrok 1
def metric(fn):
    def wrapper(*args, **kw):
        start_time = time.time()
        print('{0} executed in {1} ms'.format(fn.__name__, time.time() - start_time))
        return fn(*args, **kw)
    return wrapper


# work 2
def log(text=None):
    start_time = time.time()
    print("begin call:", round(start_time))
    def decorate(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            return func(*args, **kw), print("end call:{0} \n spend time: {1} s".format(round(time.time()), round(time.time() - start_time)))
        return wrapper
    return (decorate, print("text:%s" % text ))[0] if text.__str__() == text else decorate(text)


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

print('-------work2-------')


@log
def test1():
    time.sleep(2)


@log('这里是参数')
def test2():
    time.sleep(3)


test1()

test2()
