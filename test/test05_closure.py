#!/usr/bin/env python
# -*- coding: utf-8 -*-

def count():
    fs = []
    print("come in ")
    for i in range(1, 5):
        print("create f%s" % i)
        def f():
            return i * i

        fs.append(f)
    return fs

f1, f2, f3, f4 = count()
print(f1(), f2(), f3(), f4())


# def count1():
#     fs = []
#     for i in range(1, 4):
#         def f(j):
#             def g():
#                 return j * j
#             return g
#         fs.append(f(i))  # �˲��踳ֵ
#     return fs
#
# f1, f2, f3 = count1()
# print(f1(), f2(), f3())


# def count2():
#     def f(j):
#         def g():
#             return j * j
#
#         return g
#
#     fs = []
#     for i in range(1, 4):
#         fs.append(f(i))  # f(i)���̱�ִ�У����i�ĵ�ǰֵ������f()
#     return fs
#
#
# f1, f2, f3 = count2()
# print(f1(), f2(), f3())
