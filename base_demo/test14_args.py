#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-16 17:04:31
# @Author  : TaoYuan (1876665310@qq.com)
# @Link    : https://github.com/seeways or http://blog.csdn.net/lftaoyuan
# @Version : $Id$


def powers(x=0, n=2):  # 默认参数 必须指向不变对象
    return x ** n


def cola(*nums):  # 可变参数
    sum = 0
    for num in nums:
        sum += num
    return sum


def keywordargs(no, *name, **keyword):  # 关键词参数 如果有可变参数，遵守可变参数原则
    # 如果要默认关键词，需要用*作为分隔符 keywordargs(no, *name, *， city='深圳')
    return "no:", no, "name:", name, "other:", keyword


if __name__ == '__main__':
    print(powers(3, 5))
    print(cola(1, 2, 3))
    print(cola(1, 2, 3, 4))
    print(cola(1, 2, 3, 4, 5))
    print(keywordargs(23, "张三", "小张三", remark="张三小时候叫小张三", city="深圳", country="北京"))

    print(powers())
    print(cola())
    print(keywordargs(1))
