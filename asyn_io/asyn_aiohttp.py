#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/27 0027.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408
"""
asyncio可以实现单线程并发IO操作。

如果仅用在客户端，发挥的威力不大。
如果把asyncio用在服务器端，由于HTTP连接就是IO操作，因此可以用单线程+coroutine实现多用户的高并发支持。

asyncio实现了TCP、UDP、SSL等协议，
aiohttp则是基于asyncio实现的HTTP框架。

"""

# 编写一个web服务器用来处理url
# 1. / 首页返回 b'<h1>Index</h1>'
# 2. /hello/{name} - 根据URL参数返回文本hello, %s!
import asyncio
from aiohttp import web


async def index(request):
    await asyncio.sleep(1)
    return web.Response(body=b'<h1>Index</h1>', content_type='text/html')


async def hello(request):
    await asyncio.sleep(1)
    text = '<h1>hello, %s!</h1>' % request.match_info["name"]
    return web.Response(body=text.encode("utf-8"), content_type='text/html')


async def init(loop):
    my_app = web.Application(loop=loop)
    my_app.router.add_route("GET", "/", index)
    my_app.router.add_route("GET", "/hello/{name}", hello)
    srv = await loop.create_server(my_app.make_handler(), "", 80)
    print("Server started...")
    return srv


# aiohttp的初始化函数init()也是一个coroutine，loop.create_server()则利用asyncio创建TCP服务。
loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

"""
web.Response(self, *, body=None, status=200,reason=None, text=None, headers=None, content_type=None, charset=None)
廖老师的不标记内容类型的话，默认是下载，可以加上content_type='text/html'

http://127.0.0.1/
<h1>Index</h1>

http://127.0.0.1/hello
404: Not Found

http://127.0.0.1/hello/TaoYuan
<h1>hello, TaoYuan!</h1>
"""



