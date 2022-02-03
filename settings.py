class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        self.screen_width = 700
        self.screen_heigth = 600
        self.bg_color = (230, 230, 230)
        # Настройки корабля
        self.ship_speed_factor = 1.5
        # Параметры пули
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_heigth = 15
        self.bullet_color = 60, 60, 60