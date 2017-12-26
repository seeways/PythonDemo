#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/26 0026.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408
"""
写一个app.py，处理3个URL，分别是：

GET /：首页，返回Home；

GET /signin：登录页，显示登录表单；

POST /signin：处理登录表单，显示登录结果。

注意噢，同一个URL/signin分别有GET和POST两种请求，映射到两个处理函数中。

"""
from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    return "<h1>HOME</h1>"


@app.route("/sign_in", methods=["GET"])
def sign_in_form():
    return"""
    <form action="/sign_in" method="post">
	<p>用户名：<input name="username"></p>
	<p>密  码：<input name="password" type="password"></p>
	<p><button type="submit">Sign In</button></p>
	</form>"""


@app.route("/sign_in", methods=["POST"])
def sign_in():
    username = request.form["username"]
    password = request.form["password"]
    if username == "admin" and password == "123456":
        return "<h3>Hi! {}, Welcome To Here!</h3>".format(username)
    return "<h3>Bad username or password!</h3>"


if __name__ == '__main__':
    app.run()
