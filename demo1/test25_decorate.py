#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-28 15:47:14
# @Author  : TaoYuan (1876665310@qq.com)
# @Link    : http://blog.csdn.net/lftaoyuan  Python互助学习qq群：315857408
# @Version : $Id$


# 由于log()是一个decorator，返回一个函数，
# 所以，原来的now()函数仍然存在，
# 只是现在同名的now变量指向了新的函数，
# 于是调用now()将执行新函数，
# 即在log()函数中返回的wrapper()函数。

# wrapper()函数的参数定义是(*args, **kw)，
# 因此，wrapper()函数可以接受任意参数的调用。
# 在wrapper()函数内，首先打印日志，再紧接着调用原始函数。

# 初阶log函数
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


# 高阶log函数
def log2(text):
    def decorate(func):
        def wrapper(*args, **kw):
            print("%s %s:" % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorate


@log
@log2('execute')
def now():
    print('2017-11-28')


if __name__ == '__main__':
    now()
