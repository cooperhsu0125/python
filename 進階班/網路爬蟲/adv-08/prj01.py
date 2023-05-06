import sys as s
import os as o
import requests as r
import datetime as d
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties as f

o.chdir(s.path[0])
font = f(fname='NotoSansTC-Light.otf', size=21)

day = []
tem = []

api_key = '892da2f13edf3c7f382637760e72d224'  #API key
# API URL
base_url = "https://api.openweathermap.org/data/2.5/onecall?"
lon = '121.5319'
lat = '25.0478'
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

print(send_url)

reponse = r.get(send_url)
info = reponse.json()

if 'daily' in info.keys():
    for i in range(7):
        temp = info['daily'][i]['temp']['day']
        time = d.datetime.fromtimestamp(
            info['daily'][i]['dt']).strftime('%m/%d')
        print(f'{time}的溫度是{temp}度')
        day.append(time)
        tem.append(temp)
else:
    print('request fail')

fig, ax = plt.subplots()
ax.plot(day, tem)
ax.set_xlabel('日期', fontproperties=font)
ax.set_ylabel('溫度', fontproperties=font)
ax.set_title('7天氣溫預測', fontproperties=font)

plt.show()