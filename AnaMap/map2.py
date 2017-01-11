#!/usr/bin/env python3
# -*- coding: utf-8 -*-'

import matplotlib
from matplotlib.font_manager import FontProperties
from requests.packages.urllib3.connectionpool import xrange

matplotlib.use('TkAgg')
myfont = FontProperties(fname='/Library/Fonts/huawenfangsong.ttf')
matplotlib.rcParams['axes.unicode_minus']=False

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


def data_gen_bubble_sort():
    for i in range(len(data_to_be_sorted)):
        for j in range(0, len(data_to_be_sorted)-i-1):
            if data_to_be_sorted[j] > data_to_be_sorted[j+1]:
                # exchange the corresponding data
                data_to_be_sorted[j], data_to_be_sorted[j+1] = data_to_be_sorted[j+1], data_to_be_sorted[j]
                yield data_to_be_sorted
        # corted part set color to color sorted
        lines[len(data_to_be_sorted)-i-1].set_color(color_sorted)
        yield data_to_be_sorted


def data_gen_insert_sort():
    for i in range(0,len(data_to_be_sorted)):
        for j in range(i, 0, -1):
            if data_to_be_sorted[j] < data_to_be_sorted[j-1]:
                # exchange the corresponding data
                data_to_be_sorted[j], data_to_be_sorted[j-1] = data_to_be_sorted[j-1], data_to_be_sorted[j]
                yield data_to_be_sorted
        # corted part set color to color sorted
        lines[i].set_color(color_sorted)
        yield data_to_be_sorted

def update(data):
    """
    这里面获取到的data来自 data_gen返回的数据
    """
    for i in xrange(len(data)):
        lines[i].set_ydata([0, data[i]])

    return lines


def init():
    ax.set_ylim(-1, max_val)
    ax.set_xlim(-1, n+1)
    return


color_original = '#ff9999'
color_sorted = '#9999ff'
color_selected = '#99ff99'

n = 20
max_val = 50
# 产生 n 个 0到50之间的数
data_to_be_sorted = np.random.rand(n)*max_val

fig, ax = plt.subplots()

xdata = [[i+1 for i in xrange(n)], [i+1 for i in xrange(n)]]
ydata = [[0 for i in xrange(n)], data_to_be_sorted]

lines = ax.plot(xdata, ydata, lw=2, c=color_original)


#print lines[0].__str__


#ani = animation.FuncAnimation(fig, update, data_gen_bubble_sort, interval=300,repeat=False, init_func=init)
ani = animation.FuncAnimation(fig, update, data_gen_insert_sort, interval=300,repeat=False, init_func=init)
#ani = animation.FuncAnimation(fig, update, data_gen_select_sort, interval=300,repeat=False, init_func=init)

plt.show()