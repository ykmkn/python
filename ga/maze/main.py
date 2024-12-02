import pygame
import random
import utils.ga as ga
import utils.maze as maze
import utils.player as player
from utils.common import *

screen = initialize_screen(WIDTH, HEIGHT)

# フォントの設定
font = pygame.font.Font(None, 36)  # デフォルトフォント、サイズ36

# 個体の初期化
individuals = [[random.randint(0,3) for j in range(30)] for i in range(5)]
# 内部で進化に使用する世代数
num_of_generation = 30

# 進化の世代数
generation_count = 0

# ゲームループ
running = True

# ヒントの作成
maze.create_hint_to_goal()

while running:
    # 強制終了用のイベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 遺伝的アルゴリズムの処理
    individuals, strongest_individual = ga.create_next_individuals(individuals, num_of_generation)

    # プレイヤーの初期位置とゴールの位置を取得
    player_pos = maze.get_start_pos()
    goal_pos = maze.get_goal_pos()

    # プレイヤーの位置を描画
    for move in strongest_individual:
        screen.fill(BLUE)

        # 迷路とプレイヤーを描画
        maze.draw_maze(screen)
        player.draw_player(screen, player_pos)

        # 進化の世代数を描画
        text = font.render(f"Count: {generation_count}", True, WHITE)  # アンチエイリアス=True, 色=WHITE
        text_rect = text.get_rect()
        text_rect.topright = (WIDTH - 10, 10)  # 画面右上の位置に配置 (10pxの余白)
        screen.blit(text, text_rect)

        # 画面を更新
        pygame.display.flip()
        pygame.time.delay(100)

        # プレイヤーを移動
        player.move_player(player_pos, move)

    # 世代を進める
    generation_count += 1

pygame.quit()
