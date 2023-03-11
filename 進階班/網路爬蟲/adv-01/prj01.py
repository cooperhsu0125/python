from tkinter import *
import random as r


def hi():
    Lbl.config(text='hi', fg=color[r.randint(0, 2)], bg='white')


win = Tk()
win.title('GUI')

color = [
    "black", "red", "green", "blue", "yellow", "orange", "purple", "pink",
    "brown", "gray", "cyan", "magenta", "gold", "silver", "lime", "maroon",
    "navy", "olive", "teal", "violet", "indigo", "coral", "crimson", "hotpink",
    "khaki", "lavender", "lavenderblush", "lemonchiffon", "lightblue",
    "lightcoral", "lightcyan", "lightgoldenrodyellow", "lightgreen",
    "lightgrey", "lightpink", "lightsalmon", "lightseagreen", "lightskyblue",
    "lightslategray", "lightsteelblue", "lightyellow"
]

Lbl = Label(win, text='', fg='white', bg='black')
Lbl.pack()

btn = Button(win, text='hi', command=hi, fg='#009EFF', bg='#646464')
btn.pack()

win.mainloop()