#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/11/23 0023
# @Author  : TaoYuan (1876665310@qq.com)
# @Link    : http://blog.csdn.net/lftaoyuan  Python互助学习qq群：315857408
# @Version : V1.0.0


def wt_file():  # 写文件
    with open("test.txt", "wt") as out_file:
        out_file.write("test\n test2 \n\n test4")


def rd_file():  # 读文件
    with open("test.txt", "rt") as in_file:
        text = in_file.read()
    print(text)


if __name__ == '__main__':
    # 卸载本文件同级目录下
    wt_file()
    rd_file()
