#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/26 0026.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408
"""
协程

优势
1. 最大的优势就是协程极高的执行效率。因为不用切换线程
2. 不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突
在协程中控制共享资源不加锁，只需要判断状态就好了，所以执行效率比多线程高很多。

Python对协程的支持是通过generator实现的：
在generator中，我们不但可以通过for循环来迭代
还可以不断调用next()函数获取由yield语句返回的下一个值。
但是Python的yield不但可以返回一个值，它还可以接收调用者发出的参数。

执行顺序如下：
come produce
come consumer
# 以上只执行一次，然后进入循环收发
[生产者] 生产了1
[消费者] 消费了1
[生产者] 消费者返回了OK


consumer函数是一个generator，把一个consumer传入produce后：

1. 调用c.send(None)启动生成器
2. 一旦生产了东西，通过c.send(n)切换到consumer执行
3. consumer通过yield拿到消息，处理，又通过yield把结果传回
4. produce拿到consumer处理的结果，继续生产下一条消息
5. produce决定不生产了，通过c.close()关闭consumer，整个过程结束
整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。

"""


def consumer():
    r = ""
    print("come consumer")
    while True:
        n = yield r
        if not n:
            return
        print("[消费者] 消费了{}".format(n))
        r = "OK"


def produce(csm):
    print("come produce")
    csm.send(None)
    n = 0
    while n < 5:
        n += 1
        print("[生产者] 生产了{}".format(n))
        r = csm.send(n)
        print("[生产者] 消费者返回了{}".format(r))
    csm.close()


if __name__ == '__main__':
    c = consumer()
    produce(c)

