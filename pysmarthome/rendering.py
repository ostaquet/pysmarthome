from typing import List

import pygame
from pygame import Surface
from pysmarthome.room import Room
from pysmarthome.timeticker import TimeTicker

COLOR_BLACK = (0, 0, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_WHITE = (255, 255, 255)


def render_clock(time_ticker: TimeTicker) -> Surface:
    surface: Surface = pygame.Surface((100, 100))
    surface.fill(COLOR_BLACK)

    font = pygame.font.Font(None, 34)
    text = font.render(time_ticker.str(), True, COLOR_WHITE)
    text_rect = text.get_rect()
    text_rect.center = (surface.get_rect().width // 2, surface.get_rect().height // 2)

    surface.blit(text, text_rect)

    return surface


def render_outside_temperature(outside_temperature: float) -> Surface:
    surface: Surface = pygame.Surface((100, 100))
    surface.fill(COLOR_BLACK)

    font = pygame.font.Font(None, 34)
    text = font.render(f"{outside_temperature:.01f}°C", True, COLOR_WHITE)
    text_rect = text.get_rect()
    text_rect.center = (surface.get_rect().width // 2, surface.get_rect().height // 2)

    surface.blit(text, text_rect)

    return surface


def render_all(screen: Surface, time_ticker: TimeTicker, outside_temperature: float, rooms: List[Room]):
    # Background in black
    screen.fill(COLOR_BLACK)

    # Render clock and put it in the top-right corner
    clock: Surface = render_clock(time_ticker)
    screen.blit(clock, (screen.get_rect().width - clock.get_rect().width, 0))

    # Render outside temperature and put in the top-left corner
    temperature: Surface = render_outside_temperature(outside_temperature)
    screen.blit(temperature, (0, 0))
