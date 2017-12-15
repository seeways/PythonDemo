#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/15 0015.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408
# 根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5
import hashlib
import random


def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


class User(object):
    def __init__(self, username, password):
        self.username = username
        self.password = get_md5(password + create_salt(username))


def create_salt(username):
    salt = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    len_chars = len(chars) - 1
    for i in range(5):
        # 每次从chars中随机取一位
        salt += chars[random.randint(0, len_chars)]
    if username not in db:
        salt_db[username] = salt
    return salt




db = {}
salt_db = {}


def regist(username, password):
    if username in db:
        print("username existed！")
    else:
        db[username] = User(username, password)


def login(username, password):
    user = db[username]
    return get_md5(password + salt_db[username]) == user.password


if __name__ == '__main__':
    # register
    regist('michael', '123456')
    regist('bob', 'abc999')
    regist('alice', 'alice2008')
    # login:
    assert login('michael', '123456')
    assert login('bob', 'abc999')
    assert login('alice', 'alice2008')
    assert not login('michael', '1234567')
    assert not login('bob', '123456')
    assert not login('alice', 'Alice2008')
    print('ok')
