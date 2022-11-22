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

level = Level()
pygame.init()
main_display = pygame.display.set_mode((resolution_x, resolution_y), 0, 32)
fps_clock = pygame.time.Clock()
mc_x = 0
mc_y = 0

# window title
pygame.display.set_caption('Project Slave')

while True:
    dt = fps_clock.tick(MAX_FPS)

    # Movement
    speed = 0.1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        mc_x -= speed * dt
    if keys[pygame.K_RIGHT]:
        mc_x += speed * dt
    if keys[pygame.K_UP]:
        mc_y -= speed * dt
    if keys[pygame.K_DOWN]:
        mc_y += speed * dt

    if mc_x < 0:
        mc_x = 0
    if mc_y < 0:
        mc_y = 0
    if mc_x > resolution_x:
        mc_x = resolution_x
    if mc_y > resolution_y:
        mc_y = resolution_x

    for x in range(0, level.grid_width):
        for y in range(0, level.grid_height):
            if level.grid[y][x]:
                main_display.fill(
                    (120, 120, 120), (x * level.tile_width, y * level.tile_height, level.tile_width, level.tile_height)
                )
            else:
                main_display.fill(
                    (20, 20, 20), (x * level.tile_width, y * level.tile_height, level.tile_width, level.tile_height)
                )

    main_display.fill((180, 0, 0), (mc_x, mc_y, 10, 10))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    cursor_pos = pygame.mouse.get_pos()
    cursor_offset_x = cursor_pos[0]
    cursor_offset_y = cursor_pos[1]

    # cursor_x = cursor_pos[0]
    # cursor_y = cursor_pos[1]
    # camera_x_min = resolution_x // 2
    # camera_x_max = (8 * 64) - (resolution_x // 2)
    # camera_y_min = resolution_y // 2
    # camera_y_max = (8 * 64) - (resolution_y // 2)
    # camera_x = (cursor_pos[0] / resolution_x) * ((8 * 64) - resolution_x) + resolution_x // 2
    # camera_y = (cursor_pos[1] / resolution_y) * ((8 * 64) - resolution_y) + resolution_y // 2

    pygame.display.update()
