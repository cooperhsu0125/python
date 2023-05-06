import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from ttkbootstrap import *


def draw_graph():
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  #[x軸][y軸]長度要一樣，折線圖
    ax.plot([1, 2, 3, 4], [1, 4, 2, 3], 'o')  #散布圖
    canvas = FigureCanvasTkAgg(fig, master=win)
    canvas.draw()
    canvas = canvas.get_tk_widget()
    canvas.grid(row=0, column=0, padx=10, pady=10)


def on_closing():
    win.destroy()
    plt.close('all')


win = tk.Tk()
win.protocol('WM_DELETE_WINDOW', on_closing)
style = Style(theme="minty")
draw_button = Button(win, text="Draw Graph", command=draw_graph)
draw_button.grid(row=1, column=0, padx=10, pady=10)
win.mainloop()