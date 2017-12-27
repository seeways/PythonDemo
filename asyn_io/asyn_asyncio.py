#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/26 0026.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408
"""
asyncio是Python 3.4版本引入的标准库，直接内置了对异步IO的支持。

asyncio的编程模型就是一个消息循环。
我们从asyncio模块中直接获取一个EventLoop的引用
然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO。

1. asyncio提供了完善的异步IO支持；

2. 异步操作需要在coroutine中通过yield from完成；

3. 多个coroutine可以封装成一组Task然后并发执行。
"""
import asyncio
import threading
from datetime import datetime

# @asyncio.coroutine
# def hello():
#     print("hello!")
#     # 异步调用asyncio.sleep(1)
#     r = yield from asyncio.sleep(1)
#     print("等待结束，返回：", r)


# # get EventLoop
# loop = asyncio.get_event_loop()
# # exec coroutine
# loop.run_until_complete(hello())
# loop.close()


"""
@asyncio.coroutine把一个generator标记为coroutine类型
然后，我们就把这个coroutine扔到EventLoop中执行

hello() 首先执行print("hello!")
然后，yield from语法可以让我们方便地调用另一个generator

由于asyncio.sleep()也是一个coroutine
所以线程不会等待asyncio.sleep()，而是直接中断并执行下一个消息循环
当asyncio.sleep()返回时，线程就可以从yield from拿到返回值(None)，然后继续执行下一行语句

把asyncio.sleep(1)看成是一个耗时1秒的IO操作
此时，主线程并未等待，而是去执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行。

"""


# 对上面的demo用两个coroutine进行改造实验
@asyncio.coroutine
def hello():
    print("hello {} {}".format(datetime.now(), threading.currentThread()))
    r = yield from asyncio.sleep(1)
    print("end {} {}".format(datetime.now(), threading.currentThread()))


# get EventLoop
# loop = asyncio.get_event_loop()
# # exec coroutine
# test_task = [hello(), hello()]
# loop.run_until_complete(asyncio.wait(test_task))
# loop.close()

"""
hello 2017-12-27 10:54:18.648749 <_MainThread(MainThread, started 9512)>
hello 2017-12-27 10:54:18.648749 <_MainThread(MainThread, started 9512)>
(暂停约1秒)
end 2017-12-27 10:54:19.648806 <_MainThread(MainThread, started 9512)>
end 2017-12-27 10:54:19.648806 <_MainThread(MainThread, started 9512)>

由打印的当前线程名称可以看出，两个coroutine是由同一个线程并发执行的。

如果把asyncio.sleep()换成真正的IO操作，则多个coroutine就可以由一个线程并发执行。
"""


# 我们用asyncio的异步网络连接来获取sina、sohu和163的网站首页
@asyncio.coroutine
def wget(host):
    print("wget {}".format(host))
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: {}\r\n\r\n'.format(host)
    writer.write(header.encode("utf-8"))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print("{} header:{}".format(host, line.decode("utf-8").rstrip()))
    # Ignore the body, close the socket
    writer.close()


loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

"""
可见3个连接由一个线程通过coroutine并发完成。

wget www.sina.com.cn
wget www.163.com
wget www.sohu.com
www.sina.com.cn header:HTTP/1.1 200 OK
www.sina.com.cn header:Server: nginx
www.sina.com.cn header:Date: Wed, 27 Dec 2017 03:36:07 GMT
www.sina.com.cn header:Content-Type: text/html
www.sina.com.cn header:Content-Length: 603812
www.sina.com.cn header:Connection: close
www.sina.com.cn header:Last-Modified: Wed, 27 Dec 2017 03:33:15 GMT
www.sina.com.cn header:Vary: Accept-Encoding
www.sina.com.cn header:Expires: Wed, 27 Dec 2017 03:37:03 GMT
www.sina.com.cn header:Cache-Control: max-age=60
www.sina.com.cn header:X-Powered-By: shci_v1.03
www.sina.com.cn header:Age: 3
www.sina.com.cn header:Via: http/1.1 ctc.ningbo.ha2ts4.97 (ApacheTrafficServer/6.2.1 [cHs f ]), http/1.1 ctc.xiamen.ha2ts4.41 (ApacheTrafficServer/6.2.1 [cHs f ])
www.sina.com.cn header:X-Via-Edge: 1514345767204779d11da3cd64cde2eeece4f
www.sina.com.cn header:X-Cache: HIT.41
www.sina.com.cn header:X-Via-CDN: f=edge,s=ctc.xiamen.ha2ts4.41.nb.sinaedge.com,c=218.17.157.119;f=Edge,s=ctc.xiamen.ha2ts4.41,c=222.76.214.41
www.163.com header:HTTP/1.0 302 Moved Temporarily
www.163.com header:Server: Cdn Cache Server V2.0
www.163.com header:Date: Wed, 27 Dec 2017 03:36:07 GMT
www.163.com header:Content-Length: 0
www.163.com header:Location: http://www.163.com/special/0077jt/error_isp.html
www.163.com header:Connection: close
www.sohu.com header:HTTP/1.1 200 OK
www.sohu.com header:Content-Type: text/html;charset=UTF-8
www.sohu.com header:Connection: close
www.sohu.com header:Server: nginx
www.sohu.com header:Date: Wed, 27 Dec 2017 03:35:10 GMT
www.sohu.com header:Cache-Control: max-age=60
www.sohu.com header:X-From-Sohu: X-SRC-Cached
www.sohu.com header:Content-Encoding: gzip
www.sohu.com header:FSS-Cache: HIT from 9730790.17464048.11067740
www.sohu.com header:FSS-Proxy: Powered by 3373701.4749967.4710554
"""