import pytest
from unittest.mock import patch

from functions.level_4.three_promocodes import generate_promocode


@pytest.mark.parametrize('code_len', [0, -1, -2, -5, -55])
def test__genegate_promocode__returns_blank_string_for_zero_and_negative_len_argument(code_len):
    assert generate_promocode(-1) == ''


@patch('random.choice', return_value='A')
def test__genegate_promocode__returns_eight_len_code_in_no_arguments_case(mock_choice):
    assert generate_promocode() == 'AAAAAAAA'


@patch('random.choice', return_value='B')
@pytest.mark.parametrize('code_len', [1, 2, 3, 10, 20])
def test__genegate_promocode__returns_adjusted_len_codes(mock_choice, code_len):
    assert generate_promocode(code_len) == 'B' * code_len
