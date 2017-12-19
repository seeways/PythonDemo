#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/19 0019.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408

"""
我们已经讲解了Python内置的urllib模块，用于访问网络资源。
但是，它用起来比较麻烦，而且，缺少很多实用的高级功能。

更好的方案是使用requests。它是一个Python第三方库，处理URL资源特别方便。

1. 获得bytes对象: r.content
2. 检测编码: r.encoding
3. 获取json:  r.json()
4. 传入header(dict): r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
5. post + data请求: r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})
6. requests默认使用application/x-www-form-urlencoded对POST数据编码
7. json post: r =  requests.post(url, json=params) # 内部自动序列化为JSON
8. file post: 在读取文件时，注意务必使用'rb'即二进制模式读取，这样获取的bytes长度才是文件的长度
upload_files = {'file': open('report.xls', 'rb')}
r = requests.post(url, files=upload_files)

9. 获取响应头: r.headers  头信息: r.headers['Content-Type']
10. 获取cookie：  r.cookies['ts']
11. 传入cookie： r = requests.get(url, cookies={'token': '12345', 'status': 'working'))
12. 超时参数： r = requests.get(url, timeout=2.5) # 单位: s
"""
import requests

# get
r = requests.get('https://www.python.org')
print(r.status_code)
print(b'Python is a programming language' in r.content)

print("--------------get args-------------")
r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
print(r.url)

print("-------------post------------")
payload = dict(key1='value1', key2='value2')
r = requests.post('http://httpbin.org/post', data=payload)
print(r.text)
