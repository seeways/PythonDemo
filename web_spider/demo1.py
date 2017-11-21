#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/11/21 0021
# @Author  : TaoYuan (1876665310@qq.com)
# @Link    : http://blog.csdn.net/lftaoyuan  Python互助学习qq群：315857408
# @Version : V1.0.0

import urllib.request

keywd = '矮大紧'
url = 'http://www.baidu.com/s?wd='
keywd_code = urllib.request.quote(keywd)
url_all = url + keywd_code
request = urllib.request.Request(url_all)
data = urllib.request.urlopen(request).read()
filename = 'C:\\Users\\Administrator\\Desktop\\5.html'
file = open(filename, 'wb')  # 打开文件
file.write(data)  # 写入文件
file.close()  # 关闭文件
