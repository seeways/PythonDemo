#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/7 0007.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408
import os

fpath = os.path.abspath(os.path.join(os.getcwd(), "../work/test.txt"))

with open(fpath, 'r') as f:
    s = f.read()
    print(s)