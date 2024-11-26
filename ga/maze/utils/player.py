import pygame
from utils.common import *
from utils.maze import is_walkable

def draw_player(screen, player_pos):
    pygame.draw.circle(screen, BLUE,
                       (player_pos[1] * TILE_SIZE + TILE_SIZE // 2, player_pos[0] * TILE_SIZE + TILE_SIZE // 2),
                       TILE_SIZE // 4)

def move_player(pos, direction):
    new_pos = pos[:]
    if direction == UP: new_pos[0] -= 1
    if direction == DOWN: new_pos[0] += 1
    if direction == LEFT: new_pos[1] -= 1
    if direction == RIGHT: new_pos[1] += 1

    # 移動先が通路なら移動
    if is_walkable(new_pos):
        pos[0], pos[1] = new_pos
