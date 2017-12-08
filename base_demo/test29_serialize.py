#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/8 0008.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408
# 序列化

import pickle

# write serialize(bytes) in file
# d = dict(name="Bob", age=20, score=88)
# print(pickle.dumps(d))  # b'\x80\x03}q\x00(X\x04\x00\x00\x00nameq\x01X\x03\x00\x00\x00Bobq\x02X\x03\x00\x00\x00ageq\x03K\x14X\x05\x00\x00\x00scoreq\x04KXu.'
#
# f = open("dump.txt", "wb")
# pickle.dump(d, f)
# f.close()

# read serialize
a = open("dump.txt", "rb")
b = pickle.load(a)
a.close()
print(b)  # {'name': 'Bob', 'age': 20, 'score': 88}
