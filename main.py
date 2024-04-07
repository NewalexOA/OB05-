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

<<<<<<< Updated upstream
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
=======
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEMOTION:
            image_rect.x = event.pos[0] - 25
            image_rect.y = event.pos[1] - 25
>>>>>>> Stashed changes


def new_piece():
    return random.choice(tetris_shapes)


def draw_block(x, y):
    pygame.draw.rect(screen, BLOCK_COLOR, (x * block_size, y * block_size, block_size, block_size))
    pygame.draw.rect(screen, WHITE, (x * block_size, y * block_size, block_size, block_size), 1)

def rotate_shape(shape):
    return [ [ shape[y][x]
               for y in range(len(shape)) ]
             for x in range(len(shape[0]) - 1, -1, -1) ]

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


pygame.time.set_timer(pygame.USEREVENT + 1, 1000)  # Событие таймера каждую секунду
current_piece = new_piece()
piece_pos = [board_width // 2, 0]

# Игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            new_x = piece_pos[0]
            new_y = piece_pos[1]
            if event.key == pygame.K_LEFT:
                new_x -= 1
            elif event.key == pygame.K_RIGHT:
                new_x += 1
            elif event.key == pygame.K_DOWN:
                new_y += 1

            if not check_collision(board, current_piece, (new_x, new_y)):
                piece_pos[0] = new_x
                piece_pos[1] = new_y

        elif event.type == pygame.USEREVENT + 1:
            new_y = piece_pos[1] + 1
            if not check_collision(board, current_piece, (piece_pos[0], new_y)):
                piece_pos[1] = new_y
            else:
                # Закрепляем фигуру на игровом поле
                for y, row in enumerate(current_piece):
                    for x, cell in enumerate(row):
                        if cell:
                            board[y + piece_pos[1]][x + piece_pos[0]] = 1
                # Удаляем заполненные линии
                board = remove_line(board)
                # Создаем новую фигуру
                current_piece = new_piece()
                piece_pos = [board_width // 2, 0]

    draw_board(board, current_piece, piece_pos)
    pygame.display.flip()
    pygame.time.wait(100)
