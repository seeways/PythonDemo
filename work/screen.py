#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/1 0001.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408
# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：


class Screen(object):
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise ValueError("must be integer!")
        elif width < 0:
            raise ValueError("Error Value:", width)
        else:
            self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise ValueError("must be integer!")
        elif height < 0:
            raise ValueError("Error Value:", height)
        else:
            self.__height = height

    @property
    def resolution(self):
        return self.__height * self.__width


if __name__ == '__main__':
    # 测试:
    s = Screen()
    s.width = 1024
    s.height = 768
    print('resolution =', s.resolution)
    if s.resolution == 786432:
        print('测试通过!')
    else:
        print('测试失败!')
