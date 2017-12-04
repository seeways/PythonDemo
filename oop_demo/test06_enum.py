#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/2 0002.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408
# 把Student的gender属性改造为枚举类型，可以避免使用字符串
from enum import Enum, unique


@unique
class Gender(Enum):
    Male = 0
    Female = 1


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


# 测试:
lilei = Student('lilei', Gender.Male)
hanmeimei = Student("hanmeimei", Gender.Female)
if lilei.gender == Gender.Male and hanmeimei.gender == Gender.Female:
    print('测试通过!')
else:
    print('测试失败!')
