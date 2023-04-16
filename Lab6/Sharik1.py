import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_ball():
    global x, y, r
    x = randint(0,1200)
    y = randint(0,900)
    r = randint(30,50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

def click(event):
    print(event.pos, countgoal)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
countgoal = 0

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            distance = ((event.pos[0] - x)**2 + (event.pos[1] - y)**2)**0.5
            if distance < r:
                countgoal +=1
            else:
                countgoal -=1
            click(event) # передаем объект event в функцию click()
    new_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()