import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Настройки окна
screen_width = 300
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Цвета
WHITE = (255, 255, 255)
BLOCK_COLOR = (0, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)

# Размеры
block_size = 30
board_width = 10
board_height = 20

# Игровое поле
board = [[0 for _ in range(board_width)] for _ in range(board_height)]

# Фигуры
tetris_shapes = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[0, 1, 0], [1, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 0], [0, 1, 1]],
    [[1, 0, 0], [1, 1, 1]],
    [[0, 0, 1], [1, 1, 1]]
]

def new_piece():
    return random.choice(tetris_shapes)

def draw_block(x, y):
    pygame.draw.rect(screen, BLOCK_COLOR, (x * block_size, y * block_size, block_size, block_size))
    pygame.draw.rect(screen, WHITE, (x * block_size, y * block_size, block_size, block_size), 1)

def remove_line(board):
    new_board = [row for row in board if not all(row)]
    removed_lines = len(board) - len(new_board)
    for _ in range(removed_lines):
        new_board.insert(0, [0 for _ in range(board_width)])
    return new_board

def draw_board(board, piece, piece_pos):
    screen.fill(BACKGROUND_COLOR)
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell: draw_block(x, y)
    for y, row in enumerate(piece):
        for x, cell in enumerate(row):
            if cell: draw_block(x + piece_pos[0], y + piece_pos[1])
    pygame.display.flip()

current_piece = new_piece()
piece_pos = [board_width // 2, 0]

# Игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                piece_pos[0] -= 1
            elif event.key == pygame.K_RIGHT:
                piece_pos[0] += 1
            elif event.key == pygame.K_DOWN:
                piece_pos[1] += 1
            # Здесь добавить обработку вращения и других действий

    # Обновление игрового состояния
    # Здесь добавить логику падения фигуры, проверки столкновений и т.д.

    draw_board(board, current_piece, piece_pos)

    pygame.time.wait(100)  # Установка задержки для замедления игры
