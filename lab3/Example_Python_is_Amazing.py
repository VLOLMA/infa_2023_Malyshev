import pygame
from pygame.draw import circle, rect, line, polygon

pygame.init()

FPS = 30
screen = pygame.display.set_mode((927, 769))
screen.fill((255, 255, 255))

circle(screen, (255, 255, 0), (200, 200), 100)
circle(screen, (0, 0, 0), (200, 200), 100, 1)
circle(screen, (255, 0, 0), (150, 180), 20)
circle(screen, (0, 0, 0), (150, 180), 20, 1)
circle(screen, (0, 0, 0), (150, 180), 8)
circle(screen, (255, 0, 0), (250, 180), 15)
circle(screen, (0, 0, 0), (250, 180), 15, 1)
circle(screen, (0, 0, 0), (250, 180), 7)
rect(screen, (0, 0, 0), (150, 250, 100, 20))
polygon(screen, (0, 0, 0), [(103,116), (183,166),
                            (178,174), (97,124)])
polygon(screen, (0, 0, 0), [(220,165), (300,135),
                            (303,144), (223,174)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
