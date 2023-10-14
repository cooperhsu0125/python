######################匯入模組######################
import pygame as pg
import random as r
import sys as s
import os


####################定義函式######################
def check_click(pos, x_min, y_min, x_max, y_max):
    x_match = x_min < pos[0] < x_max
    y_match = y_min < pos[1] < y_max
    if x_match and y_match:
        return True
    else:
        return False


def snow_fall():
    for snow in snow_list:
        pg.draw.circle(screen, (255, 255, 255),
                       (snow['x_site'], snow['y_site']), snow['radius'])  #畫出雪花
        snow['x_site'] += snow['x_shift']  #計算雪花下次顯示的座標
        snow['y_site'] += snow['radius']
        if snow['y_site'] > bg_y or snow['x_site'] > bg_x:  #如果雪花落出畫面，重設位置
            snow['y_site'] = r.randint(-10, -1)
            snow['x_site'] = r.randint(0, bg_x)


####################初始化######################
os.chdir(s.path[0])
pg.init()
bg_img = 'snow.jpg'
bg = pg.image.load(bg_img)

bg_x = bg.get_width()
bg_y = bg.get_height()
######################建立視窗######################
screen = pg.display.set_mode((bg_x, bg_y))
pg.display.set_caption('snow')
####################撥放音樂######################
mp3_path = "snow-dream.mp3"
pg.mixer.music.load(mp3_path)  # 音樂載入程式
pg.mixer.music.play()  # 播放音樂
pg.mixer.music.fadeout(600000)  # 設定音樂撥放時間單位毫秒
pg.mixer.music.pause()
####################設定文字######################
label = 'start'
typeface = pg.font.get_default_font()
font = pg.font.Font(typeface, 24)
title = font.render(label, True, (0, 0, 0))
tit_w = title.get_width()
tit_h = title.get_height()
####################設定雪花基本參數######################
snow_list = []
for i in range(150):
    x_site = r.randrange(0, bg_x)
    y_site = r.randrange(-bg_y, -1)
    x_shift = r.randint(-1, 1)
    radius = r.randint(4, 6)
    snow_list.append({
        'x_site': x_site,
        'y_site': y_site,
        'x_shift': x_shift,
        'radius': radius
    })
####################新增fps######################
clock = pg.time.Clock()

######################循環偵測######################
change = True
snow = False
cnt = 0
while True:
    clock.tick(60)  #幀數
    pos = pg.mouse.get_pos()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            s.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            if check_click(pos, 0, 0, tit_w, tit_h):
                change = not change

    if cnt > 10:
        cnt = 0
        for snow in snow_list:

            snow['x_shift'] = r.randint(-3, 3)
    else:
        cnt += 1

    screen.blit(bg, (0, 0))
    screen.blit(title, (0, 0))
    if change:
        title = font.render("Start", True, (0, 0, 0))
        pg.mixer.music.pause()

    else:
        title = font.render("Stop", True, (0, 0, 0))
        pg.mixer.music.unpause()
        snow_fall()
    pg.display.update()
