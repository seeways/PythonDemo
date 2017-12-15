#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/15 0015.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408
import hmac

message = b"hello"
key = b"secret"
h = hmac.new(key, message, digestmod="MD5")
print(h.hexdigest())  # bade63863c61ed0b3165806ecd6acefc
