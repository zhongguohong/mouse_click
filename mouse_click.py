#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/24 19:25
# @Author  : dami
# @File    : mouse_click.py
# @Site    :


import time
from pymouse import PyMouse
from tkinter import Tk, Entry, IntVar, Label, EW
import keyboard
import threading

m = PyMouse()
e = threading.Event()


def run(v):
    tm = time.time()
    while True:
        time.sleep(0.001)
        if e.is_set():
            if tm + v.get() <= time.time():
                tm = time.time()
                m.click(*m.position())


def toggle():
    while True:
        time.sleep(0.001)
        keyboard.wait('F4')
        if not e.is_set():
            e.set()
        else:
            e.clear()


top = Tk()
top.title('大米 鼠标连点器')
l = Label(top, text="点击间隔（秒）：")
l.grid(row=0, column=1)
v = IntVar()
v.set(60)
w = Entry(top, textvariable=v)
w.grid(row=0, column=2)
b = Label(text='请将鼠标移动到需要自动点击的地方按F4键开始自动点击')
b.grid(row=1, column=1, columnspan=2, sticky=EW)
t1 = threading.Thread(target=run, args=(v,))
t2 = threading.Thread(target=toggle)
t1.setDaemon(True)
t1.start()
t2.setDaemon(True)
t2.start()
top.mainloop()
