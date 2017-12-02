#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/2 0002.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408
# 定制类


# __str__ 和 __repr__
class Student(object):
    """docstring for Student"""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Student object {0}".format(self.name)

    __repr__ = __str__  # 格式化栈显示


# __iter__该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器

    def __iter__(self):
        return self  # 实例本身就是迭代对象

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:
            raise StopIteration()
        return self.a  # 返回下一个值

    # __getitem__ :把__iter__变成数组
    # 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。
    # 还有一个__delitem__()方法，用于删除某个元素
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a


# __getattr__ 正常情况下，当我们调用类方法或属性时，不存在就报错
# 为了避免这个错误，可以用__getattr__动态返回一个属性
class Chain(object):
    """docstring for Chain"""

    def __init__(self, path=""):
        self.path = path

    def __getattr__(self, path):
        return Chain("{0}/{1}".format(self.path, path))
        # return Chain("%s/%s" % (self.path, path))

    def __str__(self):
        return self.path

    __repr__ = __str__


# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用
class Student_call(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print("My name is {0}".format(self.name))

# s = Student_call("taoyuan")
# print(s())
