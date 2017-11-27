#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-27 20:12:56
# @Author  : TaoYuan (1876665310@qq.com)
# @Link    : http://blog.csdn.net/lftaoyuan  Python互助学习qq群：315857408
# @Version : $Id$
# @des : 利用闭包返回一个计数器函数，每次调用它返回递增整数：


def createCounter():
    def add_nums():  # 2. 添加计数
        n = 0
        while True:
            n = n + 1
            yield n

    y = add_nums()

    def counter():  # 1. 首先调用此函数
        return next(y)  # 3. 迭代计数

    return counter


if __name__ == '__main__':
    # 测试:
    counterA = createCounter()
    print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
    counterB = createCounter()
    if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
        print('测试通过!')
    else:
        print('测试失败!')
