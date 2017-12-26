#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/26 0026.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408
"""
http://flask.pocoo.org/

sample flask demo

app.run()
http://127.0.0.1:5000/

app.run("", 8000)
http://localhost:8000/
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


# host=None, port=None, debug=None, **options
app.run()
