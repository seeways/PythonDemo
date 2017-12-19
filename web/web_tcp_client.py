#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/19 0019.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408
import socket

# 用ipv4创建一个面向流的socket对象，下面为参数及默认值
# self, family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0, None)
# 建立连接   address = (host, port)
s.connect(('www.sina.com.cn', 80))
# 发送数据:
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# 接收数据:
buffer = []
while True:
    # 从socket接收缓冲区字节大小：1k
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
# 关闭连接:
s.close()
# 接收到的数据包括HTTP头和网页本身
# 我们只需要把HTTP头和网页分离一下，把HTTP头打印出来，网页内容保存到文件
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('my_res/sina.html', 'wb') as f:
    f.write(html)

"""
HTTP/1.1 200 OK
Server: nginx
Date: Tue, 19 Dec 2017 10:18:31 GMT
Content-Type: text/html
Content-Length: 604543
Connection: close
Last-Modified: Tue, 19 Dec 2017 10:18:17 GMT
Vary: Accept-Encoding
Expires: Tue, 19 Dec 2017 10:19:29 GMT
Cache-Control: max-age=60
X-Powered-By: shci_v1.03
Age: 2
Via: http/1.1 ctc.ningbo.ha2ts4.97 (ApacheTrafficServer/6.2.1 [cHs f ]), http/1.1 ctc.xiamen.ha2ts4.41 (ApacheTrafficServer/6.2.1 [cHs f ])
X-Via-Edge: 1513678711708779d11da3cd64cde57ebfc32
X-Cache: HIT.41
X-Via-CDN: f=edge,s=ctc.xiamen.ha2ts4.42.nb.sinaedge.com,c=218.17.157.119;f=Edge,s=ctc.xiamen.ha2ts4.41,c=222.76.214.42
"""