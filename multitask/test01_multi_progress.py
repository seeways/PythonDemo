#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/10.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408


import os, time, random
from multiprocessing import Process, Pool


# print("Process (%s) start..." % os.getpid())
# Only works on Unix/Linux/Mac:
# pid = os.fork()
# if pid == 0:
#     print("I am child Process (%s) and my parent is %s" % (os.getpid(), os.getpid()))
# else:
#     print("I (%s) just Created a child process (%s)" % (os.getpid(), pid))

def run_proc(name):
    print("Process child process %s (%s)..." % (name, os.getpid()))


def long_time_task(name):
    print("Run task %s (%s)..." % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print("Task %s runs %0.2f seconds." % (name, end - start))


if __name__ == '__main__':
    print("Parent process %s " % os.getpid())
    # # 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动
    # p = Process(target=run_proc, args=("test",))
    # print("child process will start.")
    # p.start()
    # p.join()  # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
    # print("child process end.")

    p1 = Pool(5)  # Pool()线程池数量，默认是cpu核心数
    for i in range(5):
        p1.apply_async(long_time_task, args=(i,))
    print("waiting for all subprocesses done...")
    p1.close()
    p1.join()
    print("all subprocesses done.")
