#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/15 0015.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408
# Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等
import hashlib

s = b"Nobody inspects the spammish repetition"
m = hashlib.md5()
m.update(b"Nobody inspects ")  # b'>\xf7)\xcc\xf0\xccV\x07\x9c\xa5F\xd5\x80\x83\xdc\x12'
m.update(b"the spammish repetition")  # b'>\xf7)\xcc\xf0\xccV\x07\x9c\xa5F\xd5\x80\x83\xdc\x12'
# 多次调用，update会累加参数进行运算
# m.update(s)  # bb649c83dd1ea5c9d9dec9a18df0ffe9
# print(m.digest())  # b'%\x8d3\xf9,:k\xe0?\xbb0+\xc4K\x94S'
print(m.hexdigest())

print("--------------")
# 常用 简写
# my_md5 = hashlib.md5()
# my_md5.update(s)
# my_md5.hexdigest()
print(hashlib.md5(s).hexdigest())
print(hashlib.sha1(s).hexdigest())
print(hashlib.sha256(s).hexdigest())
print(hashlib.sha512(s).hexdigest())

# bb649c83dd1ea5c9d9dec9a18df0ffe9
# 531b07a0f5b66477a21742d2827176264f4bbfe2
# 031edd7d41651593c5fe5c006fa5752b37fddff7bc4e843aa6af0c950f4b9406
# d0f4c14c48ad4837905ea7520cc4af700f6433ce0985e6bb87b6b4617cb944abf814bd53964ddbf55b41e5812b3afe90890c0a4db75cb04367e139fd62eab2e1


