######################匯入模組######################
import pygame as pg
import sys as s
import math


####################定義函式######################
def check_click(pos, x_min, y_min, x_max, y_max):
    x_match = x_min < pos[0] < x_max
    y_match = y_min < pos[1] < y_max
    if x_match and y_match:
        return True
    else:
        return False


######################初始化######################
pg.init()  #啟動pygame
width = 1300  #視窗寬度
height = 650  #視窗高度
######################建立視窗及物件######################
screen = pg.display.set_mode((width, height))  #視窗大小
pg.display.set_caption('game')  #視窗標題
######################設定文字######################
typeface = pg.font.get_default_font()  #取得系統文字
font = pg.font.Font(typeface, 24)  #設定字體跟大小
title = font.render('start', True, (0, 0, 0))  #設定文字參數:文字內容,是否開啟反鋸齒,文字顏色,背景顏色
tit_w = title.get_width()
tit_h = title.get_height()
######################建立畫布######################
bg = pg.Surface(screen.get_size())  #建立畫布
bg.fill(
    (255, 255,
     255))  #畫布RGB顏色(https://www.rapidtables.com/convert/color/rgb-to-hex.html)
# 畫圓(畫布,顏色,圓心,半徑,線寬)
# pg.draw.circle(bg, (0, 0, 255), (200, 100), 30, 0)  #0是填滿
# pg.draw.circle(bg, (0, 0, 255), (400, 100), 30, 0)
# # 畫矩形(畫布,顏色,[x,y,寬,高],線寬)
# pg.draw.rect(bg, (0, 0, 255), [270, 130, 60, 40], 5)
# # 畫橢圓(畫布,顏色,[x,y,寬,高],線寬)
# pg.draw.ellipse(bg, (0, 0, 255), [130, 160, 60, 35], 5)
# pg.draw.ellipse(bg, (0, 0, 255), [400, 160, 60, 35], 5)
# # 畫線(畫部,顏色,起點,終點,線寬)
# pg.draw.line(bg, (0, 0, 255), (280, 220), (320, 220), 3)
# # 畫多邊形(畫布,顏色,[[x1,y1],[x2,y2],[x3,y3]...],線寬)
# pg.draw.polygon(bg, (100, 200, 45), [[100, 100], [0, 200], [200, 200]], 0)
# # 畫圓弧(畫部,顏色,[x,y,寬,高],起始角度,結束角度,線寬)
# pg.draw.arc(bg, (255, 0, 0), [100, 100, 100, 50], math.radians(180),
#             math.radians(0), 2)
######################循環偵測######################
paint = False
while True:
    for event in pg.event.get():
        pos = pg.mouse.get_pos()
        if event.type == pg.QUIT:
            s.exit()
        if event.type == pg.MOUSEBUTTONDOWN:

            if check_click(pos, 0, 0, tit_w, tit_h):
                pg.draw.circle(bg, (0, 0, 255), (200, 100), 30, 0)  #0是填滿
                pg.draw.circle(bg, (0, 0, 255), (400, 100), 30, 0)
                pg.draw.rect(bg, (0, 0, 255), [270, 130, 60, 40], 5)
                pg.draw.ellipse(bg, (0, 0, 255), [130, 160, 60, 35], 5)
                pg.draw.ellipse(bg, (0, 0, 255), [400, 160, 60, 35], 5)
                pg.draw.line(bg, (0, 0, 255), (280, 220), (320, 220), 3)
                pg.draw.polygon(bg, (100, 200, 45),
                                [[100, 100], [0, 200], [200, 200]], 0)
                pg.draw.arc(bg, (255, 0, 0), [100, 100, 100, 50],
                            math.radians(180), math.radians(0), 2)
            else:
                if event.button == 1:
                    color = (0, 0, 0)
                if event.button == 3:
                    color = (255, 255, 255)
                    print(pg.mouse.get_pos())
                    paint = not (paint)

    if paint:
        x, y = pos
        if color == (0, 0, 0):
            pg.draw.circle(bg, color, (x, y), 10, 0)
        else:
            pg.draw.circle(bg, color, (x, y), 20, 0)
    screen.blit(bg, (0, 0))  #畫布0,0在視窗左上角
    screen.blit(title, (0, 0))
    pg.display.update()  #更新視窗
