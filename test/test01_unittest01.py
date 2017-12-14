#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/5 0005.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender.__str__() != 'male' and gender.__str__() != 'female':
            raise ValueError('wrong')
        else:
            self.__gender = gender


# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败1!')
else:
    bart.set_gender('enen')
    if bart.get_gender() != 'female':
        print('测试失败2!')
    else:
        print('测试成功!')
