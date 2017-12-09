#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/8 0008.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408

import json

"""
standard json
"""

# create json
# d = dict(name="Bob", age=20, score=88)
# print(json.dumps(d))  # {"name": "Bob", "age": 20, "score": 88}

# load json
# json_str = '{"name": "Bob", "age": 20, "score": 88}'
# print(json.loads(json_str))  # {'name': 'Bob', 'age': 20, 'score': 88}


"""
advanced usage
"""


class Student(object):
    """docstring for Student"""

    def __init__(self, name, age, score):
        super(Student, self).__init__()
        self.name = name
        self.age = age
        self.score = score


def cls2dict(in_cls):
    return {
        "name": in_cls.name,
        "age": in_cls.age,
        "score": in_cls.score
    }


def dict2cls(in_dict):
    return Student(in_dict["name"], in_dict["age"], in_dict["score"])


# s = Student("Bob", 20, 88)
# print(json.dumps(s, default=cls2dict))  # {"name": "Bob", "age": 20, "score": 88}
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2cls))  # <__main__.Student object at 0x00000000028F46D8>


