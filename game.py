import pygame
import sys
from board import Board
from piece_manager import PieceManager
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE, BOARD_WIDTH, BOARD_HEIGHT
from end_screen_manager import EndScreenManager


class TetrisGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tetris")
        self.board = Board(BOARD_WIDTH, BOARD_HEIGHT, BLOCK_SIZE)
        self.piece_manager = PieceManager(self.board)
        self.running = True

        # Инициализируем менеджера конца игры с белым фоном и черными жирными буквами
        self.end_screen_manager = EndScreenManager(
            self.screen,
            text="Game Over",
            font_name='Arial',
            font_size=48,
            text_color=(0, 0, 0),  # Черный текст
            bg_color=(255, 255, 255),  # Белый фон
            bold=True  # Жирный текст
        )

    def run(self):
        pygame.time.set_timer(pygame.USEREVENT + 1, 1000)
        clock = pygame.time.Clock()

        while self.running:
            self.handle_events()
            if not self.board.game_over:
                self.update()
            self.draw()
            clock.tick(60)

        pygame.quit()
        sys.exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.piece_manager.move(-1, 0)
        if keys[pygame.K_RIGHT]:
            self.piece_manager.move(1, 0)
        if keys[pygame.K_DOWN]:
            self.piece_manager.move(0, 1)

        if keys[pygame.K_UP]:
            self.piece_manager.rotate()

        self.piece_manager.update()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.board.draw(self.screen)
        self.piece_manager.draw(self.screen)

        # Если игра закончена, вызываем менеджера конца игры для вывода сообщения
        if self.board.game_over:
            self.end_screen_manager.display_message()

        pygame.display.flip()


if __name__ == '__main__':
    game = TetrisGame()
    game.run()
