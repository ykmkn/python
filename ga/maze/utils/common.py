import pygame

# 初期設定
WIDTH, HEIGHT = 500, 500
TILE_SIZE = 50
WHITE, BLACK, GREEN, RED, BLUE = (255, 255, 255), (0, 0, 0), (0, 255, 0), (255, 0, 0), (0, 0, 255)
UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3

def initialize_screen(width, height, title="maze"):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(title)
    return screen


