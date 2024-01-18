import typing
import pytest
import datetime
from decimal import Decimal
from random import choice, randint

from functions.level_3.models import Expense, Currency, BankCard, ExpenseCategory


@pytest.fixture
def expense_object() -> typing.Callable:
    def compose_random_expense(
        amount: Decimal | None = None,
        currency: Currency | None = None,
        card: BankCard | None = None,
        spent_in: str | None = None,
        spent_at: datetime.datetime | None = None,
    ) -> Expense:

        with open('tests/level_3/first_names.txt', 'r') as file_handler:
            first_names = file_handler.readlines()
        with open('tests/level_3/last_names.txt', 'r') as file_handler:
            last_names = file_handler.readlines()
        with open('tests/level_3/spent_ins.txt', 'r') as file_handler:
            spent_ins = file_handler.readlines()

        random_spent_in = choice(spent_ins).rstrip()
        random_name = f'{choice(first_names).rstrip()} {choice(last_names).rstrip()}'

        return Expense(
            amount=round(Decimal(randint(0, 10000) / 100) if amount is None else amount, 2),
            currency=currency or choice(list(Currency)),
            card=card or BankCard(last_digits=f'{randint(0, 9999):04d}', owner=random_name),
            spent_in=random_spent_in if spent_in is None else spent_in,
            spent_at=spent_at or datetime.datetime.now(),
            category=choice(list(ExpenseCategory) + [None]),
        )

    return compose_random_expense


@pytest.fixture
def expense_objects(expense_object: typing.Callable) -> typing.Callable:
    def create_expenses_list(
        quantity: int = 1,
        amounts_seq: list[Decimal] = [],
        currencies_seq: list[Currency] = [],
        spent_ins_seq: list[str] = [],
        spent_ats_seq: list[datetime.datetime] = [],
    ) -> list[Expense]:
        
        expenses = []
        for index in range(quantity):
            kwargs_to_sequences_map = {
                'amount': amounts_seq,
                'currency': currencies_seq,
                'spent_in': spent_ins_seq,
                'spent_at': spent_ats_seq
            }
            expense_kwargs = {}
            for kwarg, sequence in kwargs_to_sequences_map.items():
                expense_kwargs[kwarg] = sequence[index % len(sequence)] if sequence else None
            expenses.append(expense_object(**expense_kwargs))
        return expenses
    
    return create_expenses_list
