class Room:
    def __init__(self, name: str):
        self._name: str = name
        self._temperature: float = 20.0
        self.window_opened: bool = False
        self.heating_enabled: bool = False

    def get_temperature(self) -> float:
        return self._temperature

    def get_name(self) -> str:
        return self._name

    def apply(self, temperature_exterior: float):
        # Apply temperature evolution in the room based on external temperature, internal temperature
        # and actuators. This function aimed to be applied every second (animation) which is about
        # 6 minutes in virtual time
        self._apply_inertia(temperature_exterior)

        if self.window_opened:
            self._apply_external_impact(temperature_exterior)

        if self.heating_enabled:
            self._apply_heater_impact()

    def _apply_inertia(self, temperature_exterior: float):
        # Apply the impact of external temperature on internal temperature considering that
        # all windows are closed and heating system is off.
        # We consider the observed behavior:
        #  - External temperature at 30°C
        #  - Internal temperature at 20°C
        #  - There is an equilibrium after 24h of time (virtual time)
        delta: float = temperature_exterior - self._temperature
        self._temperature = self._temperature + (delta / 42)

    def _apply_external_impact(self, temperature_exterior: float):
        # Apply the impact of external temperature on internal temperature when all windows are opened
        # We consider the observed behavior:
        #  - External temperature at 30°C
        #  - Internal temperature at 20°C
        #  - There is an equilibrium after 3h of time (virtual time)
        delta: float = temperature_exterior - self._temperature
        self._temperature = self._temperature + (delta / 6)

    def _apply_heater_impact(self):
        # Apply the impact of the heating system on internal temperature
        # We consider that the heating system increase the temperature by 5°C per hour
        self._temperature = self._temperature + (5 / 10)
