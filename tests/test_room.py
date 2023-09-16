from pysmarthome.room import Room, RoomLogic


def test_init_with_default_values():
    room: Room = Room("Living room")

    assert room.get_name() == "Living room"
    assert room.get_temperature() == 20.0
    assert not room.window_opened
    assert not room.heating_enabled


def test_apply_inertia_increasing_temperature():
    room: RoomLogic = RoomLogic("Living room")
    assert room.get_temperature() == 20.0
    assert not room.window_opened
    assert not room.heating_enabled

    # After 24h, we consider that the room reached the temperature of outside
    for hour in range(24):
        for tenth_of_an_hour in range(10):
            room.apply(30.0)
    room.apply(30.0)

    assert abs(room.get_temperature() - 30.0) <= 0.1


def test_apply_inertia_decreasing_temperature():
    room: RoomLogic = RoomLogic("Living room")
    assert room.get_temperature() == 20.0
    assert not room.window_opened
    assert not room.heating_enabled

    # After 24h, we consider that the room reached the temperature of outside
    for hour in range(24):
        for tenth_of_an_hour in range(10):
            room.apply(10.0)
    room.apply(10.0)

    assert abs(room.get_temperature() - 10.0) <= 0.1


def test_apply_external_impact_with_window_opened_increasing_temperature():
    room: RoomLogic = RoomLogic("Living room")
    room.window_opened = True
    assert room.get_temperature() == 20.0
    assert room.window_opened
    assert not room.heating_enabled

    # After 3h, we consider that the room reached the temperature of outside
    for hour in range(3):
        for tenth_of_an_hour in range(10):
            room.apply(30.0)
    room.apply(30.0)

    assert abs(room.get_temperature() - 30.0) <= 0.1


def test_apply_external_impact_with_window_opened_decreasing_temperature():
    room: RoomLogic = RoomLogic("Living room")
    room.window_opened = True
    assert room.get_temperature() == 20.0
    assert room.window_opened
    assert not room.heating_enabled

    # After 3h, we consider that the room reached the temperature of outside
    for hour in range(3):
        for tenth_of_an_hour in range(10):
            room.apply(10.0)
    room.apply(10.0)

    assert abs(room.get_temperature() - 10.0) <= 0.1


def test_apply_heating_system():
    room: RoomLogic = RoomLogic("Living room")
    room.heating_enabled = True
    assert room.get_temperature() == 20.0
    assert not room.window_opened
    assert room.heating_enabled

    # After 1h, we consider that the room gains 5°C
    for tenth_of_an_hour in range(10):
        room.apply(room.get_temperature())

    assert abs(room.get_temperature() - 25.0) <= 0.1

