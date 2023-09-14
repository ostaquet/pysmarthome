import pygame

from pysmarthome.constants import EVENT_1SECOND
from pysmarthome.daylight import Daylight
from pysmarthome.house import House


def main():
    # Initialize Pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Smart Home Simulator")

    # Set up the clock & timers
    clock = pygame.time.Clock()
    pygame.time.set_timer(EVENT_1SECOND, 1000, 0)

    # Set up internal logic
    is_running: bool = True
    house: House = House()
    daylight: Daylight = Daylight()
    outside_temperature: float = 30.0

    # Game loop
    while is_running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == EVENT_1SECOND:
                daylight.pass_time()
                house.apply(outside_temperature)
                print("***** TIME " + str(daylight.get_virtual_time()[0]) + "h "
                      + str(daylight.get_virtual_time()[1]) + "min *****")
                print("***** OUTSIDE TEMPERATURE " + str(outside_temperature) + "°C ******")
                house.print_debug_status()

        # Update pysmarthome logic

        # Render graphics
        screen.fill((0, 0, 0))
        pygame.display.flip()

        # Limit the frame rate
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
