import pygame
import random
import utils.ga as ga
import utils.maze as maze
import utils.player as player
from utils.common import *

screen = initialize_screen(WIDTH, HEIGHT)

# フォントの設定
font = pygame.font.Font(None, 36)  # デフォルトフォント、サイズ36

# first generation
individuals = [[random.randint(0,3) for j in range(30)] for i in range(5)]
# number of generations
num_of_generation = 30

generation_count = 0

# メインループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    individuals, strongest_individual = ga.create_next_individuals(individuals, num_of_generation)
    player_pos = maze.get_start_pos()
    goal_pos = maze.get_goal_pos()

    for move in strongest_individual:
        screen.fill(BLUE)
        maze.draw_maze(screen)
        player.draw_player(screen, player_pos)
        # テキストを描画
        text = font.render(f"Count: {generation_count}", True, WHITE)  # アンチエイリアス=True, 色=WHITE
        text_rect = text.get_rect()
        text_rect.topright = (WIDTH - 10, 10)  # 画面右上の位置に配置 (10pxの余白)

        # テキストを画面に描画
        screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.delay(100)
        player.move_player(player_pos, move)
    generation_count += 1

    # draw current generation
    screen.fill(BLUE)
    pygame.time.delay(500)

pygame.quit()
