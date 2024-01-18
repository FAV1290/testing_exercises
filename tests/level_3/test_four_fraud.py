import pytest
import random
from decimal import Decimal
from datetime import datetime, timedelta

from functions.level_3.models import Currency
from functions.level_3.four_fraud import find_fraud_expenses


def test__find_fraud_expenses__finds_fraud_expenses_among_others(expense_objects):
    fraud_expenses = expense_objects(
        5, amounts_seq=[Decimal(1)], spent_ins_seq=['fraud'], spent_ats_seq=[datetime.now()])
    background_expenses = expense_objects(
        100, spent_ats_seq=[datetime.now() - timedelta(weeks=n) for n in range(1,101)])
    history = fraud_expenses + background_expenses
    random.shuffle(history)
    assert set(find_fraud_expenses(history)) == set(fraud_expenses)


def test__find_fraud_expenses__ignores_exchange_rates_for_multi_currency_accounts(expense_objects):
    fraud_kwargs = {
        'quantity': 4,
        'amounts_seq': [Decimal(5000)],
        'currencies_seq': [currency for currency in Currency],
        'spent_ins_seq': ['test'],
        'spent_ats_seq': [datetime(2024, 1, 1)]}
    multi_currency_expenses = expense_objects(**fraud_kwargs)
    assert set(find_fraud_expenses(multi_currency_expenses)) == set(multi_currency_expenses)


def test__find_fraud_expenses__cleans_fraud_expenses_with_even_microsecond_shift(expense_objects):
    fraud_kwargs = {
        'quantity': 5,
        'amounts_seq': [Decimal(1)],
        'spent_ins_seq': ['fraud'],
        'spent_ats_seq': [datetime(2024, 1, 1, 0, 0, 0, n + 1) for n in range(5)],
    }
    history = expense_objects(**fraud_kwargs)
    assert not find_fraud_expenses(history)
