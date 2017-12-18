#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/18 0018.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408
# 利用urllib读取JSON，然后将JSON解析为Python对象
from urllib import request
import json


def fetch_data(url):
    with request.urlopen(url) as f:
        try:
            return json.loads(f.read().decode("utf-8"))
        except ValueError:
            print("ValueError:", url)


# 测试
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
data = fetch_data(URL)
print(data)
assert data['query']['results']['channel']['location']['city'] == 'Beijing'
print('ok')
