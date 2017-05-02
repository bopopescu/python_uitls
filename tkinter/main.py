#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import tkinter
root = tkinter.Tk()
root.geometry('600x400')

label = tkinter.Label(root,text='真难')
label.pack()


def buttonActioon_1():
    print('更新咨询')
# bu =
tkinter.Button(root , text ='更新咨询' , command = buttonActioon_1()).pack()

def buttonActioon_2():
    print('更新新闻')
tkinter.Button(root , text ='更新新闻' , command = buttonActioon_2()).pack()



tkinter.mainloop()