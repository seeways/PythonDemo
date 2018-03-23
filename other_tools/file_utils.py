#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2018/1/25 0025. 
# @Link    : http://blog.csdn.net/lftaoyuan  
# Github   : https://github.com/seeways
import os
import time

"""
文件工具类
"""

# 把时间戳转化为时间: 1479264792 to 2016-11-16 10:53:12
def time_stamp_to_time(timestamp):
    time_struct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', time_struct)


# 获取文件的大小,结果保留两位小数，单位为MB
def get_file_size(file_path):
    file_path = file_path.encode("utf-8")
    file_size = os.path.getsize(file_path)
    file_size = file_size / float(1024 * 1024)
    return round(file_size, 2)


# 获取文件的访问时间
def get_file_access_time(file_path):
    file_path = file_path.encode("utf-8")
    t = os.path.getatime(file_path)
    return time_stamp_to_time(t)


# 获取文件的创建时间
def get_file_create_time(file_path):
    file_path = file_path.encode("utf-8")
    t = os.path.getctime(file_path)
    return time_stamp_to_time(t)


# 获取文件的修改时间
def get_file_modify_time(file_path):
    file_path = file_path.encode("utf-8")
    t = os.path.getmtime(file_path)
    return time_stamp_to_time(t)
