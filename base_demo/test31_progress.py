#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/10.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408


import os

print("Process (%s) start..." % os.getpid())
# Only works on Unix/Linux/Mac:
pid = os.fork()
if pid == 0:
    print("I am child Process (%s) and my parent is %s" % (os.getpid(), os.getpid()))
else:
    print("I (%s) just Created a child process (%s)" % (os.getpid(), pid))
