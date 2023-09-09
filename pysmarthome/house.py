from typing import List
from pysmarthome.room import Room


class House:
    def __init__(self):
        self.rooms: List[Room] = [Room("Living room")]

    def print_debug_status(self):
        for room in self.rooms:
            print("Status in " + room.get_name())
            print("  Temperature " + str(room.get_temperature()) + "°C")
            status:str = "Windows "
            if room.window_opened:
                status = status + "opened"
            else:
                status = status + "closed"
            status = status + ", heating system is "
            if room.heating_enabled:
                status = status + "ON"
            else:
                status = status + "OFF"
            print("  " + status)
