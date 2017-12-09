#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/8 0008.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408
import json

"""
ensure_ascii=True
{"name": "\u5c0f\u660e", "age": 20}

ensure_ascii=False
{"name": "小明", "age": 20}
"""
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)

print(s)
