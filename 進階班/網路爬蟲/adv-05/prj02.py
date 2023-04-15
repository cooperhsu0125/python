from tkinter import filedialog
from ttkbootstrap import *
from PIL import ImageTk, Image
import sys as s
import os as o
import requests as r


def on_switch_change():
    check_label.config(text=str(check_type.get()))


o.chdir(s.path[0])

win = tk.Tk()
win.title('GUI')
win.option_add('*font', ('Helvetica', 20))
style = Style(theme='cyborg')
style.configure('TButton', font=('Helvetica', 20))

entry = Entry(win, width=30)
entry.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

check_type = BooleanVar()
check_type.set(True)

check_label = Label(win, text='True')
check_label.grid(row=1, column=2)

check = Checkbutton(win,
                    variable=check_type,
                    onvalue=True,
                    offvalue=False,
                    command=on_switch_change)
check.grid(row=1, column=1)
win.mainloop()
