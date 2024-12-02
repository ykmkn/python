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

hint = None

def get_hint(pos):
    if hint is None:
        raise ValueError("Config has not been initialized.")
    return hint[pos[0]][pos[1]]

def create_hint_to_goal():
    global hint
    hint = [[0 for _ in range(len(maze[0]))] for _ in range(len(maze))]
    goal_pos = get_goal_pos()
    hint[goal_pos[0]][goal_pos[1]] = 100
    queue = [goal_pos]
    while len(queue) > 0:
        pos = queue.pop(0)
        for i in range(4):
            next_pos = pos[:]
            if i == 0: next_pos[0] -= 1
            if i == 1: next_pos[0] += 1
            if i == 2: next_pos[1] -= 1
            if i == 3: next_pos[1] += 1
            if maze[next_pos[0]][next_pos[1]] == 0 and hint[next_pos[0]][next_pos[1]] == 0:
                hint[next_pos[0]][next_pos[1]] = hint[pos[0]][pos[1]] - 2
                queue.append(next_pos)
    for row in hint:
        print(row)
    return hint

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
