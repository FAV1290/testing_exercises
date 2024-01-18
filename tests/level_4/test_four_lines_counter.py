import pytest
from unittest.mock import patch

from functions.level_4.four_lines_counter import count_lines_in


@patch('os.path.isfile', return_value=False)
def test__count_lines_in__returns_none_if_file_does_not_exist(mock_isfile):
    assert count_lines_in('non_existent_file.txt') is None


@pytest.mark.parametrize('lines', [0, 1, 2, 5, 55])
def test__count_lines_in__correctly_count_lines_in_txt_file(
    txt_file_with_fixed_lines_quantity, lines):
    assert lines >= 0, 'Lines param should be positive'
    filepath = txt_file_with_fixed_lines_quantity(lines)
    assert count_lines_in(filepath) == lines

@pytest.mark.parametrize('lines, number_sign_lines', [(5, 0), (5, 1), (5, 2), (5, 5)])  
def test__count_lines_in__skips_lines_starting_with_number_sign(
    txt_file_with_fixed_lines_quantity, lines, number_sign_lines):
    assert lines >= 0, 'Lines param should be positive'
    filepath = txt_file_with_fixed_lines_quantity(lines, number_sign_lines)
    assert count_lines_in(filepath) == lines - number_sign_lines
