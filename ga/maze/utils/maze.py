from utils.common import *

# 迷路データ
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 3, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 2, 1, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

def get_start_pos():
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == 3:
                return [row, col]
def get_goal_pos():
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == 2:
                return [row, col]

def is_walkable(pos):
    return maze[pos[0]][pos[1]] == 0

def draw_maze(screen):
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            color = WHITE if maze[row][col] == 0 else BLACK
            if maze[row][col] == 2:
                color = RED
            elif maze[row][col] == 3:
                color = GREEN
            pygame.draw.rect(screen, color, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
