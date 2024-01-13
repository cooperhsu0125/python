######################匯入模組######################
import pygame as pg
import random as r
import sys
import os
from pygame.locals import *
from typing import List


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


class Enemy:
    def __init__(self, x, y, image, shift, burn_img):
        self.x = x
        self.y = y
        self.image = image
        self.active = True
        self.shift = shift
        self.wh = image.get_width() // 2
        self.hh = image.get_height() // 2
        self.burn_img = burn_img
        self.burn_shift = 0
        self.burn_w, self.burn_h = burn_img.get_rect().size
        self.EXPLODE: int = 0
        self.hit = False

    def move(self):
        if self.active:
            self.y += self.shift
            if self.y > bg_y:
                self.reset(*create_enemy(), self.shift)

    def draw(self, screen):
        if self.active:
            self.burn_shift = (self.burn_shift + 2) % 17
            screen.blit(
                self.burn_img,
                [self.x - self.burn_w / 2, self.y - self.burn_h - self.burn_shift],
            )
            screen.blit(self.image, (self.x - self.wh, self.y - self.hh))

    def reset(self, x, y, image, shift):
        self.x = x
        self.y = y
        self.image = image
        self.active = True
        self.shift = shift
        self.wh = image.get_width() // 2
        self.hh = image.get_height() // 2
        self.EXPLODE = 0
        self.hit = False


class FastMissle(Missile):
    def __init__(self, x, y, image, shift):
        super().__init__(x, y, image, shift)
        self.shift += 100


class PiercingMissle(Missile):
    def __init__(self, x, y, image, shift):
        super().__init__(x, y, image, shift)


class Powerup:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.wh = image.get_width() / 2
        self.hh = image.get_height() / 2
        self.active = True
        self.type = r.choice([FastMissle, PiercingMissle, Missile])
        self.power = r.randint(1, 3)

    def draw(self, screen):
        if self.active:
            self.y += 5
            screen.blit(img_powerup, (self.x - self.wh, self.y - self.hh))
            if self.y > bg_y:
                self.active = False

    def reset(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.wh = image.get_width() / 2
        self.hh


######################載入套件######################


######################定義函式區######################
def roll_bg():
    global roll_y
    roll_y = (roll_y + 10) % bg_y
    screen.blit(img_bg, (0, roll_y - bg_y))
    screen.blit(img_bg, (0, roll_y))


def starship_move():
    global ss_x, ss_y, ss_wh, ss_hh, ss_img, burn_shift, ss_invisible
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
    ss_invisible = max(0, ss_invisible - 1)
    if ss_invisible % 2 == 0:
        screen.blit(img_burn, [ss_x - burn_w / 2, ss_y + burn_h + burn_shift])
        screen.blit(img_sship[ss_img], [ss_x - ss_wh, ss_y - ss_hh])


def create_enemy():
    emy_img = r.choice(emy_show)
    emy_wh = emy_img.get_width() // 2  # 敵機寬度一半
    emy_x = r.randint(emy_wh, bg_x - emy_wh)  # 起始x位置
    emy_y = r.randint(-bg_y, -emy_wh)  # 起始y位置
    return emy_x, emy_y, emy_img


def is_hit(x1, y1, x2, y2, r):
    if ((x1 - x2) ** 2 + (y1 - y2) ** 2) < (r * r):
        return True
    else:
        return False


def score_update():
    score_sur = score_font.render(str(score), True, (255, 255, 255))
    screen.blit(score_sur, (10, 10))


def draw_explode(enemy: Enemy):
    if 0 < enemy.EXPLODE < 6:
        exp_w, exp_h = img_explode[enemy.EXPLODE].get_rect().size
        screen.blit(
            img_explode[enemy.EXPLODE], [enemy.x - exp_w / 2, enemy.y - exp_h / 2]
        )
        enemy.EXPLODE += 1


def shield_update():
    shield_w = img_shield.get_width() * ss_shield / 100
    shield_h = img_shield.get_height()
    screen.blit(img_shield, [0, bg_y - 40], [0, 0, shield_w, shield_h])


def gameover():
    screen.blit(
        img_gg, (bg_x / 2 - img_gg.get_width() / 2, bg_y / 2 - img_gg.get_height() / 2)
    )


######################初始化設定######################
os.chdir(sys.path[0])
pg.init()
clock = pg.time.Clock()
gg = False
######################載入圖片######################
img_bg = pg.image.load("space.png")
img_sship = [
    pg.image.load("fighter_M.png"),
    pg.image.load("fighter_L.png"),
    pg.image.load("fighter_R.png"),
]
img_enemy = pg.image.load("enemy1.png")
img_enemy2 = pg.image.load("enemy2.png")
img_burn = pg.image.load("starship_burner.png")
img_weapon = pg.image.load("bullet.png")
img_emy_burn = pg.transform.rotate(img_burn, 180)
img_explode = [
    None,
    pg.image.load("explosion1.png"),
    pg.image.load("explosion2.png"),
    pg.image.load("explosion3.png"),
    pg.image.load("explosion4.png"),
    pg.image.load("explosion5.png"),
    pg.image.load,
]
img_shield = pg.image.load("shield.png")
img_gg = pg.image.load("gameover.png")
img_powerup = pg.image.load("Ammo.png")
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
ss_invisible = 0
ss_shield = 100

######################飛彈設定######################
msl_wh = img_weapon.get_width() / 2
msl_hh = img_weapon.get_height() / 2
msl_shift = 30
MISSILE_MAX = 100
missiles = [PiercingMissle(0, 0, img_weapon, msl_shift) for _ in range(MISSILE_MAX)]
msl_cd = 0
msl_cd_max = 0
######################敵機設定######################
emy_show = [img_enemy, img_enemy2]
emy_shift = 10
emy_list: List[Enemy] = []
emy_num = 5
for i in range(emy_num):
    emy_list.append(Enemy(*create_enemy(), emy_shift, img_emy_burn))  # 建立敵機
######################分數設定######################
score = 0
typeface = pg.font.get_default_font()
score_font = pg.font.Font(typeface, 36)
######################音樂設定######################
pg.mixer.music.load("hit.mp3")
######################道具列表######################
powerups: List[Powerup] = []
######################主程式######################
while True:
    clock.tick(60)
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
    if gg:
        gameover()
    else:
        roll_bg()
        starship_move()
        msl_cd = max(0, msl_cd - 1)
        for missile in missiles:
            missile.move()
            missile.draw(screen)
        for enemy in emy_list:
            enemy.move()
            enemy.draw(screen)
            draw_explode(enemy)
            for missile in missiles:
                if missile.active and is_hit(
                    enemy.x, enemy.y, missile.x, missile.y, msl_wh + enemy.wh
                ):
                    if enemy.hit:
                        break
                    enemy.hit = True
                    if not isinstance(missile, PiercingMissle):
                        missile.active = False

                    enemy.active = False
                    score += 1
                    enemy.EXPLODE = 1
                    pg.mixer.music.play()
                    powerups.append(Powerup(enemy.x, enemy.y, img_powerup))
                    break
            if not enemy.active and enemy.EXPLODE == 6:
                enemy.reset(*create_enemy(), emy_shift)
            if (
                enemy.active
                and is_hit(ss_x, ss_y, enemy.x, enemy.y, ss_wh + enemy.wh)
                and ss_invisible == 0
            ):
                ss_invisible = 40
                score -= 1
                ss_shield -= 20
            if ss_shield < 0:
                gg = True
                break
        for powerup in powerups:
            powerup.draw(screen)
            if not powerup.active:
                powerups.remove(powerup)
        score_update()
        shield_update()
    pg.display.update()
