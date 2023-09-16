from typing import List
import pytest

from pysmarthome.exceptions import InputParameterError
from pysmarthome.house import House


def test_house_init():
    house: House = House()

    assert house.count_rooms() == 5
    assert house.get_room(0).get_name() == "Living room"
    assert house.get_room(1).get_name() == "Kitchen"
    assert house.get_room(2).get_name() == "Hall"
    assert house.get_room(3).get_name() == "Bedroom"
    assert house.get_room(4).get_name() == "Bathroom"


def test_get_room_outside_range():
    house: House = House()
    assert house.count_rooms() == 5

    with pytest.raises(InputParameterError, match=r".* -1"):
        house.get_room(-1).get_name()

    with pytest.raises(InputParameterError, match=r".* 5"):
        assert house.get_room(5).get_name()


def test_ensure_that_apply_is_applied_on_all_rooms():
    house: House = House()
    assert house.count_rooms() == 5

    initial_temperature: List[float] = []

    for i in range(0, house.count_rooms()):
        initial_temperature.append(house.get_room(i).get_temperature())
        house.get_room(i).heating_enabled = True

    house.apply(30.0)

    for i in range(0, house.count_rooms()):
        assert abs(initial_temperature[i] - house.get_room(i).get_temperature()) > 0.1


def test_list_of_rooms_should_not_include_apply_logic_but_must_be_considered_when_apply():
    house: House = House()
    assert house.count_rooms() == 5

    initial_temperature: List[float] = []

    for room in house.get_rooms():
        initial_temperature.append(room.get_temperature())
        room.heating_enabled = True

    house.apply(30.0)

    for i in range(0, house.count_rooms()):
        assert abs(initial_temperature[i] - house.get_room(i).get_temperature()) > 0.1
