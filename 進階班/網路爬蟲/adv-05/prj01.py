import sys as s
import os as o
import requests as r

o.chdir(s.path[0])

api_key = 'b6027ac8fd5439ccb4dbd9a27a7820f0'  #API key
# API URL
base_url = 'https://api.openweathermap.org/data/2.5/weather?'
city_name = input('Enter city name:')
units = 'metric'  #單位(公制)
lang = 'zh_tw'  #語言(繁體中文)
send_url = base_url
send_url += 'appid=' + api_key
send_url += '&q=' + city_name
send_url += '&units=' + units
send_url += '&lang=' + lang
response = r.get(send_url)
info = response.json()

print('City=' + str(info['name']))
print('Temperature=' + str(info['main']['temp']) + '℃')
print('Description=' + str(info['weather'][0]['description']))

if 'main' in info.keys():
    icon_code = info['weather'][0]['icon']
    icon_url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"
    response = r.get(icon_url)
    with open(f'{icon_code}.png', 'wb') as icon_file:
        icon_file.write(response.content)
else:
    print('city not found')
