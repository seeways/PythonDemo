#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/5 0005.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408
# 记录错误日志到指定目录


import logging
import os


class MyLogger(object):
    def __init__(self, name, path='log'):
        log_path = str(os.getcwd()) + '\\' + str(name) + '_' + str(path) + '\\'
        self.error_lg = logging.getLogger('error')
        self.info_lg = logging.getLogger('info')
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        if len(self.error_lg.handlers) == 0:  # 确保只有1个handler
            error_h = logging.FileHandler(log_path + 'error.log')
            error_h.setFormatter(formatter)
            self.error_lg.addHandler(error_h)
        if len(self.info_lg.handlers) == 0:
            info_h = logging.FileHandler(log_path + 'info.log')
            info_h.setFormatter(formatter)
            self.info_lg.addHandler(info_h)

    def info(self, msg):
        self.info_lg.info(msg)

    def error(self, msg):
        self.error_lg.error(msg)

    def release(self):
        logging.shutdown()  # flushing and closing any handlers (not removing them)


if __name__ == '__main__':
    t_log = MyLogger("error", "log")
    t_log.error('error-5')
    t_log.info('info-5')
    t_log.release()

    print("End")
