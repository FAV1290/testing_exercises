import pytest
import datetime
from decimal import Decimal


from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense


@pytest.mark.parametrize(
    'cards, estimated_card',
    [
        pytest.param([], None, marks=pytest.mark.xfail),
        pytest.param([BankCard('5678', 'Ann')], None, marks=pytest.mark.xfail),
        ([BankCard('1234', 'Joe'), BankCard('5678', 'Ann')], BankCard('1234', 'Joe')),
        ([BankCard('1234', 'Joe'), BankCard('1234', 'Vic')], BankCard('1234', 'Joe')),
    ],
)
def test_parse_ineco_expense(cards, estimated_card):
    test_sms_text = ''.join([
        'E-commerce approved 4.99 USD, ',
        '8023********1234 20.11.23 10:20 Spotify authcode 555555 Balance: 23.30 USD',
    ])
    test_sms = SmsMessage(test_sms_text, 'InecoBank', datetime.datetime.now())
    expected_spent_at = datetime.datetime.strptime('20.11.23 10:20', '%d.%m.%y %H:%M')
    expected_expense = Expense(Decimal('4.99'), estimated_card, 'Spotify', expected_spent_at)
    assert parse_ineco_expense(test_sms, cards) == expected_expense
