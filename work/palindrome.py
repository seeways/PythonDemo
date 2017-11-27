#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/11/24 0024
# @Author  : TaoYuan (1876665310@qq.com)
# @Link    : http://blog.csdn.net/lftaoyuan  Python互助学习qq群：315857408
# @Version : V1.0.0
# @des     : 判断是否为回数


def is_palindrome(n):
    return str(n) == str(n)[::-1]  # 字符串倒过来如果==字符串，则为回数


if __name__ == '__main__':
    # 测试:
    output = filter(is_palindrome, range(1, 1000))
    print('1~1000:', list(output))
    if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99,
                                                      101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
        print('测试成功!')
    else:
        print('测试失败!')
