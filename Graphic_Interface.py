#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('\n\n\033[0;31;40m-1--------图形界面--------------------------------------\033[0m')
#Python支持多种图像的第三方库：Tk、wxWidgets、QT、GTK
#Python自带的库Tkinter调用Tk的接口，Tk调用操作系统提供的本地GUI接口。
#若执行报错：sudo apt-get install python3-tk
from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):  #从Frame派生一个Application类，这是所有Widget的父容器
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()  #pack()方法把Widget加入到父容器中，并实现布局。pack()是最简单的布局，grid()可以实现更复杂的布局
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)

app = Application()
app.master.title('Hello World')  #设置窗口标题
app.mainloop()  #主消息循环负责监听来自操作系统的消息，如果消息处理非常耗时，就需要在新线程中处理