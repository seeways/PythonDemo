#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/27 0027.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408
"""
Python从3.5版本开始为asyncio提供了async和await的新语法

用asyncio提供的@asyncio.coroutine可以把一个generator标记为coroutine类型
然后在coroutine内部用yield from调用另一个coroutine实现异步操作

为了简化并更好地标识异步IO，从Python 3.5开始引入了新的语法async和await，可以让coroutine的代码更简洁易读。

请注意，async和await是针对coroutine的新语法，要使用新的语法，只需要做两步简单的替换：
1. 把@asyncio.coroutine替换为async；
2. 把yield from替换为await。

注意新语法只能用在Python 3.5以及后续版本
之前版本则仍需使用asyncio案例的方案。
"""
import asyncio


# 之前代码
@asyncio.coroutine
def hello1():
    print("hello1!")
    # 异步调用asyncio.sleep(1)
    r = yield from asyncio.sleep(1)
    print("hello1等待结束，返回：", r)


# 新代码 更加简洁易懂了
async def hello2():
    print("hello2!")
    # 异步调用asyncio.sleep(1)
    r = await asyncio.sleep(1)
    print("hello2等待结束，返回：", r)


# get EventLoop
loop = asyncio.get_event_loop()
# exec coroutine
loop.run_until_complete(asyncio.wait([hello1(), hello2()]))
loop.close()

"""
返回结果仍然是一致的，使用也不受影响

hello1!
hello2!
hello1等待结束，返回： None
hello2等待结束，返回： None
"""
