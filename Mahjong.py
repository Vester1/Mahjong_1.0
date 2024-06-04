import sys
import json
import pygame as pg
from pygame.color import *
import random
pg.init()

clock = pg.time.Clock()
GREEN = (14, 122, 72)
LIGHT_GREEN = (118, 191, 74)
CARDS_img_h = ['for_M/card_hard/card1.png',
               'for_M/card_hard/card2.png',
               'for_M/card_hard/card3.png',
               'for_M/card_hard/card4.png',
               'for_M/card_hard/card5.png',
               'for_M/card_hard/card6.png',
               'for_M/card_hard/card7.png',
               'for_M/card_hard/card8.png',
               'for_M/card_hard/card9.png',
               'for_M/card_hard/card10.png',
               'for_M/card_hard/card11.png',
               'for_M/card_hard/card12.png',
               'for_M/card_hard/card13.png',
               'for_M/card_hard/card14.png',
               'for_M/card_hard/card15.png'
               ] * 6

CARDS_img_m = ['for_M/card_med/card1_med.png',
               'for_M/card_med/card2_med.png',
               'for_M/card_med/card3_med.png',
               'for_M/card_med/card4_med.png',
               'for_M/card_med/card5_med.png',
               'for_M/card_med/card6_med.png',
               'for_M/card_med/card7_med.png',
               'for_M/card_med/card8_med.png',
               'for_M/card_med/card9_med.png',
               'for_M/card_med/card10_med.png',
               'for_M/card_med/card11_med.png',
               'for_M/card_med/card12_med.png',
               'for_M/card_med/card13_med.png',
               'for_M/card_med/card14_med.png',
               'for_M/card_med/card15_med.png'
               ] * 2
for _ in range(2):
    CARDS_img_m.append('for_M/card_med/card1_med.png')
    CARDS_img_m.append('for_M/card_med/card3_med.png')
    CARDS_img_m.append('for_M/card_med/card5_med.png')
    CARDS_img_m.append('for_M/card_med/card8_med.png')
    CARDS_img_m.append('for_M/card_med/card14_med.png')

CARDS_img_easy = [
                 'for_M/card_easy/card1_easy.png',
                 'for_M/card_easy/card2_easy.png',
                 'for_M/card_easy/card3_easy.png',
                 'for_M/card_easy/card5_easy.png',
                 'for_M/card_easy/card6_easy.png',
                 'for_M/card_easy/card7_easy.png',
                 'for_M/card_easy/card9_easy.png',
                 'for_M/card_easy/card10_easy.png',
                 'for_M/card_easy/card12_easy.png',
                 'for_M/card_easy/card13_easy.png',
                 'for_M/card_easy/card14_easy.png',
                 'for_M/card_easy/card15_easy.png'
                 ] * 2
#CARDS_img_easy = ['for_M/card_easy/card1_easy.png'] * 4

CARDS_img = None
CARDS_LIST = []
TARGET = 0
target_list = []
score = 0
difficult = 0
get_dif = False
get_choice = False
stop = False
font1 = pg.font.SysFont('Comic Sans MS', 25)
font2 = pg.font.SysFont('Comic Sans MS', 110)
font3 = pg.font.SysFont('Comic Sans MS', 70)
font4 = pg.font.SysFont('Comic Sans MS', 65)

counter = font1.render(f'Попыток: {str(score)}', True, THECOLORS['black'])
greetings = font2.render('Mahjong', True, LIGHT_GREEN)
greetings_rect = greetings.get_rect(center=(565, 50))
difficulty = font3.render('Выберите уровень сложности', True, THECOLORS['black'])
difficulty_rect = difficulty.get_rect(center=(565, 150))
dif1 = font3.render('Легкий', True, THECOLORS['black'])
dif1_rect = dif1.get_rect(center=(150, 400))
dif2 = font3.render('Средний', True, THECOLORS['black'])
dif2_rect = dif2.get_rect(center=(550, 400))
dif3 = font3.render('Сложный', True, THECOLORS['black'])
dif3_rect = dif3.get_rect(center=(950, 400))
win_next = font3.render('Далее', True, THECOLORS['black'])
win_next_rect = win_next.get_rect(center=(565, 500))
record1_text = font4.render('Вы побили прошлый рекорд!', True, THECOLORS['black'])
level_passed_text = font4.render('Уровень пройден!', True, THECOLORS['black'])


