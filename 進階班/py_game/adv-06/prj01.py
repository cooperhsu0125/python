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
    global ds_y, ds_index, jumpstate, jumpvalue,ds_center_x,ds_center_y
    if jumpstate:
        if ds_y >= LIMIL_LOW:
            jumpvalue = -jump_height
        if ds_y <= 0:
            jumpvalue = jump_height
        ds_y += jumpvalue
        jumpvalue+=1
        
        if ds_y >= LIMIL_LOW:
            jumpstate = False
            ds_y = LIMIL_LOW
    ds_index = (ds_index - 1) % len(img_dino)
    ds_center_x=ds_x+img_dino[ds_index].get_width()/2
    ds_center_y=ds_y+img_dino[ds_index].get_height()/2
    screen.blit(img_dino[ds_index], (ds_x, ds_y))


def cac_move():
    global cacti_x,score,cacti_center_x,cacti_center_y
    cacti_x = (cacti_x - cacti_shift) % (bg_x + 10)
    cacti_center_x=cacti_x+img_cacti.get_width()/2
    cacti_center_y=cacti_y+img_cacti.get_height()/2
    screen.blit(img_cacti, (cacti_x, cacti_y))
    if cacti_x<=0:
        score+=1
def score_update():
    score_sur = score_font.render(str(score), True, (0,0,0))
    screen.blit(score_sur, (10, 10))
def is_hitted(x1,y1,x2,y2,r):
    if ((x1-x2)**2+(y1-y2)**2)<(r*r):
        return True
    else:
        return False
def gameover():
    screen.blit(img_gg, (bg_x / 2 - gg_w / 2,
                          bg_y / 2 - gg_h / 2))


####################初始化######################
os.chdir(s.path[0])
pg.init()
LIMIL_LOW = 140
clock = pg.time.Clock()
####################載入圖片物件######################
img = pg.image.load('bg.png')
img_dino = pg.image.load('小恐龍1.png'), pg.image.load('小恐龍2.png')
img_cacti = pg.image.load('cacti.png')
img_gg=pg.image.load('gameover.png')
bg_x = img.get_width()
bg_y = img.get_height()
bg_roll_x = 0

######################建立視窗######################
screen = pg.display.set_mode([bg_x, bg_y])
pg.display.set_caption('dino')
######################分數物件######################
score=0
typeface=pg.font.get_default_font()
score_font=pg.font.Font(typeface,36)
######################恐龍物件######################
ds_x = 50
ds_y = LIMIL_LOW
ds_index = 0
jumpstate = False
jumpvalue = 0
jump_height = 13
ds_center_x=ds_x+img_dino[0].get_width()/2
ds_center_y=ds_y+img_dino[0].get_height()/2
ds_detect_r=min(img_dino[0].get_width(),img_dino[0].get_height())/2
######################仙人掌物件######################
cacti_x = bg_x + 10
cacti_y = LIMIL_LOW
cacti_shift = 10
cacti_center_x=cacti_x+img_cacti.get_width()/2
cacti_center_y=cacti_y+img_cacti.get_height()/2
cacti_detect_r=max(img_cacti.get_width(),img_cacti.get_height())/2-15
######################遊戲結束物件######################
gg=False
gg_w=img_gg.get_width()
gg_h=img_gg.get_height()
######################循環偵測######################
while True:
    clock.tick(20)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            s.exit()
        if event.type == pg.KEYDOWN:
            if event.key == K_SPACE and ds_y <= LIMIL_LOW:
                jumpstate = True
    
    if gg:
        gameover()

    else:
        bg_update()
        cac_move()
        score_update()
        ds_move()
        gg=is_hitted(ds_center_x,ds_center_y,cacti_center_x,cacti_center_y,(ds_detect_r+cacti_detect_r))
        pg.draw.circle(screen,(255,0,0),(int(cacti_center_x),int(cacti_center_y)),cacti_detect_r+ds_detect_r,1)
    pg.display.update()