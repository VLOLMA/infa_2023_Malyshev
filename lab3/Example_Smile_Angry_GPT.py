import pygame
from pygame.draw import *

# Initialize Pygame
pygame.init()

# Set the FPS and create the screen
FPS = 30
screen = pygame.display.set_mode((400, 400))

# Fill the screen with a gray background
screen.fill((128, 128, 128))

# Draw the smiley face
circle(screen, (255, 0, 0), (200, 200), 100)
circle(screen, (0, 0, 0), (200, 200), 100, 1)
circle(screen, (255, 255, 255), (150, 180), 20)
circle(screen, (0, 0, 0), (150, 180), 20, 1)
circle(screen, (0, 0, 0), (150, 180), 8)
circle(screen, (255, 255, 255), (250, 180), 17)
circle(screen, (0, 0, 0), (250, 180), 17, 1)
circle(screen, (0, 0, 0), (250, 180), 7)
rect(screen, (0, 0, 0), (150, 250, 100, 20))

# Draw angry eyebrows
polygon(screen, (0, 0, 0), [(140, 150), (170, 140), (190, 150), (140, 150)])
polygon(screen, (0, 0, 0), [(210, 150), (230, 140), (260, 150), (210, 150)])

# Update the display and set up the game clock
pygame.display.update()
clock = pygame.time.Clock()

# Run the game loop
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

# Quit Pygame and close the window
pygame.quit()

