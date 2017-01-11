#!/usr/bin/env python3
# -*- coding: utf-8 -*-'

import matplotlib
from matplotlib.font_manager import FontProperties
matplotlib.use('TkAgg')
myfont = FontProperties(fname='/Library/Fonts/huawenfangsong.ttf')
matplotlib.rcParams['axes.unicode_minus']=False


import matplotlib.pyplot as plt





def main():
    import tushare as ts
    data = ts.get_hist_data('sz50', start='2016-11-01', end='2016-12-30')
    data = data.sort_index()


    # # 一个基本的折线图
    x = range(len(data))
    # 收盘价的折线图
    plt.plot(x, data['close'])
    plt.title(u'中文' , fontproperties=myfont)
    #
    # x = range(len(data))
    # plt.plot(x, data['close'])
    # plt.plot(x, data['high'])
    #
    # # 设置图形大小和线条颜色
    # x = range(len(data))
    # plt.figure(figsize=(10, 5))
    # plt.plot(x, data['close'])
    # plt.plot(x, data['high'])

    # x = range(len(data))
    # plt.figure(figsize=(10, 5))
    # plt.plot(x, data['close'])
    # plt.plot(x, data['high'], color='r')
    # plt.title("中文")

    # from matplotlib.pylab import datestr2num
    # x = range(len(data))
    # x_date = [datestr2num(i) for i in data.index]
    # plt.figure(figsize=(10, 5))
    # plt.title("上证50指数历史最高价、收盘价走势折线图")
    # plt.xlabel("时间")
    # # plt.xticks(x,[i for i in data.index])
    # plt.ylabel("指数")
    # plt.plot_date(x_date, data['close'], '-', label="收盘价")
    # plt.plot_date(x_date, data['high'], '-', color='r', label="开盘价")
    # plt.legend()


    # x = range(len(data))
    # x_date = [datestr2num(i) for i in data.index]
    # plt.style.use('ggplot')
    # plt.figure(figsize=(10, 5))
    # plt.title("image")
    # plt.xlabel("time")
    # plt.xticks(rotation=45)
    # plt.ylabel("index")
    # plt.plot_date(x_date, data['close'], '-', label="sp")
    # plt.plot_date(x_date, data['high'], '-', label="max")
    # plt.legend()
    # plt.grid(True)


    plt.show()
    plt.savefig('test2.jpg')

if __name__ == '__main__':
    main()

