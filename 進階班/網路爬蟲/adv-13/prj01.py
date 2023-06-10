###模組###
from ttkbootstrap import *
import time

###視窗###
win = tk.Tk()


###元件###
def start_progress():
    for i in range(101):
        progress['value'] = i
        percent_label.config(text=f'{i}%')
        win.update()
        time.sleep(0.01)


progress = Progressbar(win, orient=HORIZONTAL, length=200,
                       mode='determinate')  #進度條
progress.grid(row=0, column=0, padx=10, pady=10)
percent_label = Label(win, text='')
percent_label.grid(row=0, column=1, padx=10, pady=10)
start_button = Button(win, text='start', command=start_progress)
start_button.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

win.mainloop()