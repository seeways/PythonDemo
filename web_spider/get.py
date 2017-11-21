#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/11/21 0021
# @Author  : TaoYuan (1876665310@qq.com)
# @Link    : http://blog.csdn.net/lftaoyuan  Python互助学习qq群：315857408
# @Version : V1.0.0

import urllib.request

request = urllib.request.Request('http://www.baidu.com/')
response = urllib.request.urlopen(request)
if response.getcode() != 200:
    print("None!")
else:
    html = response.read()
    # 如果返回结果不为空
    if html is not None:
        # html = html.decode("utf-8")
        filename = 'C:\\Users\\Administrator\\Desktop\\test.html'
        file = open(filename, 'wb')
        file.write(html)
        file.close()
        # print(html)
    else:
        print("Maybe The Program is Error!")

# 头信息
print(response.info())
