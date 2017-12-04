#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/4 0004.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408
import inspect


class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return "<%s:%s>" % (self.__class__.__name__, self.name)


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, "bigint")


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, "varchar(20)")


class ModelMetaclass(type):
    def __new__(mcs, name, bases, attrs):
        if name == "Model":
            return type.__new__(mcs, name, bases, attrs)
        print("Found Model:%s" % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print("Found mappings:%s --> %s" % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 假设表名和类名一致
        return type.__new__(mcs, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):  # 属性校验
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):  # set
        self[key] = value

    def save(self):  # 保存
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))

        # 连接数据库驱动即可真正连接
        sql = "insert into %s (%s) values (%s)" % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

    def delete(self):  # 删
        # 连接数据库驱动即可真正连接
        sql = "delete from %s" % self.__table__
        print('SQL: %s' % sql)

    def update(self):  # 改
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))

        # 连接数据库驱动即可真正连接
        sql = "update %s set %s=%s" % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

    def find(self):  # 查
        # 连接数据库驱动即可真正连接
        sql = "select * from %s" % self.__table__
        print('SQL: %s' % sql)


class User(Model):
    # 定义类属性到数据库列的映射
    id = IntegerField("id")
    username = StringField("username")
    password = StringField("password")
    email = StringField("email")


if __name__ == '__main__':
    # 创建实例
    u = User(id=1, username="TaoYuan", password="123456", email="1876665310@qq.com")

    # 增删改查
    u.save()
    print('-' * 30)
    u.delete()
    print('-' * 30)
    u.update()
    print('-' * 30)
    u.find()
    print('-' * 15, "调用顺序如下", '-' * 15)
    print(inspect.getmro(User))
