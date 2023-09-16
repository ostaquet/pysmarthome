import math


class TimeTicker:
    # Define time tick (1 tick = 6 minutes virtual = 1s real on screen
    # It is expected that a TimeTick is between 0 and 240
    def __init__(self, number_of_ticks_per_virtual_day: int = 240, real_millis_per_tick: int = 1000):
        self._ticks: int = 0
        self._real_millis_per_tick: int = real_millis_per_tick
        self._24h_ticks: int = number_of_ticks_per_virtual_day

    def get_real_step_in_millis(self) -> int:
        return self._real_millis_per_tick

    def get_virtual_step_in_minutes(self) -> int:
        return round(24 * 60 / self._24h_ticks)

    def get_number_of_ticks_per_virtual_day(self) -> int:
        return self._24h_ticks

    def increment(self):
        self._ticks = self._ticks + 1

        # If day is over, restart at 0
        if self._ticks >= self._24h_ticks:
            self._ticks = 0

    def get_current_tick(self) -> int:
        return self._ticks

    def get_hour(self) -> int:
        return math.floor((self._ticks * self.get_virtual_step_in_minutes()) / 60)

    def get_minute(self) -> int:
        return (self._ticks * self.get_virtual_step_in_minutes()) % 60

    def str(self) -> str:
        return f"{self.get_hour():02d}:{self.get_minute():02d}"
