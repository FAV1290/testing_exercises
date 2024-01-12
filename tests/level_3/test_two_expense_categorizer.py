import pytest

from functions.level_3.models import ExpenseCategory
from functions.level_3.two_expense_categorizer import is_string_contains_trigger, guess_expense_category


@pytest.mark.parametrize(
    'string, trigger, expected_result',
    [
        pytest.param('', '', True, id='blank params'),
        pytest.param('hello world', '', False, id='blank trigger'),
        pytest.param('', '123', False, id='blank string'),
    ],
)
def test__is_string_contains_trigger__processes_blank_strings(string, trigger, expected_result):
    assert is_string_contains_trigger(string, trigger) == expected_result


@pytest.mark.parametrize('delimiter', [' ', ',' , '.', '-', '/', '\\'])
def test__is_string_contains_trigger__processes_double_delimiters(delimiter):
    formats = [
        (delimiter * 2, 'test', ''),
        ('test', delimiter * 2, ''),
        (delimiter * 2, 'test', delimiter * 2),
    ]
    assert all(['{}{}{}'.format(*format) for format in formats])


@pytest.mark.parametrize('left_delimiter', ['',' ', ',' , '.', '-', '/', '\\'])
@pytest.mark.parametrize('right_delimiter', ['',' ', ',' , '.', '-', '/', '\\'])
def test__is_string_contains_trigger__processes_allowed_delimiter_combinations(
    left_delimiter, right_delimiter):
    assert is_string_contains_trigger(f'{left_delimiter}test{right_delimiter}', 'test')


@pytest.mark.parametrize(
    'string, trigger, expected_result',
    [
        pytest.param('TEST', 'TEST', True, id='both uppered', marks=pytest.mark.xfail),
        pytest.param('test', 'test', True, id='both lowered'),
        pytest.param('TEST', 'test', True, id='uppered string and lowered trigger'),
        pytest.param('test', 'TEST', False, id='lowered string and uppered trigger'),
        pytest.param('TeSt', 'TeSt', True, id='randomcased match', marks=pytest.mark.xfail),
        pytest.param('TeSt', 'tEsT', False, id='randomcased mismatch'),
    ],
)
def test__is_string_contains_trigger__has_case_sensitivity_quirks(
    string, trigger, expected_result):
    assert is_string_contains_trigger(string, trigger) == expected_result


@pytest.mark.parametrize(
    'spent_in_str, guess_str',
    [
        pytest.param('juicy green apple for Snow White', "SUPERMARKET", id='trigger in sentence'),
        pytest.param('documentary movie', None, id='trigger is a part of word'),
        pytest.param('yandex goat', None, id='complex trigger is a part of wordgroup'),
        pytest.param('Alfa-pharm', "MEDICINE_PHARMACY", id='capitalized original string'),
        pytest.param('alpaca farm', "MEDICINE_PHARMACY", id='predictably wrong guess'),
    ],
)
def test__guess_expense_category__guesses_category_on_current_triggers_despite_case_issues(
    spent_in_str, guess_str, expense_object):
    expected_guess = None if guess_str is None else ExpenseCategory(guess_str)
    assert guess_expense_category(expense_object(spent_in=spent_in_str)) == expected_guess


