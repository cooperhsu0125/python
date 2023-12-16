######################匯入模組######################
import pygame as pg
import sys
import os
from pygame.locals import *

######################載入套件######################


######################定義函式區######################
def roll_bg():
    global roll_y
    roll_y = (roll_y + 10) % bg_y
    screen.blit(img_bg, (0, roll_y - bg_y))
    screen.blit(img_bg, (0, roll_y))


# def a():
#     if


######################初始化設定######################
os.chdir(sys.path[0])
pg.init()
clock = pg.time.Clock()
######################載入圖片######################
img_bg = pg.image.load("space.png")
img_sship = [
    pg.image.load("fighter_M.png"),
    pg.image.load("fighter_L.png"),
    pg.image.load("fighter_R.png"),
]
img = pg.image.load("enemy1.png")
img = pg.image.load("enemy2.png")
######################遊戲視窗設定######################
bg_x = img_bg.get_width()
bg_y = img_bg.get_height()
bg_size = (bg_x, bg_y)
pg.display.set_caption("Galaxy Lancer")
screen = pg.display.set_mode(bg_size)
roll_y = 0
ss_x = bg_x / 2
ss_y = bg_y / 2
ss_wh = img_sship[0].get_width()
ss_hh = img_sship[0].get_height() / 2
######################玩家設定######################

######################主程式######################
while True:
    clock.tick(20)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_F11:
                screen = pg.display.set_mode(bg_size, FULLSCREEN)
            elif event.type == K_ESCAPE:
                screen = pg.display.set_mode(bg_size)
    roll_bg()
    pg.display.update()
