#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/14 0014.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408
# 学过C/C++的人应该都知道结构体，python里没有
# python中b'str'可以表示字节，所以，字节数组 = 二进制str，但是很麻烦
# 幸好有struct这个模块，pack函数把任意数据类型变成bytes
# https://docs.python.org/3/library/struct.html#format-characters
import base64
import struct

# pack的第一个参数是处理指令
# >I: >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
print(struct.pack(">I", 10240099))  # b'\x00\x9c@c'
# 后面的参数个数要和处理指令一致1024 0099
# print(base64.encodebytes(b'\x00\x9c@c'))  # b'AJxAYw==\n'
# unpack把bytes变成相应的数据类型：
print(struct.unpack(">IH", b'\xf0\xf0\xf0\xf0\x80\x80'))  # (4042322160, 32896)
# I：4字节无符号整数  H：2字节无符号整数
print("--------------------------")
s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
# BMP格式采用小端方式存储数据，文件头的结构按顺序如下
# 两个字节：'BM'表示Windows位图，'BA'表示OS/2位图；
# 一个4字节整数：表示位图大小；
# 一个4字节整数：保留位，始终为0；
# 一个4字节整数：实际图像的偏移量；
# 一个4字节整数：Header的字节数；
# 一个4字节整数：图像宽度；
# 一个4字节整数：图像高度；
# 一个2字节整数：始终为1；
# 一个2字节整数：颜色数。
print(struct.unpack("<ccIIIIIIHH", s))  # (b'B', b'M', 691256, 0, 54, 40, 640, 360, 1, 24)
