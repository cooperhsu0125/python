from tkinter import filedialog
from ttkbootstrap import *
from PIL import ImageTk, Image
import sys as s
import os as o
import requests as r
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.font_manager import FontProperties as f
import datetime as d


def on_closing():
    win.destroy()
    plt.close('all')


def on_switch_change():
    global check_type, temp, units
    if check_type.get():
        units = 'meric'
    else:
        units = 'imperial'
    if lbl3.cget('text') != '溫度:?℃':
        if units == 'meric':
            temp = round((temp - 32) * 5 / 9, 2)
            lbl3.config(text='溫度:' + str(temp) + '℃')
        elif units == 'imperial':
            temp = round(temp * 9 / 5 + 32, 2)
            lbl3.config(text='溫度:' + str(temp) + '℉')
    # try:
    #     if check_type.get() == False:
    #         lbl3.config(text='溫度:' + str(int(temp) * 9 / 5 + 32) + '℉')
    #     else:
    #         lbl3.config(text='溫度:' + str(temp) + '℃')
    # except:
    #     if check_type.get() == False:
    #         lbl3.config(text='溫度:?℉')
    #     else:
    #         lbl3.config(text='溫度:?℃')


def weather():
    global temp
    global check_type
    global units

    api_key = '892da2f13edf3c7f382637760e72d224'  #API key
    # API URL
    base_url = "https://api.openweathermap.org/data/2.5/onecall?"
    lon = entry.get()
    lat = entry2.get()
    exclude = 'minutely,hourly'
    units = 'metric'
    lang = 'zh_tw'
    send_url = base_url
    send_url += 'lat=' + lat
    send_url += '&lon=' + lon
    send_url += '&exclude=' + exclude
    send_url += '&appid=' + api_key
    send_url += '&units=' + units
    send_url += '&lang=' + lang

    response = r.get(send_url)
    info = response.json()

    if 'daily' in info.keys():
        icon_code = info['current']['weather'][0]['icon']
        icon_url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"
        response = r.get(icon_url)
        with open(f'{icon_code}.png', 'wb') as icon_file:
            icon_file.write(response.content)

        image = Image.open(f'{icon_code}.png')
        tk_image = ImageTk.PhotoImage(image)
        lbl2.config(image=tk_image)
        lbl2.image = tk_image

        temp = info['current']['temp']
        # if check_type.get() == False:
        #     lbl3.config(text='溫度:' + str(int(temp) * 9 / 5 + 32) + '℉')
        # else:
        lbl3.config(text='溫度:' + str(temp) + '℃')

        lbl4.config(text='描述:' +
                    str(info['current']['weather'][0]['description']))
        lbl.config(text=f"目前搜尋的地區:{info['timezone']}")

        day = []
        tem = []

        for i in range(7):
            temp1 = info['daily'][i]['temp']['day']
            time = d.datetime.fromtimestamp(
                info['daily'][i]['dt']).strftime('%m/%d')
            print(f'{time}的溫度是{temp1}度')
            day.append(time)
            tem.append(temp1)
    else:
        print('request fail')

    fig, ax = plt.subplots()
    ax.plot(day, tem)
    canvas = FigureCanvasTkAgg(fig, master=win)
    canvas.draw()
    canvas = canvas.get_tk_widget()
    canvas.grid(row=4, column=0, columnspan=3, padx=10, pady=10)


o.chdir(s.path[0])

win = tk.Tk()
win.protocol('WM_DELETE_WINDOW', on_closing)
win.title('GUI')
win.option_add('*font', ('Helvetica', 20))
style = Style(theme='cyborg')
style.configure('TButton', font=('Helvetica', 20))
style.configure('TCheckbutton', font=('Helvetica', 20))

entry = Entry(win, width=30)
entry.grid(row=0, column=1, padx=10, pady=10)

entry2 = Entry(win, width=30)
entry2.grid(row=1, column=1, padx=10, pady=10)

btn = Button(win, text='獲得天氣資訊', command=weather, style='TButton')
btn.grid(row=0, column=2, rowspan=2)

lbl = Label(win, text='目前搜尋的地區:?')
lbl.grid(row=0, column=0, rowspan=2)

lbl2 = Label(win, text='天氣圖標')
lbl2.grid(row=2, column=0)

lbl3 = Label(win, text=f'溫度:?℃')
lbl3.grid(row=2, column=1)

lbl4 = Label(win, text='描述:?')
lbl4.grid(row=2, column=2)

check_type = BooleanVar()
check_type.set(True)

check = Checkbutton(win,
                    text='溫度單位(℃/℉)',
                    variable=check_type,
                    onvalue=True,
                    offvalue=False,
                    command=on_switch_change,
                    style='TCheckbutton')
check.grid(row=3, column=1)

win.mainloop()