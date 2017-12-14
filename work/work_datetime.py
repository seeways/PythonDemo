#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/13 0013.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408
# 假设你获取了用户输入的日期和时间如2015-1-21 9:01:30,以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp
# 这个作业的实质其实还是在提取时区
import re
from datetime import datetime, timezone, timedelta


def to_timestamp(dt_str, tz_str):
    # uct = tz_str[3:].replace(':', '')
    # if len(uct) < 5:
    #     uct = uct[:1] + '0' + uct[1:]
    # dt = datetime.strptime(dt_str + uct, '%Y-%m-%d %H:%M:%S%z')
    # return dt.timestamp()

    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    N = int(re.match(r'^UTC([0-9\+-]+):[0-9]+$', tz_str).group(1))
    tz_utc_N = timezone(timedelta(hours=N))
    dt = dt.replace(tzinfo=tz_utc_N)
    return dt.timestamp()





# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1
t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2
print('ok')
