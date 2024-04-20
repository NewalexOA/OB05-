import pygame
import sys
import random

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

def rotate_shape(shape):
    """ Возвращает новую фигуру после поворота на 90 градусов по часовой стрелке. """
    return [list(reversed(col)) for col in zip(*shape)]

def check_collision(board, shape, offset):
    off_x, off_y = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                if x + off_x < 0 or x + off_x >= board_width or y + off_y >= board_height:
                    return True
                if board[y + off_y][x + off_x]:
                    return True
    return False

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

pygame.time.set_timer(pygame.USEREVENT + 1, 1000)
current_piece = new_piece()
piece_pos = [board_width // 2, 0]

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    new_x = piece_pos[0]
    new_y = piece_pos[1]

    if keys[pygame.K_LEFT]:
        new_x -= 1
    if keys[pygame.K_RIGHT]:
        new_x += 1
    if keys[pygame.K_DOWN]:
        new_y += 1

    # Обработка поворота фигуры
    if keys[pygame.K_UP]:
        rotated_piece = rotate_shape(current_piece)
        if not check_collision(board, rotated_piece, piece_pos):
            current_piece = rotated_piece

    # Проверка на столкновения после перемещения
    if not check_collision(board, current_piece, (new_x, new_y)):
        piece_pos[0] = new_x
        piece_pos[1] = new_y

    # Событие автоматического опускания фигуры
    if pygame.time.get_ticks() % 1000 < 50:  # Примерное время 1 секунда
        new_y = piece_pos[1] + 1
        if not check_collision(board, current_piece, (piece_pos[0], new_y)):
            piece_pos[1] = new_y
        else:
            for y, row in enumerate(current_piece):
                for x, cell in enumerate(row):
                    if cell:
                        board[y + piece_pos[1]][x + piece_pos[0]] = 1
            board = remove_line(board)
            current_piece = new_piece()
            piece_pos = [board_width // 2, 0]

    draw_board(board, current_piece, piece_pos)
    pygame.display.flip()
    pygame.time.wait(50)  # Контроль скорости игры

pygame.quit()
sys.exit()
