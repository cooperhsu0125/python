######################匯入模組######################
import pygame as pg
import sys as s
import os
from pygame.locals import *


####################定義函式######################
def bg_update():
    global bg_roll_x
    bg_roll_x = (bg_roll_x - 10) % bg_x
    screen.blit(img, (bg_roll_x - bg_x, 0))
    screen.blit(img, (bg_roll_x, 0))


def ds_move():
    global ds_y, ds_index, jumpstate, jumpvalue
    if jumpstate:
        if ds_y >= LIMIL_LOW:
            jumpvalue = -jump_height
        if ds_y <= 0:
            jumpvalue = jump_height
        ds_y += jumpvalue
        if ds_y >= LIMIL_LOW:
            jumpstate = False
            ds_y = LIMIL_LOW
    ds_index = (ds_index - 1) % len(img_dino)
    screen.blit(img_dino[ds_index], (ds_x, ds_y))


####################初始化######################
os.chdir(s.path[0])
pg.init()
LIMIL_LOW = 140
clock = pg.time.Clock()
####################載入圖片物件######################
img = pg.image.load('bg.png')
img_dino = [pg.image.load('小恐龍1.png'), pg.image.load('小恐龍2.png')]
bg_x = img.get_width()
bg_y = img.get_height()
bg_roll_x = 0
######################建立視窗######################
screen = pg.display.set_mode([bg_x, bg_y])
pg.display.set_caption('dino')
######################分數物件######################

######################恐龍物件######################
ds_x = 50
ds_y = LIMIL_LOW
ds_index = 0
jumpstate = False
jumpvalue = 10
jump_height = 13
######################仙人掌物件######################

######################循環偵測######################
while True:
    clock.tick(-1)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            s.exit()
        if event.type == pg.KEYDOWN:
            if event.key == K_SPACE and ds_y <= LIMIL_LOW:
                jumpstate = True
    bg_update()
    ds_move()
    pg.display.update()