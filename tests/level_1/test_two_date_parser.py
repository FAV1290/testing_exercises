import pytest
import datetime


from functions.level_1.two_date_parser import compose_datetime_from


@pytest.mark.parametrize(
    'date_str, time_str, expected_hour, expected_minute',
    [
        ('tomorrow', '  10:00', 10, 0),
        ('today', '23:59   ', 23, 59),
        ('yesterday','  00:00  ', 0, 0),
        ('anywhen', '23:59', 23, 59),
        ('tomorrow', '00:00', 0, 0),
    ],
)
def test_compose_datetime_from(date_str, time_str, expected_hour, expected_minute):
    expected_date = datetime.date.today() + datetime.timedelta(days=int(date_str == 'tomorrow'))
    expected_result = datetime.datetime(
        expected_date.year,
        expected_date.month,
        expected_date.day,
        expected_hour,
        expected_minute,
    )
    assert compose_datetime_from(date_str, time_str) == expected_result


@pytest.mark.parametrize(
    'time_str', ['10:', ':00', ':', '23:99', '77:00', '-14:00', '23:59aaa', '23:59:'])
def test_compose_datetime_from_fails_on_time_str(time_str):
    with pytest.raises(ValueError):
        compose_datetime_from('anywhen', time_str)  
