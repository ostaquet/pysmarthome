from pysmarthome.timeticker import TimeTicker


def test_time_ticker_init():
    ticker: TimeTicker = TimeTicker(240, 1000)

    assert ticker.get_current_tick() == 0
    assert ticker.get_number_of_ticks_per_virtual_day() == 240
    assert ticker.get_virtual_step_in_minutes() == 6
    assert ticker.get_real_step_in_millis() == 1000


def test_time_ticker_init_start_at_tick():
    ticker: TimeTicker = TimeTicker(240, 1000, 90)

    assert ticker.get_current_tick() == 90
    assert ticker.get_number_of_ticks_per_virtual_day() == 240
    assert ticker.get_virtual_step_in_minutes() == 6
    assert ticker.get_real_step_in_millis() == 1000


def test_pass_time_and_virtual_time_computation():
    ticker: TimeTicker = TimeTicker(240, 1000)

    assert ticker.get_current_tick() == 0
    assert ticker.get_hour() == 0
    assert ticker.get_minute() == 0

    ticker.increment()

    assert ticker.get_current_tick() == 1
    assert ticker.get_hour() == 0
    assert ticker.get_minute() == 6

    ticker.increment()
    ticker.increment()
    ticker.increment()
    ticker.increment()

    assert ticker.get_current_tick() == 5
    assert ticker.get_hour() == 0
    assert ticker.get_minute() == 30

    ticker.increment()
    ticker.increment()
    ticker.increment()
    ticker.increment()

    assert ticker.get_current_tick() == 9
    assert ticker.get_hour() == 0
    assert ticker.get_minute() == 54

    ticker.increment()

    assert ticker.get_current_tick() == 10
    assert ticker.get_hour() == 1
    assert ticker.get_minute() == 0


def test_pass_time_24hours():
    ticker: TimeTicker = TimeTicker(240, 1000)

    assert ticker.get_current_tick() == 0
    assert ticker.get_hour() == 0
    assert ticker.get_minute() == 0

    for i in range(0, 239):
        ticker.increment()

    assert ticker.get_current_tick() == 239
    assert ticker.get_hour() == 23
    assert ticker.get_minute() == 54

    ticker.increment()

    assert ticker.get_current_tick() == 0
    assert ticker.get_hour() == 0
    assert ticker.get_minute() == 0


def test_str():
    ticker: TimeTicker = TimeTicker(240, 1000)

    assert ticker.get_current_tick() == 0
    assert ticker.get_hour() == 0
    assert ticker.get_minute() == 0
    assert ticker.str() == "00:00"

    for i in range(0, 129):
        ticker.increment()

    assert ticker.get_current_tick() == 129
    assert ticker.get_hour() == 12
    assert ticker.get_minute() == 54
    assert ticker.str() == "12:54"
