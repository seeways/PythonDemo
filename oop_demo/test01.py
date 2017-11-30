#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/11/29 0029
# @Author  : TaoYuan (1876665310@qq.com)
# @Link    : http://blog.csdn.net/lftaoyuan  Python互助学习qq群：315857408
# @Version : V1.0.0
# 简介，类和实例


# 面向对象的程序设计思想
# 我们首选思考的不是程序的执行流程，而是Student这种数据类型应该被视为一个对象
# 这个对象拥有name和score这两个属性（Property）。
# 如果要打印一个学生的成绩，
# 首先必须创建出这个学生对应的对象，
# 然后给对象发一个print_score消息
# 让对象自己把自己的数据打印出来。
class Student(object):
    """docstring for Student"""

    def __init__(self, name, score, *remark):
        self.name = name
        self.score = score
        self.remark = remark

    def print_score(self):
        print("{0} {1} {2}".format(self.name, self.score, self.remark))

    def is_pass(self):
        if 0 < self.score < 60:
            return "不及格"
        elif 60 <= self.score < 90:
            return "及格"
        elif 90 <= self.score <= 100:
            return "优等生"
        else:
            return "成绩作废！归零"


# 面向过程
# 假设我们要处理学生的成绩表，为了表示一个学生的成绩，面向过程的程序可以用一个dict表示：
std1 = {'name': 'Michael', 'score': 98}
std2 = {'name': 'Bob', 'score': 81}


# 而处理学生成绩可以通过函数实现，比如打印学生的成绩：
def print_score(std):
    print('%s: %s' % (std['name'], std['score']))


if __name__ == '__main__':
    print('----------------')
    Student("zhangsan", 59, "命不好").print_score()
    Student("lisi", 99, "屌爆了").print_score()
    print('----------------')
    print_score(std1)
    print_score(std2)
    print('----------------')

    # 变量stu指向的就是一个Student的实例
    stu = Student("wangwu", 61, "运气好")
    # 创建实例的时候已经有值了，所以可以直接打印出来
    print(stu.name)

    # 可以对name属性重新赋值
    stu.name = "zhaoliu"
    print(stu.name)

    # 也可以自定义一个新属性
    stu.address = "深圳"
    print(stu.address)
    print('----------------')
    lilei = Student('李雷', 99)
    hanmeimei = Student('韩梅梅', 59)
    print(lilei.name, lilei.is_pass())
    print(hanmeimei.name, hanmeimei.is_pass())
