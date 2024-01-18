import typing
import pytest
import datetime
from decimal import Decimal
from random import randint, choice

from functions.level_1.four_bank_parser import SmsMessage, Expense, BankCard


@pytest.fixture
def today_midnight() -> datetime.datetime:
    return datetime.datetime.now().replace(second=0, microsecond=0)


@pytest.fixture
def ineco_sms_and_expense() -> typing.Callable:
    def create_ineco_sms_and_expense(
        last_card_digits: int|None = None,
    ) -> dict[str, SmsMessage | Expense]:
        random_usd_sum_str = lambda: f'{randint(1, 5000)}.{randint(10, 99):02d}'
        last_card_digits = randint(0, 9999) if last_card_digits is None else last_card_digits

        expense_sum_str = random_usd_sum_str()
        last_card_digits_str = f'{(abs(last_card_digits) % 10000):04d}'
        spent_at = datetime.datetime.now().replace(second=0, microsecond=0)
        spent_in = choice(['Spotify', 'Digital Ocean', 'OnlyFans', 'EBay', 'Yerevan City'])
        authcode_str = f'{randint(0, 999999):06d}'
        sms_text = ''.join([
            f'E-commerce approved {expense_sum_str} USD, 8023********{last_card_digits_str} ',
            f'{spent_at.strftime("%d.%m.%y %H:%M")} {spent_in} ',
            f'authcode {authcode_str} Balance: {random_usd_sum_str()} USD',
        ])
        
        ineco_sms = SmsMessage(sms_text, 'InecoBank', spent_at)
        ineco_expense = Expense(Decimal(expense_sum_str), BankCard('', ''), spent_in, spent_at)
        return {'sms': ineco_sms, 'expense': ineco_expense}
    
    return create_ineco_sms_and_expense
