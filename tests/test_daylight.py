from pysmarthome.daylight import Daylight


def test_daylight_init():
    daylight_simulator: Daylight = Daylight()

    assert daylight_simulator.get_virtual_time()[0] == 0
    assert daylight_simulator.get_virtual_time()[1] == 0


def test_pass_time_and_virtual_time_computation():
    daylight_simulator: Daylight = Daylight()

    assert daylight_simulator.get_virtual_time()[0] == 0
    assert daylight_simulator.get_virtual_time()[1] == 0

    daylight_simulator.pass_time()

    assert daylight_simulator.get_virtual_time()[0] == 0
    assert daylight_simulator.get_virtual_time()[1] == 6

    daylight_simulator.pass_time()
    daylight_simulator.pass_time()
    daylight_simulator.pass_time()
    daylight_simulator.pass_time()

    assert daylight_simulator.get_virtual_time()[0] == 0
    assert daylight_simulator.get_virtual_time()[1] == 30

    daylight_simulator.pass_time()
    daylight_simulator.pass_time()
    daylight_simulator.pass_time()
    daylight_simulator.pass_time()

    assert daylight_simulator.get_virtual_time()[0] == 0
    assert daylight_simulator.get_virtual_time()[1] == 54

    daylight_simulator.pass_time()

    assert daylight_simulator.get_virtual_time()[0] == 1
    assert daylight_simulator.get_virtual_time()[1] == 0


def test_pass_time_24hours():
    daylight_simulator: Daylight = Daylight()

    assert daylight_simulator.get_virtual_time()[0] == 0
    assert daylight_simulator.get_virtual_time()[1] == 0

    for i in range(0, 239):
        daylight_simulator.pass_time()

    assert daylight_simulator.get_virtual_time()[0] == 23
    assert daylight_simulator.get_virtual_time()[1] == 54

    daylight_simulator.pass_time()

    assert daylight_simulator.get_virtual_time()[0] == 0
    assert daylight_simulator.get_virtual_time()[1] == 0


def test_daylight_night_time():
    daylight_simulator: Daylight = Daylight()

    assert daylight_simulator.get_virtual_time()[0] == 0
    assert daylight_simulator.get_virtual_time()[1] == 0
    assert not daylight_simulator.is_daylight()
    assert daylight_simulator.is_night()

    for i in range(0, 79):
        daylight_simulator.pass_time()

    assert daylight_simulator.get_virtual_time()[0] == 7
    assert daylight_simulator.get_virtual_time()[1] == 54
    assert not daylight_simulator.is_daylight()
    assert daylight_simulator.is_night()

    daylight_simulator.pass_time()

    assert daylight_simulator.get_virtual_time()[0] == 8
    assert daylight_simulator.get_virtual_time()[1] == 0
    assert daylight_simulator.is_daylight()
    assert not daylight_simulator.is_night()

    for i in range(0, 119):
        daylight_simulator.pass_time()

    assert daylight_simulator.get_virtual_time()[0] == 19
    assert daylight_simulator.get_virtual_time()[1] == 54
    assert daylight_simulator.is_daylight()
    assert not daylight_simulator.is_night()

    daylight_simulator.pass_time()

    assert daylight_simulator.get_virtual_time()[0] == 20
    assert daylight_simulator.get_virtual_time()[1] == 0
    assert not daylight_simulator.is_daylight()
    assert daylight_simulator.is_night()

    for i in range(0, 20):
        daylight_simulator.pass_time()

    assert daylight_simulator.get_virtual_time()[0] == 22
    assert daylight_simulator.get_virtual_time()[1] == 0
    assert not daylight_simulator.is_daylight()
    assert daylight_simulator.is_night()
