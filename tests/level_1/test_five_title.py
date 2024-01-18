import pytest

from functions.level_1.five_title import change_copy_item


@pytest.mark.parametrize(
    'title, max_main_item_title_length, expected_title',
    [
        ('Looooooooooooooooooooooooong title', 35, 'Looooooooooooooooooooooooong title'),
        ('Copy of Looooooooooooooooooooooooong title', 50, 'Copy of Looooooooooooooooooooooooong title'),
        ('Copy of Looooooooooooooooooooooooong title', 51, 'Copy of Looooooooooooooooooooooooong title (2)'),
        ('something', 100, 'Copy of something'),
        ('something', -1000, 'something'),
        ('copy of a copy of a copy lyrics', 100, 'Copy of copy of a copy of a copy lyrics'),
        ('Copy of a copy of a copy lyrics', 100, 'Copy of a copy of a copy lyrics (2)'),
        ('something (1)', 100, 'Copy of something (1)'),
        ('something ()', 100, 'Copy of something ()'),
        ('something (abc)', 100, 'Copy of something (abc)'),
        ('Copy of something (1)', 100, 'Copy of something (2)'),
        ('Copy of something (2)', 100, 'Copy of something (3)'),
        ('Copy of something (50)', 100, 'Copy of something (51)'),
    ],
)
def test__change_copy_item__forms_correct_titles(title, max_main_item_title_length, expected_title):
    assert change_copy_item(title, max_main_item_title_length) == expected_title
