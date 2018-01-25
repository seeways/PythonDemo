#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-17 16:58:55
# @Author  : TaoYuan (1876665310@qq.com)
# @Link    : https://github.com/seeways or http://blog.csdn.net/lftaoyuan
# @Version : 1
"""
汉诺塔算法
"""

# 第一个塔为初始塔，中间的塔为借用塔，最后一个塔为目标塔
i = 0  # 记录步数


def move(no, come, to):  # 将编号为no的盘子由come移动到to
    global i
    i += 1
    print("第", i, " 步:将 ", no, " 号盘子 ", come, "---->", to)


def hanoi(no, come, denpend_on, to):  # 将no个盘子由初始塔移动到目标塔(利用借用塔)
    if no == 1:
        move(1, come, to)  # 只有一个盘子是直接将初塔上的盘子移动到目的地
    else:
        hanoi(no - 1, come, to, denpend_on)  # 先将初始塔的前no - 1个盘子借助目的塔移动到借用塔上
        move(no, come, to)  # 将剩下的一个盘子移动到目的塔上
        hanoi(no - 1, denpend_on, come, to)  # 最后将借用塔上的no - 1个盘子移动到目的塔上


if __name__ == '__main__':
    print("请输入盘子的个数:")
    no = input()
    print(no)
    print("盘子移动情况如下:\n")
    hanoi(int(no), 'A塔', 'B塔', 'C塔')
