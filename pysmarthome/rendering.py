from typing import List, Tuple

import pygame
from pygame import Surface
from pysmarthome.room import Room
from pysmarthome.timeticker import TimeTicker

COLOR_BLACK = (0, 0, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_WHITE = (255, 255, 255)
COLOR_TEMPERATURE = [
    (49, 54, 147),
    (69, 117, 181),
    (117, 171, 210),
    (170, 217, 233),
    (223, 243, 249),
    (255, 255, 191),
    (255, 224, 144),
    (253, 174, 97),
    (243, 110, 67),
    (214, 48, 37),
    (164, 0, 38)
]


def get_color_for_temperature(temperature: float) -> Tuple[int, int, int]:
    mid_scale_color: int = round(len(COLOR_TEMPERATURE) / 2)
    mid_scale_temp: int = 20
    step_temp_per_step_color: float = 2.5
    index_scale_color: int = round(mid_scale_color + ((temperature - mid_scale_temp) / step_temp_per_step_color))
    if index_scale_color < 0:
        index_scale_color = 0
    if index_scale_color >= len(COLOR_TEMPERATURE):
        index_scale_color = len(COLOR_TEMPERATURE) - 1
    return COLOR_TEMPERATURE[index_scale_color]


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


def draw_room(surface: Surface, room: Room, x: int, y: int, width: int, height: int):
    pygame.draw.rect(surface, get_color_for_temperature(room.get_temperature()), (x, y, width, height))

    font = pygame.font.Font(None, 20)

    text_room = font.render(f"{room.get_name()}", True, COLOR_BLACK)
    text_room_rect = text_room.get_rect()
    text_room_rect.center = (width // 2 + x, height // 2 + y - text_room_rect.height)
    surface.blit(text_room, text_room_rect)

    text_temp = font.render(f"{room.get_temperature():.01f}°C", True, COLOR_BLACK)
    text_temp_rect = text_temp.get_rect()
    text_temp_rect.center = (width // 2 + x, height // 2 + y + text_temp_rect.height)
    surface.blit(text_temp, text_temp_rect)


def render_rooms(rooms: List[Room], outside_temperature: float) -> Surface:
    surface: Surface = pygame.Surface((600, 400))
    surface.fill(get_color_for_temperature(outside_temperature))

    draw_room(surface, rooms[0], 50, 50, 200, 300)
    draw_room(surface, rooms[1], 250, 150, 150, 200)
    draw_room(surface, rooms[2], 250, 50, 150, 100)
    draw_room(surface, rooms[3], 400, 50, 150, 150)
    draw_room(surface, rooms[4], 400, 200, 150, 150)

    pygame.draw.line(surface, COLOR_BLACK, (50, 50), (550, 50), 3)
    pygame.draw.line(surface, COLOR_BLACK, (50, 50), (50, 350), 3)
    pygame.draw.line(surface, COLOR_BLACK, (250, 50), (250, 350), 3)
    pygame.draw.line(surface, COLOR_BLACK, (400, 50), (400, 350), 3)
    pygame.draw.line(surface, COLOR_BLACK, (550, 50), (550, 350), 3)
    pygame.draw.line(surface, COLOR_BLACK, (50, 350), (550, 350), 3)
    pygame.draw.line(surface, COLOR_BLACK, (250, 150), (400, 150), 3)
    pygame.draw.line(surface, COLOR_BLACK, (400, 200), (550, 200), 3)

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

    # Render house
    house: Surface = render_rooms(rooms, outside_temperature)
    house_rect = house.get_rect()
    house_rect.center = screen.get_rect().width // 2, screen.get_rect().height // 2
    screen.blit(house, house_rect)
