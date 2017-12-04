#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/4 0004.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408
import logging
import sys


class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def bar():
    try:
        foo("0")
    except ValueError as e:
        print("ValueError:", e)
        raise

def test_log_level():
    # set default logging configuration
    logger = logging.getLogger()  # initialize logging class
    logger.setLevel(logging.DEBUG)  # default log level
    format = logging.Formatter("%(asctime)s - %(message)s")  # output format
    sh = logging.StreamHandler(stream=sys.stdout)  # output to standard output
    sh.setFormatter(format)
    logger.addHandler(sh)

    # use logging to generate log ouput
    logger.info("this is info")
    logger.debug("this is debug")
    logger.warning("this is warning")
    logging.error("this is error")
    logger.critical("this is critical")


bar()

# if __name__ == '__main__':
    # try:
    #     bar("0")
    #     test_log_level()
    # except Exception as e:
    #     logging.exception(e)
    #
    # print("end")
