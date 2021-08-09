# -*- coding: utf-8 -*-
"""
@author: ERDEM ERBABA 
"""
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
import random
import numpy as np

window = Tk()
window.title("Tombala Gecesi Uygulaması")
#window.geometry('600x600')
window['bg'] = '#49A'


def clicked():
    b=random.choice(tas)
    lbl.configure(text=b)
    cekilen.append(b)
    tas.remove(b)
    """
    lbl2 = Label(window, text=tas)
    lbl2.grid(column=1, row=3)
    lbl3 = Label(window, text=cekilen)
    lbl3.grid(column=1, row=4)
    """
    if b<10:
        Button(window,text=b,bg="red").grid(row=b,column=2)
    if 9<b<20:
        Button(window,text=b,bg="red").grid(row=b-10,column=2+1)
    if 19<b<30:
        Button(window,text=b,bg="red").grid(row=b-20,column=2+2)
    if 29<b<40:
        Button(window,text=b,bg="red").grid(row=b-30,column=2+3)
    if 39<b<50:
        Button(window,text=b,bg="red").grid(row=b-40,column=2+4)
    if 49<b<60:
        Button(window,text=b,bg="red").grid(row=b-50,column=2+5)
    if 59<b<70:
        Button(window,text=b,bg="red").grid(row=b-60,column=2+6)
    if 69<b<80:
        Button(window,text=b,bg="red").grid(row=b-70,column=2+7)
    if 79<b<90:
        Button(window,text=b,bg="red").grid(row=b-80,column=2+8)
    if 89<b<100:
        Button(window,text=b,bg="red").grid(row=b-90,column=2+9)
    bar['value'] = bar['value'] + 1.1
    if not tas:
        lbl0 = Label(window, text="OYUN BİTTİ TEBRİKLER")
        lbl0.grid(column=1, row=6)

def finished():
    lbl0 = Label(window, text="OYUN BİTTİ TEBRİKLER")
    lbl0.grid(column=1, row=7)

cekilenler=0
taslar=0
for x in range(10):
    for y in range(10):
        Button(window,text=taslar,bg="green").grid(row=y,column=x+2)
        taslar=taslar+1

style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='black')
bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')
bar['value'] = 0

tas = list(range(1,91))
cekilen=[]
"""
lbl4 = Label(window, text="Çekilmeyen Taşlar:   ")
lbl4.grid(column=0, row=3)
lbl5 = Label(window, text="Çekilen Taşlar:   ")
lbl5.grid(column=0, row=4)
"""
lbl0 = Label(window, text="Tombala")
lbl0.grid(column=0, row=0)
lbl = Label(window, text="")
lbl.grid(column=1, row=1)
Button(window,text=0,bg="red").grid(row=0,column=2)
Button(window,text=91,bg="red").grid(row=1,column=11)
Button(window,text=92,bg="red").grid(row=2,column=11)
Button(window,text=93,bg="red").grid(row=3,column=11)
Button(window,text=94,bg="red").grid(row=4,column=11)
Button(window,text=95,bg="red").grid(row=5,column=11)
Button(window,text=96,bg="red").grid(row=6,column=11)
Button(window,text=97,bg="red").grid(row=7,column=11)
Button(window,text=98,bg="red").grid(row=8,column=11)
Button(window,text=99,bg="red").grid(row=9,column=11)
btn = Button(window, text="Sayı Çek", command=clicked)
btn.grid(column=1, row=0)
bar.grid(column=1, row=2)
Label(window, text='1.Çinko Kazananı').grid(row=3, column=0)
Entry(window, bd=3).grid(row=3, column=1)
Label(window, text='2.Çinko Kazananı').grid(row=4, column=0)
Entry(window, bd=3).grid(row=4, column=1)
Label(window, text='     KAZANAN     ').grid(row=5, column=0)
Entry(window, bd=3).grid(row=5, column=1)
btn2 = Button(window, text="Oyunu Bitir", command=finished)
btn2.grid(column=1, row=6)
Button(window,text="ÇEKİLECEK TAŞLAR",bg="green").grid(row=8,column=1)
Button(window,text="ÇEKİLEN TAŞLAR",bg="red").grid(row=9,column=1)
#Label(window, text='x').grid(row=0, column=0)

window.mainloop()