#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/11/21 0021
# @Author  : TaoYuan (1876665310@qq.com)
# @Link    : http://blog.csdn.net/lftaoyuan  Python互助学习qq群：315857408
# @Version : V1.0.0

import urllib.request
from test05_custom_class import Chain


# 动态拼接url
url = "{}{}".format('http://127.0.0.1:5000', Chain().get.taoyuan)

request = urllib.request.Request(url)
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
        print("--------页面信息----------")
        print(html)

    else:
        print("Maybe The Program is Error!")

# 头信息
print("--------头信息----------")
print(response.info())
