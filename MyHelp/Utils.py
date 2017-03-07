# -*- coding: utf-8 -*-


# 相关的工具类
import time


def getDate():
    #获得当前日期
    _date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    return _date


def getTime():
    #获得当前时间
    _time = time.strftime('%H:%M:%S', time.localtime(time.time()))
    return _time



