import sys

import pygame as pg
import pygame.event

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # Инициализирует pygame, settings и объект экрана.
    pg.init()
    ai_settings = Settings()
    screen = pg.display.set_mode((ai_settings.screen_width, ai_settings.screen_heigth))
    pg.display.set_caption("Alien Invasion")
    # Создание корабля.
    ship = Ship(screen)

    # Запуск основного цикла игры.
    while True:
        # Отслеживание событий клавиатуры и мыши.
        gf.check_events(ship)
        # ship.update()
        gf.update_screen(ai_settings, screen, ship)


run_game()