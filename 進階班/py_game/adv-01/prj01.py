######################匯入模組######################
import pygame as pg
import sys as s
import math
######################初始化######################
pg.init()  #啟動pygame
width = 1300  #視窗寬度
height = 650  #視窗高度
######################建立視窗及物件######################
screen = pg.display.set_mode((width, height))  #視窗大小
pg.display.set_caption('game')  #視窗標題
######################建立畫布######################
bg = pg.Surface((width, height))  #建立畫布
bg.fill(
    (255, 255,
     255))  #畫布RGB顏色(https://www.rapidtables.com/convert/color/rgb-to-hex.html)
# 畫圓(畫布,顏色,圓心,半徑,線寬)
pg.draw.circle(bg, (0, 0, 255), (200, 100), 30, 0)  #0是填滿
pg.draw.circle(bg, (0, 0, 255), (400, 100), 30, 0)
# 畫矩形(畫布,顏色,[x,y,寬,高],線寬)
pg.draw.rect(bg, (0, 0, 255), [270, 130, 60, 40], 5)
# 畫橢圓(畫布,顏色,[x,y,寬,高],線寬)
pg.draw.ellipse(bg, (0, 0, 255), [130, 160, 60, 35], 5)
pg.draw.ellipse(bg, (0, 0, 255), [400, 160, 60, 35], 5)
# 畫線(畫部,顏色,起點,終點,線寬)
pg.draw.line(bg, (0, 0, 255), (280, 220), (320, 220), 3)
# 畫多邊形(畫布,顏色,[[x1,y1],[x2,y2],[x3,y3]...],線寬)
pg.draw.polygon(bg, (100, 200, 45), [[100, 100], [0, 200], [200, 200]], 0)
# 畫圓弧(畫部,顏色,[x,y,寬,高],起始角度,結束角度,線寬)
pg.draw.arc(bg, (255, 0, 0), [100, 100, 100, 50], math.radians(180),
            math.radians(0), 2)
######################循環偵測######################
paint = False
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            s.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                color = (0, 0, 0)
            elif event.button == 3:
                color = (255, 255, 255)
            print(pg.mouse.get_pos())
            paint = not (paint)
    if paint:
        x, y = pg.mouse.get_pos()
        pg.draw.circle(bg, color, (x, y), 10, 0)

    screen.blit(bg, (0, 0))  #畫布0,0在視窗左上角
    print(pg.mouse.get_pos())  #滑鼠x,y座標
    pg.display.update()  #更新視窗
