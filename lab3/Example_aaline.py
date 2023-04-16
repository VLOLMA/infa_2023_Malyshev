import pygame

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((255, 255, 255))

pygame.draw.aaline(screen, (255, 0, 0), (50, 50), (350, 350), 1)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
