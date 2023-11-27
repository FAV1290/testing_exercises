import pytest


from functions.level_1.three_url_builder import build_url


@pytest.mark.parametrize(
    'host_name, relative_url, get_params, expected_url',
    [
        ('', '', None, '/'),
        ('http://test.com', 'items', {'item': '10'}, 'http://test.com/items?item=10'),
        ('1', '2', {'3': '4'}, '1/2?3=4'),
        ('test.am', 'index.php', {'one': '1', 'two': '2'}, 'test.am/index.php?one=1&two=2'),
    ],
)
def test_build_url(host_name, relative_url, get_params, expected_url):
    assert build_url(host_name, relative_url, get_params) == expected_url
