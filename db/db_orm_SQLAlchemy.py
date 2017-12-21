#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/21 0021.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408

"""
python: [('0', 'TaoYuan0'), ('1', 'TaoYuan1'), ('2', 'TaoYuan2')]
sqlalchemy:
[
    User('1', 'Michael'),
    User('2', 'Bob'),
    User('3', 'Adam')
]

'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
"""
# 导入:
from sqlalchemy import Column, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()


# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user1'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # 一对多:
    books = relationship('Book')


class Book(Base):
    __tablename__ = 'book'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # “多”的一方的book表是通过外键关联到user表的:
    user_id = Column(String(20), ForeignKey('user.id'))


# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/test')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


# 以上代码完成SQLAlchemy的初始化和具体每个表的class定义。
# 如果有多个表，就继续定义其他class，例如School
# class School(Base):
#     __tablename__ = 'school'
#     id = Column(String(20), primary_key=True)
#     name = Column(String(20))


# 向数据库表中添加一行记录，可以视为添加一个User对象
# 创建session对象:
session = DBSession()
# 创建新User对象:
new_user = User(id='5', name='Bob')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()
# 关键是获取session，然后把对象添加到session，最后提交并关闭
# DBSession对象可视为当前数据库连接


# 查询数据
# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='5').one()
# 打印类型和对象的name属性:
print('type:', type(user))
print('name:', user.name)
# 关闭Session:
session.close()

"""
结果：
type: <class '__main__.User'>
name: Bob

ORM就是把数据库表的行与相应的对象建立关联，互相转换

由于关系数据库的多个表还可以用外键实现一对多、多对多等关联
相应地，ORM框架也可以提供两个对象之间的一对多、多对多等功能。

例如，如果一个User拥有多个Book，就可以定义一对多关系如下：
"""


# class User(Base):
#     __tablename__ = 'user1'
#
#     id = Column(String(20), primary_key=True)
#     name = Column(String(20))
#     # 一对多:
#     books = relationship('Book')
#
#
# class Book(Base):
#     __tablename__ = 'book'
#
#     id = Column(String(20), primary_key=True)
#     name = Column(String(20))
#     # “多”的一方的book表是通过外键关联到user表的:
#     user_id = Column(String(20), ForeignKey('user.id'))

# 当我们查询一个User对象时，该对象的books属性将返回一个包含若干个Book对象的list