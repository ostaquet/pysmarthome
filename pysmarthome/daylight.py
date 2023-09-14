import math


class Daylight:
    def __init__(self):
        self._current_6min_tick: int = 0

    def pass_time(self):
        self._current_6min_tick = self._current_6min_tick + 1

        # If day is over, restart at 0
        if self._current_6min_tick >= 240:
            self._current_6min_tick = 0

    def get_virtual_time(self) -> tuple[int, int]:
        hours: int = math.floor((self._current_6min_tick * 6) / 60.0)
        minutes: int = (self._current_6min_tick * 6) % 60
        return hours, minutes

    def is_daylight(self) -> bool:
        hours: int = self.get_virtual_time()[0]
        return 8 <= hours < 20

    def is_night(self) -> bool:
        return not self.is_daylight()
