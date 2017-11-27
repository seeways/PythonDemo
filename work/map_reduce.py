#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/11/23 0023
# @Author  : TaoYuan (1876665310@qq.com)
# @Link    : http://blog.csdn.net/lftaoyuan  Python互助学习qq群：315857408
# @Version : V1.0.0
from functools import reduce


# print(str.upper())          # 把所有字符中的小写字母转换成大写字母
# print(str.lower())          # 把所有字符中的大写字母转换成小写字母
# print(str.capitalize())     # 把第一个字母转化为大写字母，其余小写
# print(str.title())          # 把每个单词的第一个字母转化为大写，其余小写
def normalize(name):  # 首字母大写，其余小写
    return name.capitalize()


def prod(L):  # 求积
    return reduce(lambda x, y: x * y, L)


def str2float(s):  # 要求reduce和map
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    n = s.index('.')
    return reduce(lambda x, y: x * 10 + y, map(char2num, s[:n] + s[n + 1:])) / (10 ** (len(s) - n - 1))


# def str2float(s):  # 实际中
#     return float(s)


if __name__ == '__main__':
    # 大小写转换测试:
    L1 = ['adam', 'LISA', 'barT']
    L2 = list(map(normalize, L1))
    print(L2)

    # 求乘积测试
    print('-' * 30)
    print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
    if prod([3, 5, 7, 9]) == 945:
        print('测试成功!')
    else:
        print('测试失败!')

    # str 2 float 测试
    print('-' * 30)
    print('str2float(\'123.456\') =', str2float('123.456'))
    print('str2float(\'12345.6\') =', str2float('12345.6'))
    if abs(str2float('123.456') - 123.456) < 0.00001:
        print('测试成功!')
    else:
        print('测试失败!')
