import pygame
import sys

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((600, 800))
    pygame.display.set_caption("Tetris PY")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()

if __name__ == '__main__':
    run_game()
