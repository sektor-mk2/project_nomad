import sys
import pygame
from pygame.locals import *

MAX_FPS = 60
resolution_x = 400
resolution_y = 300


class Level:
    def __init__(self):
        self.grid = [
            [1, 1, 0, 1, 1, 1, 0, 1],
            [1, 0, 0, 1, 1, 0, 0, 1],
            [0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 1, 0, 0, 1, 1],
            [1, 1, 0, 1, 1, 1, 0, 1],
            [1, 0, 0, 1, 1, 0, 0, 1],
            [0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 1, 0, 0, 1, 1],
        ]
        self.grid_width = 8
        self.grid_height = 8
        self.tile_width = 64
        self.tile_height = 64

    def draw(self, surface):
        for x in range(0, self.grid_width):
            for y in range(0, self.grid_height):
                if self.grid[y][x]:
                    surface.fill((100, 100, 100), (x * self.tile_width, y * self.tile_height, self.tile_width, self.tile_height))


level = Level()
pygame.init()
main_display = pygame.display.set_mode((resolution_x, resolution_y), 0, 32)
fps_clock = pygame.time.Clock()

# window title
pygame.display.set_caption('Project Slave')

while True:
    dt = fps_clock.tick(MAX_FPS)
    level.draw(main_display)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    cursor_pos = pygame.mouse.get_pos()
    print(cursor)
    pygame.display.update()
