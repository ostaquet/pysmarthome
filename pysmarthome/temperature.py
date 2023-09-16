import math

from pysmarthome.exceptions import InputParameterError


class OutsideTemperatureSimulator:
    def __init__(self, number_of_ticks_per_virtual_day: int, minimum: int = 10, maximum: int = 25):
        if minimum > maximum:
            raise InputParameterError(f"Minimum temperature {minimum} is above maximum temperature {maximum}")
        if number_of_ticks_per_virtual_day <= 0:
            raise InputParameterError("Number of ticks per day cannot be zero or negative. Usual value is 240.")

        self._min: int = minimum
        self._max: int = maximum
        self._24h_ticks: int = number_of_ticks_per_virtual_day

    def set_minimum(self, minimum: int):
        if minimum > self._max:
            raise InputParameterError(f"Minimum temperature {minimum} is above current maximum {self._max}")
        self._min = minimum

    def set_maximum(self, maximum: int):
        if maximum < self._min:
            raise InputParameterError(f"Maximum temperature {maximum} is below current minimum {self._min}")
        self._max = maximum

    def get_minimum(self) -> int:
        return self._min

    def get_maximum(self) -> int:
        return self._max

    def get_temperature_at_tick(self, tick: int) -> float:
        delta_sin_4am: float = self._24h_ticks * 10 / 24  # Move the sine wave to have minimum at 4AM
        coefficient: float = (math.sin((tick - delta_sin_4am) * ((math.pi * 2) / self._24h_ticks)) + 1) / 2
        delta_temperature: float = self._max - self._min
        return self._min + coefficient * delta_temperature
