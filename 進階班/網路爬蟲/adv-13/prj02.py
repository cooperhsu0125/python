from mod.mod import *
import sys as s
from ttkbootstrap import *
import os as o

o.chdir(s.path[0])


def get_video_info_gui():
    _, _, _, _, res = get_video_info(entry.get())
    res_option['menu'].delete(0, 'end')
    for r in res:
        res_option['menu'].add_command(label=r, command=tk._setit(res_var, r))
    res_var.set(res[0])


def download_video_gui():

    if download_video(entry.get(), res_var.get(), show_progress):
        lbl2.configure(text='下載完成')
    else:
        lbl2.config(text='下載失敗')


def show_progress(stream, chunk, bytes_remaining):
    percent = (100 * (stream.filesize - bytes_remaining)) / stream.filesize
    percent_label.config(text=f'{percent:.2f}%')
    progress['value'] = percent
    win.update()


win = tk.Tk()
win.title('GUI')
win.option_add('*font', ('Helvetica', 10))
style = Style(theme='cyborg')
style.configure('TButton', font=('Helvetica', 10))
style.configure('TCheckbutton', font=('Helvetica', 10))

entry = Entry(win, width=30)
entry.grid(row=0, column=1, padx=10, pady=10)

lbl = Label(win, text='輸入Youtube影片網址:')
lbl.grid(row=0, column=0, padx=10, pady=10)

lbl1 = Label(win, text='選擇影片解析度:')
lbl1.grid(row=1, column=0, padx=10, pady=10)

lbl2 = Label(win, text='.')
lbl2.grid(row=2, column=0, padx=10, pady=10)

btn = Button(win, text='搜尋影片資訊', command=get_video_info_gui, style='TButton')
btn.grid(row=0, column=2, padx=10, pady=10)

btn1 = Button(win, text='下載影片', command=download_video_gui, style='TButton')
btn1.grid(row=1, column=2, padx=10, pady=10)

res_var = tk.StringVar()
res_option = OptionMenu(win, res_var, ())
res_option.grid(row=1, column=1, padx=10, pady=10)

progress = Progressbar(win, orient=HORIZONTAL, length=200, mode='determinate')
progress.grid(row=2, column=1, padx=10, pady=10)
percent_label = Label(win, text='')
percent_label.grid(row=2, column=2, padx=10, pady=10)

win.mainloop()