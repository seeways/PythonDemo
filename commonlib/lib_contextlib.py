#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/17.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408

# try:
# 	f = open("../2.txt")
# 	f.read()
# except Exception as e:
# 	raise FileNotFoundError("file not fpund!")
# finally:
# 	if f:
# 		f.close()

# with open("../2.txt", "r") as f:
#     f.read()


# 并不是只有open()函数返回的fp对象才能使用with语句。
# 任何对象，只要正确实现了上下文管理，就可以用于with语句。
# 实现上下文管理是通过__enter__和__exit__这两个方法实现的。
# class Query(object):
#     """docstring for Query"""

#     def __init__(self, name):
#         self.name = name

#     def __enter__(self):
#         print("begin..")
#         return self

#     def __exit__(self, exc_type, exc_value, traceback):
#     	if exc_type:
#     		print("Error")
#     	else:
#     		print("End")
#     def query(self):
#     	print("Query info about %s..." % self.name)

# with Query("Bob") as q:
# 	q.query()

# 编写__enter__和__exit__仍然很繁琐，因此Python的标准库contextlib提供了更简单的写法，上面的代码可以改写如下
from contextlib import contextmanager


# class Query(object):
# 	"""docstring for Query"""
# 	def __init__(self, name):
# 		self.name = name

# 	def query(self):
# 		print("Query info about %s..." % self.name)


# @contextmanager
# def create_query(name):
# 	print("begin...")
# 	q = Query(name)
# 	yield q
# 	print("end")

# # @contextmanager这个decorator接受一个generator，用yield语句把with ... as var把变量输出出去
# # 然后，with语句就可以正常地工作了
# with create_query("Bob") as q:
# 	q.query()


# 很多时候，我们希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现。
@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("<%s>" % name)


with tag("h1"):
    print("hello")
    print("world!")

# 代码的执行顺序是：

# 1. with语句首先执行yield之前的语句，因此打印出<h1>；
# 2. yield调用会执行with语句内部的所有语句，因此打印出hello和world；
# 3. 最后执行yield之后的语句，打印出</h1>。

# closing
from contextlib import contextmanager, closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)


# closing也是一个经过@contextmanager装饰的generator，这个generator编写起来其实非常简单
@contextmanager
def my_closing(thing):
    try:
        yield thing
    finally:
        thing.close()

# 它的作用就是把任意对象变为上下文对象，并支持with语句。
# @contextlib还有一些其他decorator，便于我们编写更简洁的代码。
