import pytest

from pysmarthome.exceptions import InputParameterError
from pysmarthome.temperature import OutsideTemperatureSimulator


def test_temperature_init():
    temperature: OutsideTemperatureSimulator = OutsideTemperatureSimulator(240, -10, 30)

    assert temperature.get_minimum() == -10
    assert temperature.get_maximum() == 30


def test_temperature_init_validation():
    with pytest.raises(InputParameterError, match=r"Number of ticks per day cannot be zero or negative."):
        OutsideTemperatureSimulator(0, -10, 30)

    with pytest.raises(InputParameterError, match=r"Number of ticks per day cannot be zero or negative."):
        OutsideTemperatureSimulator(-10, -10, 30)

    with pytest.raises(InputParameterError, match=r"Minimum temperature 10 is above maximum temperature 5"):
        OutsideTemperatureSimulator(240, 10, 5)


def test_variation_temperature_full_positive():
    temperature: OutsideTemperatureSimulator = OutsideTemperatureSimulator(240, 10, 30)

    # At 4AM, we are expecting the minimum
    assert temperature.get_temperature_at_tick(40) == 10
    # At 4PM, we are expecting the maximum
    assert temperature.get_temperature_at_tick(160) == 30

    # Spot checks
    assert abs(temperature.get_temperature_at_tick(0) - 15.0) < 0.01
    assert abs(temperature.get_temperature_at_tick(90) - 17.41) < 0.01
    assert abs(temperature.get_temperature_at_tick(190) - 27.07) < 0.01


def test_variation_temperature_full_negative():
    temperature: OutsideTemperatureSimulator = OutsideTemperatureSimulator(240, -30, -10)

    # At 4AM, we are expecting the minimum
    assert temperature.get_temperature_at_tick(40) == -30
    # At 4PM, we are expecting the maximum
    assert temperature.get_temperature_at_tick(160) == -10

    # Spot checks
    assert abs(temperature.get_temperature_at_tick(0) - (-25.0)) < 0.01
    assert abs(temperature.get_temperature_at_tick(90) - (-22.58)) < 0.01
    assert abs(temperature.get_temperature_at_tick(190) - (-12.93)) < 0.01


def test_variation_temperature():
    temperature: OutsideTemperatureSimulator = OutsideTemperatureSimulator(240, -10, 20)

    # At 4AM, we are expecting the minimum
    assert temperature.get_temperature_at_tick(40) == -10
    # At 4PM, we are expecting the maximum
    assert temperature.get_temperature_at_tick(160) == 20

    print(temperature.get_temperature_at_tick(0))
    print(temperature.get_temperature_at_tick(90))
    print(temperature.get_temperature_at_tick(190))

    # Spot checks
    assert abs(temperature.get_temperature_at_tick(0) - (-2.5)) < 0.01
    assert abs(temperature.get_temperature_at_tick(90) - 1.12) < 0.01
    assert abs(temperature.get_temperature_at_tick(190) - 15.61) < 0.01


def test_settings_min_max_validation():
    temperature: OutsideTemperatureSimulator = OutsideTemperatureSimulator(240, -10, 20)

    with pytest.raises(InputParameterError, match=r"Minimum temperature 21 is above current maximum 20"):
        temperature.set_minimum(21)

    temperature.set_minimum(20)
    temperature.set_minimum(-10)

    with pytest.raises(InputParameterError, match=r"Maximum temperature -11 is below current minimum -10"):
        temperature.set_maximum(-11)

    temperature.set_maximum(-10)
    temperature.set_maximum(20)