import pytest
import random

from functions.level_4.two_students import get_student_by_tg_nickname


@pytest.mark.parametrize('student_tg_account', ['test', '@test'])
def test__get_student_by_tg_nickname__gets_target_student_from_list(
    student_objects, student_tg_account):
    students = student_objects(10) + student_objects(1, student_tg_account)
    random.shuffle(students)
    assert get_student_by_tg_nickname('test', students).telegram_account == student_tg_account


def test__get_student_by_tg_nickname__returns_none_if_there_are_no_matches(student_objects):
    assert get_student_by_tg_nickname('test', student_objects(100)) is None


def test__get_student_by_tg_nickname__returns_none_for_empty_students_list_case():
    assert get_student_by_tg_nickname('test', []) is None


def test__get_student_by_tg_nickname__defines_none_and_blank_string(student_objects):
    assert get_student_by_tg_nickname('', student_objects(1, None)) is None


def test__get_student_by_tg_nickname__returns_first_match_only(student_objects):
    students = student_objects(5, 'test')
    first_student_in_list = students[0]
    assert get_student_by_tg_nickname('test', students) == first_student_in_list
