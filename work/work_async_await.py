#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/27 0027.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408
# 用asyncio的异步网络连接来获取sina、sohu和163的网站首页
# 异步获取sina、sohu和163的网站首页源码用新语法重写并运行。
import asyncio


async def wget(host):
    print("wget {}".format(host))
    connect = asyncio.open_connection(host, 80)
    reader, writer = await connect
    header = 'GET / HTTP/1.0\r\nHost: {}\r\n\r\n'.format(host)
    writer.write(header.encode("utf-8"))
    await writer.drain()
    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break
        print("{} header:{}".format(host, line.decode("utf-8").rstrip()))
    # Ignore the body, close the socket
    writer.close()


loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()