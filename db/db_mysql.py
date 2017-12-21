#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/21 0021.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408
"""
mysql驱动
pip install mysql-connector

如果MySQL的版本≥5.5.3，可以把编码设置为utf8mb4
utf8mb4和utf8完全兼容，但它支持最新的Unicode标准，可以显示emoji字符。

执行INSERT等操作后要调用commit()提交事务；
MySQL的SQL占位符是%s
"""
# 导入MySQL驱动
import mysql.connector

# 连接数据库
conn = mysql.connector.connect(user="root", password="123456", database="test")
# cursor = conn.cursor()

# 建表
# cursor.execute("create table user1 (id varchar(20) primary key , name varchar(20), user_id VARCHAR(20))")
# 添加数据
# cursor.execute("insert into user1 (id, name) values (%s, %s)", [str(x), "TaoYuan"+str(x)])
# print(cursor.rowcount)


# 提交事务
# conn.commit()
# cursor.close()

# 查询
cursor = conn.cursor()
cursor.execute("select * from user1")

values = cursor.fetchall()
print(values)

cursor.close()
conn.close()

# [('0', 'TaoYuan0'), ('1', 'TaoYuan1'), ('2', 'TaoYuan2')]