#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/26 0026.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408
"""
Web服务器网关接口
WSGI：Web Server Gateway Interface

Web应用的本质就是:

1. 浏览器发送一个HTTP请求；
2. 服务器收到请求，生成一个HTML文档；
3. 服务器把HTML文档作为HTTP响应的Body发送给浏览器；
4. 浏览器收到HTTP响应，从HTTP Body取出HTML文档并显示。

WSGI接口定义非常简单，它只要求Web开发者实现一个函数，就可以响应HTTP请求
"""


# 上面的application()函数就是符合WSGI标准的一个HTTP处理函数，它接收两个参数：

# environ：一个包含所有HTTP请求信息的dict对象；
# start_response：一个发送HTTP响应的函数。
def application(environ, start_response):
    start_response("200 OK", [("Content-Type", "text/html")])  # 发送响应的header，并且只发送一次
    # 从environ里读取PATH_INFO，这样可以显示更加动态的内容
    body = "<h1>Hello {}, Welcome come here!</h1>".format(environ["PATH_INFO"][1:] or "web")
    return [body.encode("utf-8")]  # 请求体Body

# 有了WSGI，我们关心的就是如何从environ这个dict对象拿到HTTP请求信息，然后构造HTML，通过start_response()发送Header，最后返回Body。
# 整个application()函数本身没有涉及到任何解析HTTP的部分，也就是说，底层代码不需要我们自己编写，我们只负责在更高层次上考虑如何响应请求就可以了
# 但是， application()函数必须由WSGI服务器来调用

# Python内置了一个简单的WSGI服务器，叫wsgiref

"""
小结

无论多么复杂的Web应用程序，入口都是一个WSGI处理函数。
HTTP请求的所有输入信息都可以通过environ获得
HTTP响应的输出都可以通过start_response()加上函数返回值作为Body。

复杂的Web应用程序，光靠一个WSGI函数来处理还是太底层了
我们需要在WSGI之上再抽象出Web框架，进一步简化Web开发。
"""