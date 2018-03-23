#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/7 0007.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408
import os
import sys

print('-----------获取本文件地址----------')
print(os.path.realpath(__file__))
print(os.path.abspath(__file__))  # 推荐方法

# 注意这两个方法的分隔符，不推荐使用
print(__file__)
print(sys.argv[0])


print('-----------获取本文件所在目录----------')
print(os.path.dirname(os.path.realpath(__file__)))
print(os.path.split(os.path.realpath(__file__))[0])
print(os.getcwd())
print(sys.path[0])

print('-----------获取上级目录----------')
print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
print(os.path.abspath(os.path.dirname(os.getcwd())))
print(os.path.abspath(os.path.join(os.getcwd(), "..")))

print('-----------获取上上级目录---------')
print(os.path.abspath(os.path.join(os.getcwd(), "../..")))

print('-----------本级目录下新建目录---------')
print(os.path.abspath(os.path.join(os.getcwd(), "img")))

print('-----------本盘符下新建目录---------')
print(os.path.abspath(os.path.join(os.getcwd(), "/img")))
