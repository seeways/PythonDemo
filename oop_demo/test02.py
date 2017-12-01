#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-30 11:26:38
# @Author  : TaoYuan (1876665310@qq.com)
# @Link    : http://blog.csdn.net/lftaoyuan  Python互助学习qq群：315857408
# @Version : $Id$
# 继承和多态


class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def dog_run(self):
        print('Dog is running...')


# 子类可以继承父类的所有功能
dog = Dog()
dog.run()
dog.dog_run()

print('-' * 30)

a = list()
b = Animal()
c = Dog()

print(isinstance(a, list))
print(isinstance(b, Animal))
print(isinstance(c, Dog))
# 上述没错，但是c同时也可以是Animal
print(isinstance(c, Animal))

# 获取该对象所有的属性和方法
print(dir(Dog()))


