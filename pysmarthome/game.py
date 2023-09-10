import pygame

from pysmarthome.house import House


def main():
    # Initialize Pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Smart Home Simulator")

    # Set up the clock
    clock = pygame.time.Clock()

    # Set up internal logic
    is_running: bool = True
    last_tick: int = pygame.time.get_ticks()
    house: House = House()
    outside_temperature: float = 30.0

    # Game loop
    while is_running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        # Update pysmarthome logic
        current_tick: int = pygame.time.get_ticks()
        if current_tick - last_tick >= 1000:
            house.apply(outside_temperature)
            last_tick = current_tick
            print("***** OUTSIDE TEMPERATURE " + str(outside_temperature) + "°C ******")
            house.print_debug_status()

        # Render graphics
        screen.fill((0, 0, 0))
        pygame.display.flip()

        # Limit the frame rate
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
