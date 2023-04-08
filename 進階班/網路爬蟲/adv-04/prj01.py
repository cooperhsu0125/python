from tkinter import filedialog
from ttkbootstrap import *
from PIL import ImageTk, Image
import random as r
import sys as s
import os as o


def e():
    global file_path
    file_path = filedialog.askopenfilename(initialdir=s.path[0])
    Lbl2.config(text=file_path)


def y():
    global file_path
    image = Image.open(file_path)
    image = image.resize((canvas.winfo_width(), canvas.winfo_height()),
                         Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor='nw', image=photo)
    canvas.image = photo


o.chdir(s.path[0])  #設定工作目錄

win = tk.Tk()
win.title('GUI')
win.option_add('*font', ('Helvetica', 20))  #設定預設字形

style = Style(theme='cyborg')  #設定主題
style.configure('TButton', font=('Helvetica', 20))  #Tbutton是固定的, 設定按鈕字形

Lbl = Label(win, text='選擇檔案:')
Lbl.grid(row=0, column=0, sticky='E')  #row:Y  column:X  sticky靠哪個方位

Lbl2 = Label(win, text='無')
Lbl2.grid(row=0, column=1, sticky='E')

btn = Button(win, text='瀏覽', command=e, style='TButton')
btn.grid(row=0, column=2, sticky='W')

btn1 = Button(win, text='顯示', command=y, style="TButton")
btn1.grid(row=1, columnspan=3, sticky='EW')

canvas = Canvas(win, width=600, height=600)
canvas.grid(row=2, columnspan=3, sticky='EW')

win.mainloop()