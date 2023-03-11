from tkinter import *
import random as r
import sys as s
import os as o


def exit():
    win.destroy()


def move_canvas(event):
    key = event.keysym
    if key == 'Right':
        canvas.move(myimg, 10, 0)
    elif key == "Left":
        canvas.move(myimg, -10, 0)
    elif key == 'Up':
        canvas.move(myimg, 0, -10)
    elif key == 'Down':
        canvas.move(myimg, 0, 10)


o.chdir(s.path[0])  #設定工作目錄

win = Tk()
win.title('GUI')

quit_btn = Button(win, text='Quit', command=exit, fg='red')
quit_btn.pack()

canvas = Canvas(win, width=10000, height=10000, bg='black')
canvas.pack()

win.iconbitmap('業火拳統.ico')

img = PhotoImage(file='魯夫.gif')

rec = canvas.create_rectangle(0, 0, 30, 30, fill='red3')

circle = canvas.create_oval(0, 0, 30, 30, fill='black')

myimg = canvas.create_image(300, 300, image=img)

msg = canvas.create_text(300,
                         100,
                         text='llllllllllllllllll',
                         fill='red',
                         font=('Arial', 30))

canvas.bind_all('<Key>', move_canvas)
win.mainloop()

a = 10
print((lambda x: x + 10)(a))  #20
