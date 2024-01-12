import pytest
import datetime

from functions.level_1.two_date_parser import compose_datetime_from


@pytest.mark.parametrize('date_str', ['today', '', 'tomorrow', 'anywhen', 'ToMoRrOw', 'tomorr0w'])
def test__compose_datetime_from__processes_date_str_correctly(date_str):
    expected_date = datetime.date.today() + datetime.timedelta(days=int(date_str == 'tomorrow'))
    assert compose_datetime_from(date_str, '00:00').date() == expected_date


@pytest.mark.parametrize(
    'time_str, expected_hour, expected_min',
    [
        pytest.param('  10:00', 10, 0, id='space before time it time_str'),
        pytest.param('23:59   ', 23, 59, id='space after time in time_str'),
        pytest.param('  00:00  ', 0, 0, id='unstripped from both sides time_str'),
        pytest.param('23:59', 23, 59, id='last minute of day'),
        pytest.param('00:00', 0, 0, id='first minute of day'),
    ],
)
def test__compose_datetime_from__works_on_various_time_str(
    time_str, expected_hour, expected_min, today_midnight):
    expected_datetime = today_midnight.replace(hour=expected_hour, minute=expected_min)
    assert compose_datetime_from('anything but tomorrow', time_str) == expected_datetime


@pytest.mark.parametrize(
    'time_str', ['10:', ':00', ':', '23:99', '77:00', '-14:00', '23:59aaa', '23:59:'])
def test__compose_datetime_from__fails_on_incorrect_time_strings(time_str):
    with pytest.raises(ValueError):
        compose_datetime_from('anywhen', time_str)  
