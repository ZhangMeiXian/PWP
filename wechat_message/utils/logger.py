#!/usr/bin/env python 3.6
# -*- coding: utf-8 -*-
"""
@ModuleName: 打印日志
@Author: zhangmeixian
@Date: 2022/06/25
"""

import os
import sys
import datetime


def log(level, msg):
    filename = os.path.basename(sys._getframe().f_back.f_back.f_code.co_filename)
    lineno = sys._getframe().f_back.f_back.f_lineno
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    temp = '[%(time)s] [%(level)+5s] - %(message)s (%(filename)s:%(lineno)s)' \
        % {'time': time, 'level': level, 'message': msg, 'filename': filename, 'lineno': lineno}
    print(temp)


def info(msg):
    """
    打印info级别的日志
    :param msg:
    :return:
    """
    log("INFO", msg)


def error(msg):
    """
    打印error级别的日志
    :param msg:
    :return:
    """
    log("ERROR", msg)


def debug(msg):
    """
    打印debug级别的日志
    :param msg:
    :return:
    """
    log("DEBUG", msg)


def warn(msg):
    """
    打印warn级别的日志
    :param msg:
    :return:
    """
    log("WARN", msg)