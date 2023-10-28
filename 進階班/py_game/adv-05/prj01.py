import pygame as pg
import random as r
import sys as s
import os


####################定義函式######################
def gophers_update():
    global tick, pos, times, gopher_tick, gopher
    if tick > max_tick:
        times += 1
        new_pos = r.randint(0, 5)
        pos = pos6[new_pos]
        tick = 0

    else:
        tick += 1
    if gopher == gopher2:
        if gopher_tick > gopher_max_tick:
            gopher = gopher1
            gopher_tick = 0
        else:
            gopher_tick += 1
    screen.blit(
        gopher,
        (pos[0] - gopher.get_width() / 2, pos[1] - gopher.get_height() / 2))


def mouse_update():
    global ham, ham_tick
    if ham == ham1:
        if ham_tick > ham_max_tick:
            ham = ham2
            ham_tick = 0
        else:
            ham_tick += 1
    screen.blit(ham, (m_pos[0] - 15, m_pos[1] - 15))


def score_update():
    score_sur = score_font.render(str(score), True, RED)
    screen.blit(score_sur, (10, 10))


def times_update():
    times_sur = score_font.render(str(times), True, RED)
    screen.blit(times_sur, (bg_x - 10 - times_sur.get_width(), 10))


def check_click(m_pos, x_min, y_min, x_max, y_max):
    x_match = x_min < m_pos[0] < x_max
    y_match = y_min < m_pos[1] < y_max
    if x_match and y_match:
        return True
    else:
        return False


def gameover():
    screen.fill(BLACK)
    end_sur = score_font.render(f'Game over your score:{score}', True, RED)
    screen.blit(end_sur, (bg_x / 2 - end_sur.get_width() / 2,
                          bg_y / 2 - end_sur.get_height() / 2))


####################初始化######################
os.chdir(s.path[0])
pg.init()
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
clock = pg.time.Clock()
tick = 0
max_tick = 20
bg_img = '地鼠背景.png'
bg = pg.image.load(bg_img)
bg_x = bg.get_width()
bg_y = bg.get_height()
######################建立視窗######################

screen = pg.display.set_mode((bg_x, bg_y))
pg.display.set_caption('打地鼠')
######################地鼠物件######################
pos6 = [[195, 305], [400, 305], [610, 305], [195, 450], [400, 450], [610, 450]]
pos = pos6[r.randint(0, 5)]
radious = 50
gopher1 = pg.image.load('地鼠.png')
gopher2 = pg.image.load('Gophers2_150.png')
gopher = gopher1
gopher_tick = 0
gopher_max_tick = 2
######################分數物件######################
score = 0
typeface = pg.font.get_default_font()
score_font = pg.font.Font(typeface, 24)
######################滑鼠物件######################
pg.mouse.set_visible(False)
ham1 = pg.image.load('Hammer1.png')
ham2 = pg.image.load('Hammer2.png')
ham = ham2
ham_tick = 0
ham_max_tick = 7
######################次數物件######################
times = 0
times_max = 100
typeface = pg.font.get_default_font()
times_font = pg.font.Font(typeface, 24)
######################聲音物件######################
pg.mixer.music.load('hit.mp3')
######################循環偵測######################
while True:
    clock.tick(20)
    m_pos = pg.mouse.get_pos()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            s.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            ham = ham1
            if check_click(m_pos, pos[0] - gopher.get_width() / 2,
                           pos[1] - gopher.get_height() / 2,
                           pos[0] + gopher.get_width() / 2,
                           pos[1] + gopher.get_height() / 2):
                tick = max_tick + 1
                score += 1
                gopher = gopher2
                pg.mixer.music.play()

    if times >= times_max:
        gameover()
    else:
        screen.blit(bg, (0, 0))
        gophers_update()
        score_update()
        times_update()
        mouse_update()
    pg.display.update()