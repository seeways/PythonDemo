#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-24 14:13:06
# @Author  : TaoYuan (1876665310@qq.com)
# @Link    : http://blog.csdn.net/lftaoyuan  Python互助学习qq群：315857408
# @Version : $Id$

L_num = [1, 0, -9, 22, -89]
L_str = ['bob', 'about', 'Zoo', 'Credit']

# 假设我们用一组tuple表示学生名字和成绩：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0]


def by_score(t):
    return t[1]


if __name__ == '__main__':
    # print("-" * 15, "对list排序", "-" * 15)
    # print(sorted(L_num))
    #
    # print("-" * 15, "用key函数自定义排序", "-" * 15)
    # print(sorted(L_num, key=abs))
    #
    # print("-" * 15, "默认str排序，按ASCII排序，Z>a", "-" * 15)
    # print(sorted(L_str))
    #
    # print("-" * 15, "忽略大小写排序", "-" * 15)
    # print(sorted(L_str, key=str.lower))
    #
    # print("-" * 15, "忽略大小写并反向排序", "-" * 15)
    # print(sorted(L_str, key=str.lower, reverse=True))

    # print("-" * 50)
    print("-" * 15, "用sorted()对L分别按名字排序", "-" * 15)
    L2 = sorted(L, key=by_name)
    print(L2)
    print("-" * 15, "按成绩排序", "-" * 15)
    L2 = sorted(L, key=by_score)
    print(L2)