sc = pg.display.set_mode((1130, 630))
pg.display.set_caption('Mahjong')
sc.fill(GREEN)
pg.display.update()


class Card(pg.sprite.Sprite):
    def __init__(self, surf, x, y, shirt):
        pg.sprite.Sprite.__init__(self)
        self.number = surf
        self.shirt = pg.image.load(shirt)
        self.image = pg.image.load(surf)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.hide = True

    def draw(self):
        if self.hide:
            sc.blit(self.shirt, self.rect)
        else:
            sc.blit(self.image, self.rect)

    def click(self, x, y):
        return self.rect.collidepoint(x, y)


def drawing(n):
    pg.time.wait(n)
    sc.fill(GREEN)
    for card in CARDS_LIST:
        card.draw()
    pg.display.update()


def calculation(difficult):
    if difficult == 'hard':
        CARDS_img = CARDS_img_h.copy()
        pg.display.set_caption('Mahjong. Level hard')
        x = 50
        y = 45
        for _ in range(6):
            for _ in range(15):
                ind = random.randint(0, len(CARDS_img) - 1)
                im = CARDS_img[ind]
                card = Card(im, x, y, 'for_M/card_hard/shirt.png')
                CARDS_LIST.append(card)
                CARDS_img.remove(im)
                x += 70
                drawing(25)
            x = 50
            y += 94

    elif difficult == 'medium':
        CARDS_img = CARDS_img_m.copy()
        pg.display.set_caption('Mahjong. Level medium')
        x = 85
        y = 40
        for _ in range(4):
            for _ in range(10):
                ind = random.randint(0, len(CARDS_img) - 1)
                im = CARDS_img[ind]
                card = Card(im, x, y, 'for_M/card_med/shirt_med.png')
                CARDS_LIST.append(card)
                CARDS_img.remove(im)
                x += 100
                drawing(50)
            x = 85
            y += 140

    elif difficult == 'easy':
        CARDS_img = CARDS_img_easy.copy()
        pg.display.set_caption('Mahjong. Level easy')
        x = 60
        y = 40
        for _ in range(3):
            for _ in range(8):
                ind = random.randint(0, len(CARDS_img) - 1)
                im = CARDS_img[ind]
                card = Card(im, x, y, 'for_M/card_easy/shirt_easy.png')
                CARDS_LIST.append(card)
                CARDS_img.remove(im)
                x += 130
                drawing(70)
            x = 60
            y += 185


def get_diff():
    pg.display.set_caption('Mahjong')
    global get_dif
    global difficult
    sc.fill(GREEN)
    sc.blit(greetings, greetings_rect)
    sc.blit(difficulty, difficulty_rect)
    sc.blit(dif1, dif1_rect)
    sc.blit(dif2, dif2_rect)
    sc.blit(dif3, dif3_rect)
    pg.display.update()
    while not get_dif:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                sys.exit()
            elif i.type == pg.MOUSEBUTTONDOWN and i.button == 1:
                if dif1_rect.collidepoint(i.pos):
                    get_dif = True
                    difficult = 'easy'
                elif dif2_rect.collidepoint(i.pos):
                    get_dif = True
                    difficult = 'medium'
                elif dif3_rect.collidepoint(i.pos):
                    get_dif = True
                    difficult = 'hard'


get_diff()
calculation(difficult)
start_ticks = pg.time.get_ticks()

