#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/6 0006.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408
import unittest


class TestDict(unittest.TestCase):
    def setUp(self):
        print('setUp...')

    def test_isequeals(self):
        self.assertEqual(abs(-1), 1)

    def tearDown(self):
        print('tearDown...')
