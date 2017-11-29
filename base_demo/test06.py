import urllib
from urllib import request

url = 'http://wthrcdn.etouch.cn/weather_mini?city=深圳'
request = urllib.request.Request(url)
ret = urllib.request.urlopen(request)
data = ret.read()

data = data.decode("utf-8")
print(data, type(data))
