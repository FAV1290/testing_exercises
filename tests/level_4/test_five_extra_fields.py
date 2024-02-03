import pytest
from unittest.mock import patch

from functions.level_4.five_extra_fields import (
    fetch_extra_fields_configuration, fetch_app_config_field)


@pytest.mark.parametrize('filepath', ['non_existent_file.ini', '', 'something'])
def test__fetch_app_config_field__returns_none_for_non_existent_file(filepath):
    assert fetch_app_config_field(filepath, 'any_field') is None


def test__fetch_app_config_field__returns_none_for_non_existent_field(config_file):
    filepath = config_file('tool:app-config', {'some_field': 'some_value'})
    assert fetch_app_config_field(filepath, 'non_existent_field') is None


def test__fetch_app_config_field__returns_none_for_non_existent_field(config_file):
    filepath = config_file(
        'tool:app-config', {'first_field': 'first_value', 'second_field': 'second_value'})
    assert all([
        fetch_app_config_field(filepath, 'first_field') == 'first_value',
        fetch_app_config_field(filepath, 'second_field') == 'second_value',
    ])


@pytest.mark.parametrize('filepath', ['non_existent_file.ini', '', 'something'])
def test__fetch_extra_fields_configuration__returns_black_mapping_for_non_existent_file(filepath):
    assert fetch_extra_fields_configuration(filepath) == {}


@pytest.mark.parametrize(
    'return_value, expected_result',
    [
        (
            'first_extra_field: 200',
            {'first_extra_field': 200},
        ),
        (
            'first_extra_field: 2 * 100\nsecond_extra_field: 3+3',
            {'first_extra_field': 200, 'second_extra_field': 6},
        ),
        (
            '  first_extra_field: chr(80)\nsecond_extra_field: "string".capitalize()',
            {'first_extra_field': 'P', 'second_extra_field': 'String'},
        ),
        (
            '',
            {},
        ),
    ],
)
def test__fetch_extra_fields_configuration__returns_correct_mapping(return_value, expected_result):
    mocked_function_str = 'functions.level_4.five_extra_fields.fetch_app_config_field'
    with patch(mocked_function_str) as mock_fetch_app_config_field:
        mock_fetch_app_config_field.return_value = return_value
        assert fetch_extra_fields_configuration('') == expected_result
