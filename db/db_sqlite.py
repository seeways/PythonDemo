#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/20 0020.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408
"""
SQLite是一种嵌入式数据库，它的数据库就是一个文件
iOS和Android的App中都可以集成

Python就内置SQLite3

Python定义了一套操作数据库的API接口
任何数据库要连接到Python，只需要提供符合Python标准的数据库驱动即可

SQLite的驱动内置在Python标准库中

使用Cursor对象执行insert，update，delete语句时，执行结果由rowcount返回影响的行数

使用Cursor对象执行select语句时，通过featchall()可以拿到结果集。
结果集是一个list，每个元素都是一个tuple，对应一行记录。
? 表示占位符，需要和参数对应
cursor.execute('select * from user where name=? and pwd=?', ('abc', 'password'))
"""

# 导入驱动
import sqlite3

# 连接数据库，不存在则自动创建
conn = sqlite3.connect("test.db")
# 创建一个游标
cursor = conn.cursor()
# 创建user表
cursor.execute("CREATE TABLE user (id VARCHAR(20) PRIMARY KEY, name TEXT)")
# 添加一条记录
cursor.execute("INSERT INTO user (id, name) VALUES('1', 'TaoYuan')")
# 获取插入行数
print(cursor.rowcount)


# # 查询
# cursor.execute("select * from user")
# # 获取查询结果
# values = cursor.fetchall()
# print(values)  # [('1', 'Taoyuan')]


# 关闭游标
cursor.close()
# 提交事务
conn.commit()
# 关闭连接
conn.close()
