from ttkbootstrap import *
import random as r
import sys as s
import os as o


def e():
    try:
        e = eval(entry.get())
    except:
        lbl.config(text='error')
    lbl.config(text=e)


win = tk.Tk()
win.title('GUI')
win.option_add('*font', ('Helvetica', 20))

style = Style(theme='cyborg')
style.configure('TButton', font=('Helvetica', 20))

entry = Entry(win, width=30)
entry.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

btn = Button(win, text='顯示計算結果', command=e, style='TButton')
btn.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

lbl = Label(win, text='計算結果')
lbl.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

win.mainloop()
