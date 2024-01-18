

import pytest
from decimal import Decimal
from statistics import StatisticsError
from datetime import datetime, timedelta, timezone

from functions.level_3.models import Currency
from functions.level_3.one_avg_daily_expenses import calculate_average_daily_expenses


def test__calculate_average_daily_expenses__raises_error_for_blank_expenses_list():
    with pytest.raises(StatisticsError):
        assert calculate_average_daily_expenses([])
        

def test__calculate_average_daily_expenses__ignore_currencies(expense_object):
    amd_expense = expense_object(amount=Decimal(100), currency=Currency.AMD)
    usd_expense = expense_object(amount=Decimal(100), currency=Currency.USD)
    assert calculate_average_daily_expenses([amd_expense, usd_expense]) == Decimal(200)   


@pytest.mark.parametrize('decimal_base', [0, -1])
def test__calculate_average_daily_expenses__works_for_null_and_negative_amounts(
    expense_object, decimal_base):
    expenses = [expense_object(Decimal(decimal_base))]
    assert calculate_average_daily_expenses(expenses) == Decimal(decimal_base)


@pytest.mark.parametrize(
    'test_datetime', 
    [
        pytest.param(datetime.now() - timedelta(weeks=105556), id='prehistoric_date'),
        pytest.param(datetime.now() + timedelta(weeks=105556), id='far future date'),
        pytest.param(datetime.now(timezone.utc) + timedelta(days=1), id='aware dt among unaware'),
    ],
)
def test__calculate_average_daily_expenses_works_on_weird_spent_at_expenses(
    expense_object, expense_objects, test_datetime):
    ok_expenses = expense_objects(4, [Decimal(1)])
    weird_expense = expense_object(Decimal(8), spent_at=test_datetime)
    assert calculate_average_daily_expenses(ok_expenses + [weird_expense]) == Decimal(6)


@pytest.mark.parametrize('expenses_list_len', [1, 2, 5, 10, 50])
def test__calculate_average_daily_expenses__works_for_positive_expenses_list_length(
    expense_objects, expenses_list_len):
    expenses = expense_objects(expenses_list_len, [Decimal(1)])
    assert calculate_average_daily_expenses(expenses) == Decimal(expenses_list_len)


@pytest.mark.parametrize('unique_dates_quantity', [1, 2, 5, 10, 50])
def test__calculate_average_daily_expenses__works_for_various_dates_quantity(
    expense_object, unique_dates_quantity):
    gauss_mean = (unique_dates_quantity + 1) / 2
    expenses = []
    for delta in range(1, unique_dates_quantity + 1): 
        new_spent_at = datetime.now() + timedelta(days=delta)
        new_expense = expense_object(Decimal(delta), spent_at=new_spent_at)
        expenses.append(new_expense)
    assert calculate_average_daily_expenses(expenses) == Decimal(gauss_mean)
