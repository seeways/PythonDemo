#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/14 0014.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408
# base64
import base64

s = b"i\xb7\x1d\xfb\xef\xff"
# def test():
#     s0 = b"Aladdin:open sesame"
#     print(repr(s0))
#     s1 = encodebytes(s0)
#     print(repr(s1))
#     s2 = decodebytes(s1)
#     print(repr(s2))
#     assert s0 == s2
base64.test()
# b'Aladdin:open sesame'
# b'QWxhZGRpbjpvcGVuIHNlc2FtZQ==\n'
# b'Aladdin:open sesame'
print("-----------------------")
# url encode
url_base64 = base64.urlsafe_b64encode(s)
print(url_base64)
print(base64.urlsafe_b64decode(url_base64))
print("-----------------------")
# normal
normal_base64 = base64.b64encode(s)
print(normal_base64)
print(base64.b64decode(normal_base64))
print("-----------------------")
# other
print(base64.encodebytes(s))  # encodebytes 对string进行base64编码
base64.decodebytes(b'abcd++//\n')  # decodebytes 解码一组base64数据
print(base64.encodestring(s))  # Legacy alias of encodebytes()
base64.decodestring(b'abcd++//\n')  # Legacy alias of decodebytes()
print(base64.standard_b64encode(s))  # 使用标准Base64字母表对字节进行编码,返回byteArray
base64.standard_b64encode(b'abcd++//')  # 使用标准Base64字母表对字节进行编码,返回byteArray
