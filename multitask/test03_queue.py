#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/11 0011.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408


from multiprocessing import Process, Queue
import os, time, random


# 写数据进程执行的代码
def write(q):
    print("process to write: %s" % os.getpid())
    for value in ["A", "B", "C"]:
        print("Put %s to queue..." % value)
        q.put(value)
        time.sleep(random.random())


# 读数据进程执行的代码：
def read(q):
    print("process to read: %s" % os.getpid())
    while True:
        value = q.get(True)
        print("Get %s from queue." % value)


if __name__ == '__main__':
    # 父进程创建Queue，并传给各子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
