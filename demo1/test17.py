#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-20 10:24:08
# @Author  : TaoYuan (1876665310@qq.com)
# @Link    : http://blog.csdn.net/lftaoyuan  Python互助学习qq群：315857408
# @Version : 1


def trim(s):
    #  判断是否符合trim条件
    if len(s) == 0 or s[0] != ' ' and s[-1] != ' ':
        return s
    else:
        #  递归去空
        return trim(s[0] == ' ' and s[1:] or s[:-1])


# 测试:
if __name__ == '__main__':
    if trim('hello  ') != 'hello':
        print('测试失败!')
    elif trim('  hello') != 'hello':
        print('测试失败!')
    elif trim('  hello  ') != 'hello':
        print('测试失败!')
    elif trim('') != '':
        print('测试失败!')
    elif trim('    ') != '':
        print('测试失败!')
    else:
        print('测试成功!')
