#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-30 17:54:54
# @Author  : TaoYuan (1876665310@qq.com)
# @Link    : http://blog.csdn.net/lftaoyuan  Python互助学习qq群：315857408
# @Version : $Id$
# @des	   : 请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender.__str__() == 'male' or gender.__str__() == 'female':
            self.__gender = gender
        else:
            raise ValueError('不男不女')


if __name__ == '__main__':
    # 测试:
    bart = Student('Bart', 'male')
    if bart.get_gender() != 'male':
        print('测试失败!')
    else:
        bart.set_gender('female')
        if bart.get_gender() != 'female':
            print('测试失败!')
        else:
            try:
                bart.set_gender('人妖')
                print('测试失败!')
            except ValueError:
                print('测试成功!')
