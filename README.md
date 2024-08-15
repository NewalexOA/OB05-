
### [Описание на русском языке](#русский)

### [Description in English](#english)

---

## <a name="русский"></a>Описание на русском языке

### Описание

Проект представляет собой классическую игру Tetris, реализованную с использованием библиотеки Pygame. В проекте используются основные принципы ООП и SOLID для обеспечения расширяемости и поддержки. Игра включает в себя управление фигурами, игровым полем и логику завершения игры с финальной надписью.

### Структура классов

#### Класс `TetrisGame`
- **Цель:** Управление игровым циклом и взаимодействием с пользователем.
- **Методы:**
  - `__init__`: Инициализация игрового экрана, доски, менеджера фигур и менеджера конца игры.
  - `run`: Главный игровой цикл, который отвечает за обновление игры и отрисовку.
  - `handle_events`: Обрабатывает события, такие как нажатие клавиш и закрытие окна.
  - `update`: Обновляет состояние игры при движении или вращении фигур.
  - `draw`: Отвечает за отрисовку игрового поля и текущей фигуры на экране.
  - `display_game_over`: Отображает финальную надпись "Game Over" на экране.

#### Класс `Board`
- **Цель:** Управление игровым полем, проверка столкновений и обработка удаления линий.
- **Методы:**
  - `__init__`: Инициализация размеров доски и игрового поля.
  - `check_collision`: Проверка столкновений фигуры с границами поля или другими фигурами.
  - `lock_piece`: Фиксирует текущую фигуру на доске после её падения.
  - `remove_full_lines`: Удаляет заполненные линии и сдвигает оставшиеся вниз.
  - `draw`: Отображает игровое поле на экране.
  - `draw_block`: Рисует отдельный блок фигуры на доске.

#### Класс `PieceManager`
- **Цель:** Управление фигурами, их движением и вращением.
- **Методы:**
  - `__init__`: Инициализация текущей фигуры и её позиции на доске.
  - `new_piece`: Создает новую случайную фигуру.
  - `move`: Обрабатывает движение фигуры по горизонтали и вертикали.
  - `rotate`: Поворачивает фигуру на 90 градусов.
  - `update`: Обновляет состояние текущей фигуры, перемещает её вниз или фиксирует на доске.
  - `draw`: Отображает текущую фигуру на игровом экране.

#### Класс `TetrisPiece`
- **Цель:** Представляет отдельную фигуру и её свойства.
- **Методы:**
  - `__init__`: Инициализация фигуры и её цвета.
  - `rotate`: Поворачивает фигуру на 90 градусов.
  - `new_random_piece`: Создает новую случайную фигуру с цветом.

#### Класс `EndScreenManager`
- **Цель:** Управление финальной надписью, выводимой на экран после завершения игры.
- **Методы:**
  - `__init__`: Инициализация параметров текста (шрифт, размер, цвет, фон).
  - `display_message`: Отображает сообщение в центре экрана.
  - `update_text`: Изменяет текст сообщения.
  - `update_font`: Изменяет шрифт и размер текста.
  - `update_text_color`: Изменяет цвет текста.
  - `update_bg_color`: Изменяет цвет фона.

### Инструкция по установке

1. Убедитесь, что у вас установлен Python версии 3.6 или выше.
2. Установите Pygame, используя команду:
   ```bash
   pip install pygame
   ```
3. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/yourusername/tetris-game.git
   ```
4. Перейдите в папку с проектом:
   ```bash
   cd tetris-game
   ```
5. Запустите игру:
   ```bash
   python game.py
   ```

---

## <a name="english"></a>Description in English

### Description

This project is a classic Tetris game implemented using the Pygame library. The project utilizes the main principles of OOP and SOLID to ensure extensibility and maintainability. The game includes figure management, a game board, and game-over logic with a final message.

### Class Structure

#### Class `TetrisGame`
- **Purpose:** Manages the game loop and user interaction.
- **Methods:**
  - `__init__`: Initializes the game screen, board, figure manager, and end screen manager.
  - `run`: The main game loop that handles game updates and rendering.
  - `handle_events`: Handles events such as key presses and window closing.
  - `update`: Updates the game state when moving or rotating pieces.
  - `draw`: Renders the game board and current piece on the screen.
  - `display_game_over`: Displays the "Game Over" message on the screen.

#### Class `Board`
- **Purpose:** Manages the game board, collision detection, and line removal.
- **Methods:**
  - `__init__`: Initializes the board dimensions and game grid.
  - `check_collision`: Checks for collisions between a piece and the edges of the board or other pieces.
  - `lock_piece`: Locks the current piece on the board after it falls.
  - `remove_full_lines`: Removes completed lines and shifts the remaining lines down.
  - `draw`: Renders the game board on the screen.
  - `draw_block`: Draws an individual block of a piece on the board.

#### Class `PieceManager`
- **Purpose:** Manages the pieces, their movement, and rotation.
- **Methods:**
  - `__init__`: Initializes the current piece and its position on the board.
  - `new_piece`: Creates a new random piece.
  - `move`: Handles the movement of the piece horizontally and vertically.
  - `rotate`: Rotates the piece by 90 degrees.
  - `update`: Updates the state of the current piece, moves it down, or locks it on the board.
  - `draw`: Renders the current piece on the game screen.

#### Class `TetrisPiece`
- **Purpose:** Represents an individual piece and its properties.
- **Methods:**
  - `__init__`: Initializes the piece and its color.
  - `rotate`: Rotates the piece by 90 degrees.
  - `new_random_piece`: Creates a new random piece with a color.

#### Class `EndScreenManager`
- **Purpose:** Manages the final game message displayed on the screen after the game ends.
- **Methods:**
  - `__init__`: Initializes text parameters (font, size, color, background).
  - `display_message`: Displays the message centered on the screen.
  - `update_text`: Changes the message text.
  - `update_font`: Changes the font and size of the text.
  - `update_text_color`: Changes the text color.
  - `update_bg_color`: Changes the background color.

### Installation Instructions

1. Make sure you have Python 3.6 or higher installed.
2. Install Pygame using the command:
   ```bash
   pip install pygame
   ```
3. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/tetris-game.git
   ```
4. Navigate to the project folder:
   ```bash
   cd tetris-game
   ```
5. Run the game:
   ```bash
   python game.py
   ```
