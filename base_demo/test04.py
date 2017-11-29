import urllib.request

request = urllib.request.Request('http://www.baidu.com/')
response = urllib.request.urlopen(request)
if response.getcode() != 200:
    print("None!")
else:
    html = response.read()
    # 如果返回结果不为空
    if html is not None:
        # html = html.decode("utf-8")
        filename = 'C:\\Users\\Administrator\\Desktop\\test.html'
        file = open(filename, 'wb')
        file.write(html)
        file.close()
        # print(html)
    else:
        print("Maybe The Program is Error!")

# 头信息
print(response.info())
