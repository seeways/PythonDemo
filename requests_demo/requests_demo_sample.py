#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2018/2/2 0002. 
# @Link    : http://blog.csdn.net/lftaoyuan  
# Github   : https://github.com/seeways
import requests

with open("test.html", "wb") as code:
    code.write(requests.get("http://www.baidu.com/").content)
