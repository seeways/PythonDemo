#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/8 0008.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408
# 1. 利用os模块编写一个能实现dir -l输出的程序。
# 2. 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
# V2.0 优化函数
import os


def dir_l():
    print(os.listdir('.'))


"""
root 当前目录路径
dirs 当前路径下所有子目录
files 当前路径下所有非目录子文件
"""


def get_files(file_name, dir_path=os.path.abspath(".")):
    for root, dirs, files in os.walk(dir_path):  # 获取当前目录的所有子目录和文件
        for file_path in files:
            if file_name in file_path:
                print(os.path.join(root, file_path))


if __name__ == '__main__':
    # dir_l()  # 我的理解是输出当前目录所有文件名
    get_files("test")  # 我的理解是模糊匹配
