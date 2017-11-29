#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/11/24 0024
# @Author  : TaoYuan (1876665310@qq.com)
# @Link    : http://blog.csdn.net/lftaoyuan  Python互助学习qq群：315857408
# @Version : V1.0.0

L1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
L2 = ['A', 'B', 'c', None, '  ']
L3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def is_odd(n):  # 是否奇数
    return n % 2 == 1


def not_empty(s):  # 不为空
    return s and s.strip()


def odd_iter():  # 奇数生成器
    n = 1
    while True:
        n += 2
        yield n


def not_divisible(n):  # 筛选函数
    return lambda x: x % n > 0


def primes():  # 生成素数列表
    yield 2
    it = odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(not_divisible(n), it)  # 构造新序列


if __name__ == '__main__':
    # print(list(filter(is_odd, L1)))  # [1, 3, 5, 7, 9]
    # print(list(filter(not_empty, L2)))  # ['A', 'B', 'c']
    # 打印100以内的素数:
    for n in primes():
        if n < 100:
            print(n)
        else:
            break
