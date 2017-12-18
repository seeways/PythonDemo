#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/17.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408
# Python提供了HTMLParser来非常方便地解析HTML
from html.parser import HTMLParser  # 查找标记和其他标记和调用处理程序函数
from html.entities import name2codepoint  # 将HTML实体名称映射到Unicode代码点

"""
利用HTMLParser，可以把网页中的文本、图像等解析出来。


feed()方法可以多次调用，也就是不一定一次把整个HTML字符串都塞进去，可以一部分一部分塞进去。
特殊字符有两种，一种是英文表示的&nbsp;，一种是数字表示的&#1234;，这两种字符都可以通过Parser解析出来。
"""


class MyHTMLParse(HTMLParser):
    """docstring for MyHTMLParse"""

    def handle_starttag(self, tag, attrs):
        print("<{}>".format(tag))

    def handle_endtag(self, tag):
        print("<{}>".format(tag))

    def handle_startendtag(self, tag, attrs):
        print("<{}>".format(tag))

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print("<!--{}-->".format(data))

    def handle_entityref(self, name):
        print("&{};".format(name))

    def handle_charref(self, name):
        print("&#{};".format(name))


parser = MyHTMLParse()
parser.feed("""
	<html>
		<head></head>
		<body>
			<!-- test html parser -->
			<h1>
			Some
			 <a href="#">html</a>
			 html&nbsp;tutorial...<br>
			 end
			</h1>
		</body>
	</html>
	""")
