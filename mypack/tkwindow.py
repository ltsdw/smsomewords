#! /hint/python

from tkinter import *

from .appenditemquit import appendItemQuit

class Application:
    def __init__(self, master=None):

        self.defaultFont = ('Mono', '10')
        self.containerM = Frame(master, width=100, height=100)
        self.containerM.pack()
        self.title = Label(self.containerM, text='言葉のリスト')
        self.title.pack(side=TOP)

        self.containerN = Frame(master, width=100, height=100)
        self.containerN['padx'] = 20
        self.containerN.pack()
        self.entryLabel = Label(self.containerN, text='入力：', font=self.defaultFont)
        self.entryLabel.pack(side=LEFT)

        self.entry = Entry(self.containerN)
        self.entry['width'] = 30
        self.entry['font'] = self.defaultFont
        self.entry.pack(side=RIGHT)

        self.containerE = Frame(master, width=100, height=100)
        self.containerE.pack()
        self.quit = Button(self.containerE)
        self.quit['text'] = '完成'
        self.quit['font'] = self.defaultFont
        self.quit['width'] = 5
        self.quit['command'] = self.callAppendItemQuit
        self.quit.pack(side=BOTTOM)
    

    def callAppendItemQuit(self):
        self.lista = self.entry.get().split(" ")
        appendItemQuit(self.lista)

