import urllib
from urllib import request

"""
这个是写重复了

本目录的test04
commonlib: lib_urllib  # 原生
ex_lib: ex_lib_requests  # 框架
还有其他的
"""

url = 'http://wthrcdn.etouch.cn/weather_mini?city=深圳'
req = urllib.request.Request(url)
ret = urllib.request.urlopen(req)
data = ret.read()

data = data.decode("utf-8")
print(data, type(data))
