#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/4 0004.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408

try:
    print("try...")
    r = 10 / int('5')
    print("result:", r)

except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)
except ValueError as e:
    print("ValueError:", e)
except BaseException as e:
    print("Error:", e)
else:
    print("No Error!")
finally:
    print("finally...")

