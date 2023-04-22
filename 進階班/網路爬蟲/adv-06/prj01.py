from tkinter import filedialog
from ttkbootstrap import *
from PIL import ImageTk, Image
import sys as s
import os as o
import requests as r


def on_switch_change():
    global check_type, temp
    try:
        if check_type.get() == False:
            lbl3.config(text='溫度:' + str(int(temp) * 9 / 5 + 32) + '℉')
        else:
            lbl3.config(text='溫度:' + str(temp) + '℃')
    except:
        if check_type.get() == False:
            lbl3.config(text='溫度:?℉')
        else:
            lbl3.config(text='溫度:?℃')


def weather():
    global temp
    global check_type
    api_key = 'b6027ac8fd5439ccb4dbd9a27a7820f0'
    base_url = 'https://api.openweathermap.org/data/2.5/weather?'
    city_name = entry.get()
    units = 'metric'

    lang = 'zh_tw'
    send_url = base_url
    send_url += 'appid=' + api_key
    send_url += '&q=' + city_name
    send_url += '&units=' + units
    send_url += '&lang=' + lang
    response = r.get(send_url)
    info = response.json()
    if 'main' in info.keys():
        icon_code = info['weather'][0]['icon']
        icon_url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"
        response = r.get(icon_url)
        with open(f'{icon_code}.png', 'wb') as icon_file:
            icon_file.write(response.content)

        image = Image.open(f'{icon_code}.png')
        tk_image = ImageTk.PhotoImage(image)
        lbl2.config(image=tk_image)
        lbl2.image = tk_image
        temp = info['main']['temp']
        if check_type.get() == False:
            lbl3.config(text='溫度:' + str(int(temp) * 9 / 5 + 32) + '℉')
        else:
            lbl3.config(text='溫度:' + str(temp) + '℃')

        lbl4.config(text='描述:' + str(info['weather'][0]['description']))
    else:
        print('city not found')


o.chdir(s.path[0])

win = tk.Tk()
win.title('GUI')
win.option_add('*font', ('Helvetica', 20))
style = Style(theme='cyborg')
style.configure('TButton', font=('Helvetica', 20))
style.configure('TCheckbutton', font=('Helvetica', 20))

entry = Entry(win, width=30)
entry.grid(row=0, column=1, padx=10, pady=10)

btn = Button(win, text='獲得天氣資訊', command=weather, style='TButton')
btn.grid(row=0, column=2)

lbl = Label(win, text='請輸入想搜尋的城市:')
lbl.grid(row=0, column=0)

lbl2 = Label(win, text='天氣圖標')
lbl2.grid(row=1, column=0)

lbl3 = Label(win, text=f'溫度:?℃')
lbl3.grid(row=1, column=1)

lbl4 = Label(win, text='描述:?')
lbl4.grid(row=1, column=2)

check_type = BooleanVar()
check_type.set(True)

check = Checkbutton(win,
                    text='溫度單位(℃/℉)',
                    variable=check_type,
                    onvalue=True,
                    offvalue=False,
                    command=on_switch_change,
                    style='TCheckbutton')
check.grid(row=2, column=1)

win.mainloop()
