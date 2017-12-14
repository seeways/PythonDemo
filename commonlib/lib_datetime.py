#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/13 0013.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408
# datetime是Python处理日期和时间的标准库。
from datetime import datetime, timedelta, timezone

print("-" * 10, "get current time", "-" * 10)
current_time = datetime.now()  # 获取当前datetime
print(current_time)
print(type(current_time))
# 2017-12-13 09:28:48.800766
# <class 'datetime.datetime'>


print("\r\n")
print("-" * 10, "datetime to timestamp", "-" * 10)
# (self, year, month, day, hour, minute, second, microsecond,tzinfo: Optional[tzinfo] = ...)
st = datetime(2017, 12, 13, 12, 0, 0)  # 用指定日期时间创建datetime
print(st.timestamp())  # 把datetime 转换为timestamp
# 1513136723.0


print("\r\n")
print("-" * 10, "date format", "-" * 10)
print(datetime.fromtimestamp(1513136723))  # 本地时间
print(datetime.utcfromtimestamp(1513136723))  # UTC时间
print(datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S'))  # string to datetime
print(current_time.strftime("%Y-%m-%d %H:%M:%S"))  # datetime to string,like java

print("\r\n")
print("-" * 10, "计算时间(datetime加减)", "-" * 10)
print("now:", current_time)
print("one day off:", current_time + timedelta(1))
print("one days ago:", current_time - timedelta(days=1, hours=1))

print("\r\n")
print("-" * 10, "本地时间转换为UTC时间", "-" * 10)
tz_utc_8 = timezone(timedelta(hours=8))  # 创建东八区时区
print(current_time)
print(current_time.replace(tzinfo=tz_utc_8))  # 强制设置为UTC+8:00
# 2017-12-13 19:59:06.630822
# 2017-12-13 19:59:06.630822+08:00