while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
        elif i.type == pg.MOUSEBUTTONDOWN and i.button == 1:
            x, y = i.pos
            for c in CARDS_LIST:
                if c.click(x, y):
                    if c.hide:
                        c.hide = False
                        TARGET += 1

    sc.fill(GREEN)
    sc.blit(counter, (0, 0))
    stopwatch_ticks = pg.time.get_ticks() - start_ticks
    millis = stopwatch_ticks // 100 % 10
    seconds = int(stopwatch_ticks / 1000 % 60)
    minutes = int(stopwatch_ticks / 60000 % 24)
    out = f'{minutes:02d}:{seconds:02d}:{millis}'
    stopwatch = font1.render(out, True, THECOLORS['black'])
    sc.blit(stopwatch, (1000, 0))
    pg.display.update([(0, 0, 200, 40), (1000, 0, 200, 40)])
    for card in CARDS_LIST:
        card.draw()
    pg.display.update()

    if TARGET >= 2:
        score += 1
        for c in CARDS_LIST:
            if not c.hide:
                target_list.append(c)

        if target_list[0].number == target_list[1].number:
            CARDS_LIST.remove(target_list[0])
            CARDS_LIST.remove(target_list[1])
        target_list.clear()
        stop = True
        last = pg.time.get_ticks()
        while stop:
            stopwatch_ticks = pg.time.get_ticks() - start_ticks
            millis = stopwatch_ticks // 100 % 10
            seconds = int(stopwatch_ticks / 1000 % 60)
            minutes = int(stopwatch_ticks / 60000 % 24)
            out = f'{minutes:02d}:{seconds:02d}:{millis}'
            stopwatch = font1.render(out, True, THECOLORS['black'])
            sc.fill(GREEN)
            sc.blit(stopwatch, (1000, 0))
            pg.display.update((1000, 0, 200, 40))
            now = pg.time.get_ticks()
            if now - last >= 300:
                stop = False
        TARGET = 0
        for c in CARDS_LIST:
            c.hide = True

    if len(CARDS_LIST) == 0:
        sc.fill(GREEN)
        with open('data.json', encoding='UTF-8') as file:
            data = json.load(file)
            if difficult == 'easy':
                if not data['record_score_easy'] or data['record_score_easy'] > score:
                    record2_text = font4.render(f'Ваш прошлый рекорд: {data["record_score_easy"]}', True, THECOLORS['black'])
                    sc.blit(record1_text, record1_text.get_rect(center=(565, 200)))
                    sc.blit(record2_text, record2_text.get_rect(center=(565, 300)))
                    data['record_score_easy'] = score
                    record3_text = font4.render(f'Ваш нынешний рекорд: {score}', True, THECOLORS['black'])
                    sc.blit(record3_text, record3_text.get_rect(center=(565, 400)))
                    pg.display.update()
            elif difficult == 'medium':
                if not data['record_score_med'] or data['record_score_med'] > score:
                    record2_text = font4.render(f'Ваш прошлый рекорд: {data["record_score_med"]}', True, THECOLORS['black'])
                    sc.blit(record1_text, record1_text.get_rect(center=(565, 200)))
                    sc.blit(record2_text, record2_text.get_rect(center=(565, 300)))
                    data['record_score_med'] = score
                    record3_text = font4.render(f'Ваш нынешний рекорд: {score}', True, THECOLORS['black'])
                    sc.blit(record3_text, record3_text.get_rect(center=(565, 400)))
                    pg.display.update()
            elif difficult == 'hard':
                if not data['record_score_hard'] or data['record_score_hard'] > score:
                    record2_text = font4.render(f'Ваш прошлый рекорд: {data["record_score_hard"]}', True, THECOLORS['black'])
                    sc.blit(record1_text, record1_text.get_rect(center=(565, 200)))
                    sc.blit(record2_text, record2_text.get_rect(center=(565, 300)))
                    data['record_score_hard'] = score
                    record3_text = font4.render(f'Ваш нынешний рекорд: {score}', True, THECOLORS['black'])
                    sc.blit(record3_text, record3_text.get_rect(center=(565, 400)))
                    pg.display.update()
        with open('data.json', 'w', encoding='UTF-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

        get_dif = False
        get_choice = False
        sc.blit(level_passed_text, level_passed_text.get_rect(center=(565, 100)))
        sc.blit(win_next, win_next_rect)
        pg.display.update()
        while not get_choice:
            for i in pg.event.get():
                if i.type == pg.QUIT:
                    sys.exit()
                elif i.type == pg.MOUSEBUTTONDOWN and i.button == 1:
                    if win_next_rect.collidepoint(i.pos):
                        get_choice = True

    if get_choice:
        get_diff()
        calculation(difficult)
        get_choice = False
        score = 0
        start_ticks = pg.time.get_ticks()

    counter = font1.render(f'Ходов: {str(score)}', True, THECOLORS['black'])
    clock.tick(40)
