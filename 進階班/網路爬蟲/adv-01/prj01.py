from tkinter import *
import random as r


def hi():
    Lbl.config(text='hi', fg=color[r.randint(0, 2)], bg='white')


win = Tk()
win.title('1')

color = ['red', 'green', 'blue']

Lbl = Label(win, text='', fg='white', bg='black')
Lbl.pack()

btn = Button(win, text='hi', command=hi, fg='#009EFF', bg='#646464')
btn.pack()

win.mainloop()