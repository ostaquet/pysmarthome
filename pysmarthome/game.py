import pygame

from challenge.thermostat import use_thermostat
from pysmarthome.common import EVENT_TIME_TICK
from pysmarthome.house import House
from pysmarthome.temperature import OutsideTemperatureSimulator
from pysmarthome.timeticker import TimeTicker


def main():
    # Initialize Pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Smart Home Simulator")

    # Set up the clock & timers
    clock = pygame.time.Clock()
    time_ticker: TimeTicker = TimeTicker(240, 1000)
    pygame.time.set_timer(EVENT_TIME_TICK, time_ticker.get_real_step_in_millis(), 0)

    # Set up internal logic
    is_running: bool = True
    house: House = House()
    temperature_generator: OutsideTemperatureSimulator \
        = OutsideTemperatureSimulator(time_ticker.get_number_of_ticks_per_virtual_day(), 5, 25)

    # Game loop
    while is_running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == EVENT_TIME_TICK:
                # Apply internal logic at each time tick
                time_ticker.increment()
                outside_temperature: float \
                    = temperature_generator.get_temperature_at_tick(time_ticker.get_current_tick())
                house.apply(outside_temperature)

                # Use the thermostat coded for the challenge
                use_thermostat(house.get_rooms(), outside_temperature)

                # Display some debug information
                print(f"******** TIME {time_ticker.str()} - OUTSIDE TEMPERATURE {outside_temperature:.02f}°C *********")
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
