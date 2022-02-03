import pygame as pg

class Ship():
    def __init__(self, screen):
        """Инициализирует корабль и задает его начальную позицию."""
        self.screen = screen

        # Загрузка изображения корабля и получение прямоугольника.
        self.image = pg.image.load('images\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Флаг перемещения
        self.moving_rigth = False
        self.moving_left = False

    def update(self):
        """Обновляет позицию корабля с учетом флага."""
        if self.moving_rigth:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1


    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)