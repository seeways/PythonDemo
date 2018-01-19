#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2018/01/19 0019.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
import random
from urllib import request

__author__ = "TaoYuan"


headers = {
    'referer': 'http://blog.csdn.net/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 '
                  'Safari/537.36 '
}


def request_url(times, urls, headers):
    url = urls[random.randint(0, len(urls) - 1)]
    req = request.Request(url, headers=headers)
    request.urlopen(req)
    print("访问:{}次,本次访问:{}".format(times, url))


i = 0
while True:
    i += 1
    urls = [
        "http://blog.csdn.net/lftaoyuan/article/details/79085052",
        "http://blog.csdn.net/lftaoyuan/article/details/78563249",
        "http://blog.csdn.net/lftaoyuan/article/details/78549161",
        "http://blog.csdn.net/lftaoyuan/article/details/62234971",
    ]
    request_url(i, urls, headers)