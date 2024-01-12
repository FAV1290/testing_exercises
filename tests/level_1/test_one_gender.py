import pytest

from functions.level_1.one_gender import genderalize


@pytest.mark.parametrize(
    'male_verb, female_verb, gender_str, expected_result',
    [
        ('ехал', 'ехала', 'male', 'ехал'),
        ('читал', 'читала', 'female', 'читала'),
        ('спал', 'спала', 'anything else', 'спала'),
    ],
)
def test__genderalize__returns_correct_verb(male_verb, female_verb, gender_str, expected_result):
    assert genderalize(male_verb, female_verb, gender_str) == expected_result
