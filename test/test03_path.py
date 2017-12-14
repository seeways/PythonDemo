#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/7 0007.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408
import os


# 写法1
# try:
#     f = open(os.path.abspath(os.path.join(os.getcwd(), "../work/test.txt")), "r")
#     print(f.read())
# finally:
#     if f:
#         f.close()

# 写法2
# with open(os.path.abspath(os.path.join(os.getcwd(), "../work/test.txt")), "r") as f:
#     print(f.read())

# 写法3(推荐)
# with open(os.path.abspath(os.path.join(os.getcwd(), "../work/test.txt")), "r") as f:
#     for line in f.readlines():
#         print(line.strip()) # 把末尾的'\n'删掉


def return_sum( a, b):
    __a = int(a)
    __b = int(b)
    return __a + __b


if __name__ == '__main__':
    print(return_sum(1, 2))

