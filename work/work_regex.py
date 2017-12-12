#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/12 0012.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408
# 1. 请尝试写一个验证Email地址的正则表达式
# 2. 可以提取出带名字的Email地址：
import re

regex_email = r"^([0-9a-zA-Z\u003C][0-9a-zA-Z\_\.\u003E\s]+?)\@([0-9a-zA-Z]+?)\.([a-z]{2,3})$"
regex_email_2 = r"^\u003C([0-9a-zA-Z\s]+?)\u003E[\s]+([0-9a-zA-Z][0-9a-zA-Z\_\.]+?)$"


def is_valid_email(content):
    return re.match(regex_email, content)


def name_of_email(content):
    if is_valid_email(content):
        temp = is_valid_email(content).group(1)
        if re.match(regex_email_2, temp):
            return re.match(regex_email_2, temp).group(1)
        else:
            return temp


# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')

print("-" * 20)
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
