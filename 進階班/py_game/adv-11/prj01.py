######################匯入模組######################
import pygame as pg
import sys
import os
from pygame.locals import *


######################物件類別######################
class Missile:
    def __init__(self, x, y, image, shift):
        self.x = x
        self.y = y
        self.image = image
        self.active = False
        self.shift = shift

    def launch(self, x, y):
        if not self.active:
            self.x = x
            self.y = y
            self.active = True

    def move(self):
        if self.active:
            self.y -= self.shift
            if self.y < 0:
                self.active = False

    def draw(self, screen):
        if self.active:
            screen.blit(self.image, (self.x, self.y))


######################載入套件######################


######################定義函式區######################
def roll_bg():
    global roll_y
    roll_y = (roll_y + 10) % bg_y
    screen.blit(img_bg, (0, roll_y - bg_y))
    screen.blit(img_bg, (0, roll_y))


def starship_move():
    global ss_x, ss_y, ss_wh, ss_hh, ss_img, burn_shift
    key = pg.key.get_pressed()
    ss_img = 0
    if key[pg.K_UP]:
        ss_y -= 20
        ss_img = 0
    if key[pg.K_DOWN]:
        ss_y += 20
        ss_img = 0
    if key[pg.K_LEFT]:
        ss_x -= 20
        ss_img = 1
    if key[pg.K_RIGHT]:
        ss_x += 20
        ss_img = 2
    ss_hh = img_sship[ss_img].get_height() / 2
    ss_wh = img_sship[ss_img].get_width() / 2
    if ss_y < ss_hh:
        ss_y = ss_hh
    if ss_y > bg_y - ss_hh:
        ss_y = bg_y - ss_hh
    if ss_x < ss_wh:
        ss_x = ss_wh
    if ss_x > bg_x - ss_wh:
        ss_x = bg_x - ss_wh
    burn_shift = (burn_shift + 2) % 10
    screen.blit(img_burn, [ss_x - burn_w / 2, ss_y + burn_h + burn_shift])
    screen.blit(img_sship[ss_img], [ss_x - ss_wh, ss_y - ss_hh])


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
img_burn = pg.image.load("starship_burner.png")
img_weapon = pg.image.load("bullet.png")
######################遊戲視窗設定######################
bg_x = img_bg.get_width()
bg_y = img_bg.get_height()
bg_size = (bg_x, bg_y)
pg.display.set_caption("Galaxy Lancer")
screen = pg.display.set_mode(bg_size)
roll_y = 0
ss_x = bg_x / 2
ss_y = bg_y / 2
ss_wh = img_sship[0].get_width() / 2
ss_hh = img_sship[0].get_height() / 2
ss_img = 0
######################玩家設定######################
burn_shift = 0
burn_w, burn_h = img_burn.get_rect().size
######################飛彈設定######################
msl_wh = img_weapon.get_width() / 2
msl_hh = img_weapon.get_height() / 2
msl_shift = 30
MISSILE_MAX = 10
missiles = [Missile(0, 0, img_weapon, 30) for _ in range(MISSILE_MAX)]
msl_cd = 0
msl_cd_max = 10
######################主程式######################
while True:
    clock.tick(100)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_F11:
                screen = pg.display.set_mode(bg_size, FULLSCREEN)
            elif event.type == K_ESCAPE:
                screen = pg.display.set_mode(bg_size)
            if event.key == K_SPACE and msl_cd == 0:
                for missile in missiles:
                    if not missile.active:
                        missile.launch(ss_x - msl_wh, ss_y - msl_hh)
                        msl_cd = msl_cd_max
                        break

    roll_bg()
    starship_move()
    msl_cd = max(0, msl_cd - 1)
    for missile in missiles:
        missile.move()
        missile.draw(screen)
    pg.display.update()
