#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-15 18:38:32
# @Author  : TaoYuan (1876665310@qq.com)
# @Link    : https://github.com/seeways or http://blog.csdn.net/lftaoyuan
# @Version : $Id$

from tkinter import *
from tkinter import messagebox

text = "Hello TaoYuan"


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.nameInput = None
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.helloLabel = Label(self, text=text)
        self.helloLabel.pack()

        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text="alert", command=self.sound)
        self.alertButton.pack()

        self.quitButton = Button(self, text='quit', command=self.quit)
        self.quitButton.pack()

    def sound(self):
        name = self.nameInput.get() or 'welcome to I_YIN'
        messagebox.showinfo('Message', 'Hello, %s' % name)


app = Application()
# 设置窗口标题:
app.master.title(text)
# 主消息循环:
app.mainloop()
