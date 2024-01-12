import pytest

from functions.level_2.three_first import first, NOT_SET


@pytest.mark.parametrize('items, expected_result', [([5, 4, 3], 5) ,([1, 1, 1], 1) ,([0], 0)])
def test__first__works_fine_for_filled_items(items, expected_result):
    assert first(items) == expected_result


@pytest.mark.parametrize('default, expected_result', [(None, None), (1, 1), (-5, -5), (0, 0)])
def test__first__works_fone_for_empty_items_and_set_default(default, expected_result):
    assert first([], default=default) == expected_result


def test__first__raises_error_on_empty_items_and_not_set_default():
    with pytest.raises(AttributeError):
        assert first([], NOT_SET)


def test__first__returns_str_despite_annotation():
    assert isinstance(first([], 'hello'), str)
