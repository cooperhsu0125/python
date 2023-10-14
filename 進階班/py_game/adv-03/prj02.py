######################匯入模組######################
import pygame as pg
import random as r
import sys as s
import os


####################定義函式######################
def gophers_update():
    global tick, pos
    if tick > max_tick:
        new_pos = r.randint(0, 5)
        pos = pos6[new_pos]
        tick = 0
    else:
        tick += 1
    pg.draw.circle(screen, BLUE, pos, 50)


####################初始化######################
os.chdir(s.path[0])
pg.init()
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
clock = pg.time.Clock()
tick = 0
max_tick = 20
######################建立視窗######################
bg_x = 600
bg_y = 400
screen = pg.display.set_mode((bg_x, bg_y))
pg.display.set_caption('打地鼠')
######################背景物件######################
bg = pg.Surface([bg_x, bg_y])
bg.fill(BLACK)
######################地鼠物件######################
pos6 = [[200, 200], [300, 200], [400, 200], [200, 300], [300, 300], [400, 300]]
pos = pos6[r.randint(0, 5)]
######################分數物件######################

######################滑鼠物件######################

######################循環偵測######################
while True:
    clock.tick(-1)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            s.exit()
    screen.blit(bg, (0, 0))
    gophers_update()
    pg.display.update()