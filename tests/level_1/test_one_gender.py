import pytest


from functions.level_1.one_gender import genderalize


@pytest.mark.parametrize(
    'gender, expected_verb_index',
    [('male', 0), ('female', 1), ('attack_helicopter', 1)],
)
def test_genderalize(gender, expected_verb_index):
    verbs = ('some_male_verb', 'some_female_verb')
    assert genderalize(*verbs, gender) == verbs[expected_verb_index]
