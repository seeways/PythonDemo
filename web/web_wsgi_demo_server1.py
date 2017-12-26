#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/26 0026. 
# @Link    : http://blog.csdn.net/lftaoyuan  
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408
"""
server
负责启动WSGI服务器，加载application
"""
from wsgiref.simple_server import make_server
from web_wsgi_demo1 import application


# 创建一个服务器，IP为空，端口8000，处理函数为application
httpd = make_server("", 8000, application)
print("serving http on prot 8000...")
#  监听http请求
httpd.serve_forever()
