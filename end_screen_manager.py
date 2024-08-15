import pygame


class EndScreenManager:
    def __init__(self, screen, text="Game Over", font_name='Arial', font_size=36, text_color=(0, 0, 0),
                 bg_color=(255, 255, 255), bold=True):
        """
        Конструктор EndScreenManager принимает экран для вывода,
        текст сообщения, имя шрифта, размер шрифта, цвет текста, цвет фона и параметр жирности.
        """
        self.screen = screen
        self.text = text
        self.text_color = text_color
        self.bg_color = bg_color
        self.font = pygame.font.SysFont(font_name, font_size, bold=bold)

    def display_message(self):
        """
        Отображает сообщение на экране в центре на фоне белого цвета.
        """
        # Создаем поверхность с белым фоном
        message_surface = self.font.render(self.text, True, self.text_color, self.bg_color)

        # Центрируем надпись на экране
        message_rect = message_surface.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))

        # Выводим поверхность с текстом на экран
        self.screen.blit(message_surface, message_rect)

    def update_text(self, new_text):
        """
        Позволяет обновить текст сообщения.
        """
        self.text = new_text

    def update_font(self, font_name, font_size, bold=True):
        """
        Позволяет обновить шрифт сообщения, включая параметр жирности.
        """
        self.font = pygame.font.SysFont(font_name, font_size, bold=bold)

    def update_text_color(self, new_color):
        """
        Позволяет обновить цвет текста.
        """
        self.text_color = new_color

    def update_bg_color(self, new_color):
        """
        Позволяет обновить цвет фона.
        """
        self.bg_color = new_color
