import pytest

from functions.level_1.four_bank_parser import BankCard, parse_ineco_expense


@pytest.mark.parametrize(
    'cards, estimated_card',
    [
        ([BankCard('5678', 'Ann'), BankCard('1234', 'Abby')], BankCard('1234', 'Abby')),
        ([BankCard('1234', 'Joe'), BankCard('1234', 'Vic')], BankCard('1234', 'Joe')),
    ],
)
def test__parse_ineco_expense__makes_correct_expense(cards, estimated_card, ineco_sms_and_expense):
    test_sms, expected_expense = ineco_sms_and_expense(1234).values()
    expected_expense = expected_expense._replace(card=estimated_card)
    assert parse_ineco_expense(test_sms, cards) == expected_expense


@pytest.mark.parametrize('cards', [[], [BankCard('5678', 'Ann')]])
def test__parse_ineco_expense__fails_on_list_without_target_card(cards, ineco_sms_and_expense):
    with pytest.raises(IndexError):
        parse_ineco_expense(ineco_sms_and_expense()['sms'], cards)
