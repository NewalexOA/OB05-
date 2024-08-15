import random
import pygame
from constants import TETRIS_SHAPES


class TetrisPiece:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color

    @staticmethod
    def new_random_piece():
        piece_data = random.choice(TETRIS_SHAPES)
        return TetrisPiece(piece_data["shape"], piece_data["color"])

    def rotate(self):
        """ Вращаем фигуру на 90 градусов. """
        self.shape = [list(reversed(col)) for col in zip(*self.shape)]


class PieceManager:
    def __init__(self, board):
        self.board = board
        self.current_piece = TetrisPiece.new_random_piece()
        self.piece_pos = [self.board.width // 2, 0]
        if self.board.check_collision(self.current_piece.shape, self.piece_pos):
            self.board.game_over = True  # Завершаем игру, если нет места для новой фигуры

    def move(self, dx, dy):
        new_x = self.piece_pos[0] + dx
        new_y = self.piece_pos[1] + dy
        if not self.board.check_collision(self.current_piece.shape, (new_x, new_y)):
            self.piece_pos = [new_x, new_y]

    def update(self):
        if pygame.time.get_ticks() % 1000 < 50:
            new_y = self.piece_pos[1] + 1
            if not self.board.check_collision(self.current_piece.shape, (self.piece_pos[0], new_y)):
                self.piece_pos[1] = new_y
            else:
                self.board.lock_piece(self.current_piece.shape, self.piece_pos)
                self.current_piece = TetrisPiece.new_random_piece()
                self.piece_pos = [self.board.width // 2, 0]

                # Проверка на завершение игры
                if self.board.check_collision(self.current_piece.shape, self.piece_pos):
                    self.board.game_over = True

    def rotate(self):
        rotated_piece = TetrisPiece(self.current_piece.shape, self.current_piece.color)
        rotated_piece.rotate()
        if not self.board.check_collision(rotated_piece.shape, self.piece_pos):
            self.current_piece = rotated_piece

    def draw(self, screen):
        for y, row in enumerate(self.current_piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    self.board.draw_block(screen, x + self.piece_pos[0], y + self.piece_pos[1],
                                          self.current_piece.color)
