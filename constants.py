# Screen settings
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600

# Board settings
BLOCK_SIZE = 30
BOARD_WIDTH = 10
BOARD_HEIGHT = 20

# Colors
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
PURPLE = (160, 32, 240)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)

# Tetris shapes with corresponding colors
TETRIS_SHAPES = [
    {"shape": [[1, 1, 1, 1]], "color": CYAN},
    {"shape": [[1, 1], [1, 1]], "color": YELLOW},
    {"shape": [[0, 1, 0], [1, 1, 1]], "color": PURPLE},
    {"shape": [[0, 1, 1], [1, 1, 0]], "color": GREEN},
    {"shape": [[1, 1, 0], [0, 1, 1]], "color": RED},
    {"shape": [[1, 0, 0], [1, 1, 1]], "color": BLUE},
    {"shape": [[0, 0, 1], [1, 1, 1]], "color": ORANGE},
]
