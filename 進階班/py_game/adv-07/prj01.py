######################匯入模組######################
import pygame as pg
import sys as s
import os
from pygame.locals import *
import random as r


####################定義函式######################
def bg_update():
    global bg_roll_x
    bg_roll_x = (bg_roll_x - 10) % bg_x
    screen.blit(img, (bg_roll_x - bg_x, 0))
    screen.blit(img, (bg_roll_x, 0))


def ds_move():
    global ds_y, ds_index, jumpstate, jumpvalue,ds_center_x,ds_center_y,ds_detect_r
    if dino_down:
        jumpstate=False
        ds_y=LIMIL_LOW+20
    if jumpstate and not dino_down:
        if ds_y >= LIMIL_LOW:
            jumpvalue = -jump_height
        if ds_y <= 0:
            jumpvalue = jump_height
        ds_y += jumpvalue
        jumpvalue+=1
        
        if ds_y >= LIMIL_LOW:
            jumpstate = False
            ds_y = LIMIL_LOW
    ds_index = (ds_index - 1) % len(ds_show)
    ds_center_x=ds_x+ds_show[ds_index].get_width()/2
    ds_center_y=ds_y+ds_show[ds_index].get_height()/2
    ds_detect_r=min(ds_show[0].get_width(),ds_show[0].get_height())/2
    screen.blit(ds_show[ds_index], (ds_x, ds_y))


def cac_move():
    global cacti_x,score,cacti_center_x,cacti_center_y,enemy
    cacti_x = (cacti_x - cacti_shift) % (bg_x + 10)
    cacti_center_x=cacti_x+img_cacti.get_width()/2
    cacti_center_y=cacti_y+img_cacti.get_height()/2
    screen.blit(img_cacti, (cacti_x, cacti_y))
    if cacti_x<=0:
        score+=1
        enemy=r.randint(0,1)
def ptera_move():
    global ptera_x,ptera_index,ptera_center_x,ptera_center_y,score,enemy
    ptera_x=(ptera_x-ptera_shift)%(bg_x+10)
    ptera_index=(ptera_index-1)%len(img_ptera)
    ptera_center_x=ptera_x+img_ptera[ptera_index].get_width()/2
    ptera_center_y=ptera_y+img_ptera[ptera_index].get_height()/2
    screen.blit(img_ptera[ptera_index],(ptera_x,ptera_y))
    if ptera_x < 0:
        score+=1
        enemy=r.randint(0,1)

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
PTERA_LIMIT_LOW=110
clock = pg.time.Clock()
enemy=r.randint(0,1)
####################載入圖片物件######################
img = pg.image.load('bg.png')
img_dino = [pg.image.load('小恐龍1.png'), pg.image.load('小恐龍2.png')]
img_dino_down=[pg.image.load('小恐龍蹲下1.png'),pg.image.load('小恐龍蹲下2.png')]
img_cacti = pg.image.load('cacti.png')
img_ptera=[pg.image.load('翼龍飛飛1.png'),pg.image.load('翼龍飛飛2.png')]
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
ds_show=img_dino
dino_down=False
######################仙人掌物件######################
cacti_x = bg_x + 10
cacti_y = LIMIL_LOW
cacti_shift = 10
cacti_center_x=cacti_x+img_cacti.get_width()/2
cacti_center_y=cacti_y+img_cacti.get_height()/2
cacti_detect_r=max(img_cacti.get_width(),img_cacti.get_height())/2-15
######################翼龍物件######################
ptera_x=bg_x+10
ptera_y=PTERA_LIMIT_LOW
ptera_index=0
ptera_shift=10
ptera_center_x=ptera_x+img_ptera[0].get_width()/2
ptera_center_y=ptera_y+img_ptera[0].get_height()/2
ptera_detect_r=max(img_ptera[0].get_width(),img_ptera[0].get_height())/2-10
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
            elif event.key == K_DOWN:
                dino_down=True
                ds_show=img_dino_down
        
    
            if event.key==K_RETURN:
                score=0
                gg=False
                cacti_x = bg_x + 10
                ptera_x_x = bg_x + 10
                ds_y = LIMIL_LOW
                jumpstate=False
        if event.type == pg.KEYUP:
            dino_down=False
            ds_show=img_dino
            ds_y=LIMIL_LOW

    if gg:
        gameover()
    else:
        bg_update()
        score_update()
        ds_move()
        if enemy==0:
            cac_move()
            gg=is_hitted(ds_center_x,ds_center_y,cacti_center_x,cacti_center_y,(ds_detect_r+cacti_detect_r))
            pg.draw.circle(screen,(255,0,0),(int(cacti_center_x),int(cacti_center_y)),cacti_detect_r+ds_detect_r,1)
        else:
            ptera_move()
            gg=is_hitted(ds_center_x,ds_center_y,ptera_center_x,ptera_center_y,(ds_detect_r+ptera_detect_r))
            pg.draw.circle(screen,(255,0,0),(int(ptera_center_x),int(ptera_center_y)),ptera_detect_r+ds_detect_r,1)

    pg.display.update()