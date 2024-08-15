import pygame
from constants import WHITE

class Board:
    def __init__(self, width, height, block_size):
        self.width = width
        self.height = height
        self.block_size = block_size
        self.board = [[0 for _ in range(width)] for _ in range(height)]
        self.game_over = False

    def check_collision(self, shape, offset):
        off_x, off_y = offset
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    if x + off_x < 0 or x + off_x >= self.width or y + off_y >= self.height:
                        return True
                    if self.board[y + off_y][x + off_x]:
                        return True
        return False

    def lock_piece(self, shape, piece_pos):
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    self.board[y + piece_pos[1]][x + piece_pos[0]] = 1
        self.remove_full_lines()

    def remove_full_lines(self):
        new_board = [row for row in self.board if not all(row)]
        removed_lines = len(self.board) - len(new_board)
        for _ in range(removed_lines):
            new_board.insert(0, [0 for _ in range(self.width)])
        self.board = new_board

    def draw(self, screen):
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                if cell:
                    self.draw_block(screen, x, y, WHITE)

    def draw_block(self, screen, x, y, color):
        pygame.draw.rect(screen, color, (x * self.block_size, y * self.block_size, self.block_size, self.block_size))
        pygame.draw.rect(screen, WHITE, (x * self.block_size, y * self.block_size, self.block_size, self.block_size), 1)
