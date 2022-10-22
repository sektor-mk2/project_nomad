import sys
import pygame
from pygame.locals import *

MAX_FPS = 60

pygame.init()
main_display = pygame.display.set_mode((400, 300), 0, 32)
fps_clock = pygame.time.Clock()

# window title
pygame.display.set_caption('Project Slave')

while True:
    dt = fps_clock.tick(MAX_FPS)
    pygame.draw.circle(main_display, (100, 100, 100), (100, 100), 100, 5)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
