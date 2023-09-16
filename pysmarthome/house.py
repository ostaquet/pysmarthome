from typing import List

from pysmarthome.exceptions import InputParameterError
from pysmarthome.room import Room, RoomLogic


class House:
    def __init__(self):
        self._rooms: List[RoomLogic] = [RoomLogic("Living room"), RoomLogic("Kitchen"), RoomLogic("Hall"),
                                   RoomLogic("Bedroom"), RoomLogic("Bathroom")]

    def get_room(self, room_number: int) -> Room:
        if room_number < 0 or room_number >= self.count_rooms():
            raise InputParameterError(f"Invalid room number {room_number}")

        return self._rooms[room_number]

    def count_rooms(self) -> int:
        return len(self._rooms)

    def apply(self, temperature_exterior: float):
        for room in self._rooms:
            room.apply(temperature_exterior)

    def print_debug_status(self):
        for room in self._rooms:
            status: str = "Windows "
            if room.window_opened:
                status = status + "opened"
            else:
                status = status + "closed"
            status = status + ", heating "
            if room.heating_enabled:
                status = status + "ON"
            else:
                status = status + "OFF"
            print(f"{room.get_name()} - T° {room.get_temperature():.02f}°C ({status})")

    def get_rooms(self) -> List[Room]:
        return self._rooms
