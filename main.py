import pygame
import sys
import random
import time  # Импортируем модуль времени для работы с таймерами

pygame.init()

screen_width = 300
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

WHITE = (255, 255, 255)
BLOCK_COLOR = (0, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)

block_size = 30
board_width = 10
board_height = 20

board = [[0 for _ in range(board_width)] for _ in range(board_height)]

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

def check_collision(board, piece, piece_pos):
    for y, row in enumerate(piece):
        for x, cell in enumerate(row):
            try:
                if cell and board[y + piece_pos[1]][x + piece_pos[0]]:
                    return True
            except IndexError:
                return True
    return False

def add_piece_to_board(board, piece, piece_pos):
    for y, row in enumerate(piece):
        for x, cell in enumerate(row):
            if cell: board[y + piece_pos[1]][x + piece_pos[0]] = 1

current_piece = new_piece()
piece_pos = [board_width // 2, 0]
last_fall_time = time.time()
fall_speed = 1.0  # Скорость падения фигуры

while True:
    screen.fill(BACKGROUND_COLOR)

    if time.time() - last_fall_time > fall_speed:
        piece_pos[1] += 1
        last_fall_time = time.time()

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

    if check_collision(board, current_piece, piece_pos) or piece_pos[1] + len(current_piece) == board_height:
        piece_pos[1] -= 1  # Возвращаем фигуру на шаг назад
        add_piece_to_board(board, current_piece, piece_pos)
        board = remove_line(board)
        current_piece = new_piece()
        piece_pos = [board_width // 2, 0]

    draw_board(board, current_piece, piece_pos)

    pygame.display.flip()
    pygame.time.wait(100)
