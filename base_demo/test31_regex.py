#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/12 0012.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408
# Regular Expression
import re

# string
s1 = "ABC\\-001"  # python lang support Escape Sequence
s2 = r"ABC\\-001"  # so, recommend use r''
regex_01 = r"^\d{3}\-\d{3,9}$"

#  project commonly used method
if re.match(r"your regex", "user input content"):
    print("ok")
else:
    print("error")

# split string
s3 = "a b c   d         e"
s4 = "a,b,c  ,d         e"
regex_02 = r"\s+"
regex_03 = r"[\s\,]+"

# grouping
s5 = "029-1234567"
s6 = "0755-123456"
regex_group1 = r"^(\d{3})-(\d{3,8})$"  # 3个数字，3-8个数字
regex_group2 = r"^(\d{3,4})-(\d{6})$"  # 3-4个数字，6个数字

if __name__ == '__main__':
    # string
    print(s1)  # ABC\-001
    print(s2)  # ABC\\-001
    print(re.match(regex_01, "029-123456"))  # <_sre.SRE_Match object; span=(0, 10), match='029-123456'>
    print(re.match(regex_01, "0755-123456"))  # None
    print("-" * 20)
    # split string
    print(s3.split(" "))  # nomal
    print(s4.split(","))  # nomal
    print(re.split(regex_02, s3))  # regex
    print(re.split(regex_03, s4))  # regex
    print("-" * 20)
    # grouping
    # group(0)永远是原始字符串
    m1 = re.match(regex_group1, s5)  # 这个限定了第一组只能用3个数字，否则报错
    print(m1.group(0))
    print(m1.group(1))
    print(m1.group(2))
    m2 = re.match(regex_group2, s6)  # 这个限定了第二组只能是6位数字，否则报错
    print(m2.group(0))
    print(m2.group(1))
    print(m2.group(2))
