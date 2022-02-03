import sys

import pygame as pg

def check_events(ship):
    """Обрабатывает нажатия клавиш и события мыши."""
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                ship.rect.centerx += 1
        #         # ship.moving_rigth == True
        #     elif event.key == pg.K_LEFT:
        #         ship.moving_left == True
        # elif event.type == pg.KEYUP:
        #     if event.key == pg.K_RIGHT:
        #     # Переместить корабль вправо.
        #         ship.moving_rigth == False
        #     elif event.key == pg.K_LEFT:
        #         ship.moving_left == False


def update_screen(ai_settings, screen, ship):
    """Обновляет изображения на экране и отображает новый экран."""
    # При каждом проходе цикла перерисовывается экран.
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # Отображение последнего прорисованного экрана.
    pg.display.flip()