######################匯入模組######################
import pygame as pg
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

####################設定文字######################
label = 'start'
typeface = pg.font.get_default_font()
font = pg.font.Font(typeface, 24)
title = font.render(label, True, (0, 0, 0))
tit_w = title.get_width()
tit_h = title.get_height()
####################設定雪花基本參數######################

####################新增fps######################

######################循環偵測######################
while True:
    for event in pg.event.get():
        pos = pg.mouse.get_pos()
        if event.type == pg.QUIT:
            s.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            if check_click(pos, 0, 0, tit_w, tit_h):
                if label == 'start':
                    label = 'stop'
                else:
                    label = 'start'
                title = font.render(label, True, (0, 0, 0))
    screen.blit(bg, (0, 0))
    screen.blit(title, (0, 0))
    pg.display.update()