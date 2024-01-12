import random
import pytest
from datetime import datetime

from functions.level_3.three_is_subscription import is_subscription


def test__is_subscription__does_not_considers_annual_payments_as_subscriptions(expense_objects):
    expenses = expense_objects(
        quantity=5,
        spent_ins_seq=['annual_payment'],
        spent_ats_seq=[datetime.now().replace(year=n) for n in range(2024, 2029)],
    )
    assert not is_subscription(expenses[0], expenses)


@pytest.mark.xfail
def test__is_subscription__gives_false_positive_result_on_multi_year_history(expense_object):
    first_expense = expense_object(spent_in='test', spent_at=datetime(2023, 1, 1))
    far_from_first_expense = expense_object(spent_in='test', spent_at=datetime(2033, 2, 2))
    far_from_second_expense = expense_object(spent_in='test', spent_at=datetime(2043, 3, 3))
    history = [first_expense, far_from_first_expense, far_from_second_expense]
    assert not is_subscription(first_expense, history)


@pytest.mark.xfail
def test__is_subscription__denies_subscriptions_with_long_cross_year_history(
    expense_object, expense_objects):
    monthly_expenses = expense_objects(
        12, spent_ins_seq=['test'], spent_ats_seq=[datetime(2023, n, 25) for n in range(1, 13)])
    thirteens_expense = expense_object(spent_in='test', spent_at=datetime(2024, 1, 25))
    expenses = monthly_expenses + [thirteens_expense]
    assert is_subscription(expenses[0], expenses) or is_subscription(expenses[-1], expenses)


@pytest.mark.parametrize('expenses_quantity, gap_months,', [(10, 1), (5, 2), (3, 3)])
def test__is_subscription__locates_obvious_subscriptions(
    expenses_quantity, gap_months, expense_objects):
    assert expenses_quantity * gap_months < 13, 'expenses_quantity * gap_months should be >= 12'
    expenses = expense_objects(
        quantity=expenses_quantity,
        spent_ins_seq=['definitely_subscription'],
        spent_ats_seq=[datetime.now().replace(month=n) for n in range(1, 13, gap_months)]
    )
    assert is_subscription(expenses[0], expenses)


def test__is_subscription__finds_subcription_in_big_history_array(expense_objects):
    random_expenses_mass = expense_objects(100)
    subscription_expenses = expense_objects(
        3, spent_ins_seq=['spotify'], spent_ats_seq=[datetime(2023, n, 10) for n in range(3, 6)])
    history = random_expenses_mass + subscription_expenses
    random.shuffle(history)
    assert is_subscription(subscription_expenses[0], history)
