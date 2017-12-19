#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/19 0019.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408
"""
psutil是一个用于检索信息的跨平台库
运行进程和系统利用率(CPU、内存、磁盘、网络，在Python中传感器)。

支持平台:
 - Linux
 - Windows
 - OSX
 - FreeBSD
 - OpenBSD
 - NetBSD
 - Sun Solaris
 - AIX
"""
import psutil

print("-----------cpu_count-----------")
print(psutil.cpu_count())  # 返回系统中逻辑cpu的数量
print("-----------cpu_freq-----------")
print(psutil.cpu_freq())  # 返回CPU频率
print("-----------cpu_percent-----------")
print(psutil.cpu_percent())  # 返回当前系统CPU利用率(float类型)
print("-----------cpu_stats-----------")
print(psutil.cpu_stats())  # 返回CPU统计数据
print("-----------cpu_times-----------")
print(psutil.cpu_times())  # 返回系统范围内的CPU时间。
print("-----------cpu_times_percent-----------")
print(psutil.cpu_times_percent())  # 对于每个特定的CPU时间提供利用率，由cpu_times()返回。
print("-----------boot_time-----------")
print(psutil.boot_time())  # 返回从1970以来以秒表示的系统启动时间
print("-----------users-----------")
print(psutil.users())  # 返回当前连接在系统上的用户列表
print("-----------test-----------")
print(psutil.test())  # 列出所有当前正在运行的进程信息

"""
-----------cpu_count-----------
4
-----------cpu_freq-----------
scpufreq(current=3168.0, min=0.0, max=3201.0)
-----------cpu_percent-----------
0.0
-----------cpu_stats-----------
scpustats(ctx_switches=861048211, interrupts=148032987, soft_interrupts=0, syscalls=1186688671)
-----------cpu_times-----------
scputimes(user=6015.96044921875, system=2641.171875, idle=79255.78125, interrupt=93.52259969711304, dpc=523.3521823883057)
-----------cpu_times_percent-----------
scputimes(user=0.0, system=0.0, idle=0.0, interrupt=0.0, dpc=0.0)
-----------boot_time-----------
1513644441.0
-----------users-----------
[suser(name='TaoYuan', terminal=None, host='0.0.0.0', started=1513644451.0, pid=None)]
-----------test-----------
USER         PID %MEM     VSZ     RSS TTY           START    TIME  COMMAND
SYSTEM         0    ?       ?      24 ?             08:47   00:55  System Idle Process
SYSTEM         4    ?     120     368 ?             08:47   05:13  System
             320    ?     544    1216 ?             08:47   00:00  smss.exe
             332  0.2   14004   20068 ?             08:47   00:17  svchost.exe
             496  0.3   21472   37028 ?             08:47   00:30  svchost.exe
             500    ?    2392    5416 ?             08:47   00:00  csrss.exe
             516  0.2    9904   19112 ?             08:47   00:00  svchost.exe
             656    ?    1824    5384 ?             08:47   00:00  wininit.exe
             664  0.7    4196   90228 ?             08:47   00:54  csrss.exe
             712  0.1    3476    8488 ?             08:47   00:00  winlogon.exe
             756  0.1    6044   10336 ?             08:47   00:07  services.exe
             768  0.1    5900   13452 ?             08:47   00:23  lsass.exe
             776    ?    2976    4968 ?             08:47   00:01  lsm.exe
             876  0.1    4364   10164 ?             08:47   00:03  svchost.exe
             952  0.1    5412    9540 ?             08:47   00:08  svchost.exe
            1060  0.1    3424    8216 ?             08:47   00:00  svchost.exe
            1092  0.1    5616   11364 ?             08:47   00:00  svchost.exe
            1184  0.4   44764   54276 ?             08:47   00:09  ZhuDongFangYu.exe
TaoYuan     1224  0.3   29080   34416 ?             09:11   00:00  chrome.exe
            1272  0.2   17796   19908 ?             08:47   00:06  svchost.exe
TaoYuan     1320  0.7   10948   82148 ?             08:47   00:00  taskeng.exe
TaoYuan     1416  0.1    8192   16160 ?             09:11   00:00  conhost.exe
            1452  0.1    6332   12352 ?             08:47   00:00  spoolsv.exe
...
"""

print("-----------Process-----------")
print(psutil.Process(3776))  # 获取指定进程ID=3776，其实就是当前Python交互环境
print("-----------pids-----------")
print(psutil.pids())  # 所有进程id
print("-----------pid_exists-----------")
print(psutil.pid_exists())  # 当前pid是否在列表中
print("-----------Process Other-----------")
# Process是一个类，其他信息运维可以看看，我就不看了