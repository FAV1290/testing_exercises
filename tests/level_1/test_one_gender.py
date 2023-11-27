import pytest


from functions.level_1.one_gender import genderalize


@pytest.mark.parametrize(
    'verb_male, verb_female, gender, expected_result',
    [
        ('ехал', 'ехала', 'male', 'ехал'),
        ('читал', 'читала', 'female', 'читала'),
        ('спал', 'спала', 'anything else', 'спала'),
    ],
)
def test_genderalize(verb_male, verb_female, gender, expected_result):
    assert genderalize(verb_male, verb_female, gender) == expected_result
