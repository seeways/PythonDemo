#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/11/21 0021
# @Author  : TaoYuan (1876665310@qq.com)
# @Link    : http://blog.csdn.net/lftaoyuan  Python互助学习qq群：315857408
# @Version : V1.0.0
# @des     : 杨辉三角

# def triangles():  # 列表生成式
#     L = [1]
#     while True:
#         yield L
#         L.append(0)
#         L = [L[i - 1] + L[i] for i in range(len(L))]


def triangles():  # for 循环
    ret = [1]
    while True:
        yield ret
        for i in range(1, len(ret)):
            ret[i] = pre[i] + pre[i - 1]
        ret.append(1)
        pre = ret[:]


# def triangles(num=10):  # 不用生成器
#     LL = [[1]]
#     for i in range(1, num):
#         LL.append(
#             [(0 if j == 0 else LL[i - 1][j - 1]) + (0 if j == len(LL[i - 1]) else LL[i - 1][j]) for j in range(i + 1)])
#     return LL


if __name__ == '__main__':
    n = 0
    results = []
    for t in triangles():
        print(t)
        results.append(t)
        n = n + 1
        if n == 10:
            break
    if results == [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
        [1, 5, 10, 10, 5, 1],
        [1, 6, 15, 20, 15, 6, 1],
        [1, 7, 21, 35, 35, 21, 7, 1],
        [1, 8, 28, 56, 70, 56, 28, 8, 1],
        [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
    ]:
        print('测试通过!')
    else:
        print('测试失败!')
