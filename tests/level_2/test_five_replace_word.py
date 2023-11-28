import pytest


from functions.level_2.five_replace_word import replace_word


@pytest.mark.parametrize(
    'text, replace_from, replace_to',
    [
        pytest.param('', 'hello', 'howdy', id='blank_text'),
        pytest.param('hello', '', 'howdy', id='blank_replace_from'),
        pytest.param('hello', 'howdy', '', id='blank_replace_to'),
        pytest.param('', '', 'bzzz', id='blank_text_and_replace_from'),
        pytest.param('', '123', '', id='blank_text_and_replace_to'),
        pytest.param('onetwo', '', '', id='blank_replace_from_and_replace_to'),
        pytest.param('', '', '', id='blank_all'),
    ],
)
def test__replace_word__keeps_text_in_blank_args_cases(text, replace_from, replace_to):
    assert replace_word(text, replace_from, replace_to) == text


@pytest.mark.parametrize(
    'text, replace_from, replace_to, expected_result',
    [
        pytest.param('Here we are', 'here', 'there', 'there we are', id='basic_success_case'),
        pytest.param('hello', 'hello', 'hi', 'hi', id='text_consists_of_replaceable_word_only'),
        pytest.param('hello', 'hi', 'howdy', 'hello', id='no_replaceable_word_in_text'),
        pytest.param(
            'A good dog deserves a good bone', 
            'good',
            'bad',
            'A bad dog deserves a bad bone',
            id='multiple_replaceable_words'
        ),
    ],
)
def test__replace_word__replaces_target_words(text, replace_from, replace_to, expected_result):
    assert replace_word(text, replace_from, replace_to) == expected_result


@pytest.mark.parametrize(
    'text, replace_from, replace_to, expected_result',
    [
        pytest.param('HELLO', 'hello', 'hi', 'hi', id='text_in_upper_case'),
        pytest.param('Hello', 'hello', 'Hi', 'Hi', id='text_capitalized'),
        pytest.param('hello', 'HELLO', 'hI', 'hI', id='replace_from_in_lower_case'),
        pytest.param('hello', 'Hello', 'HI', 'HI', id='replace_from_capitalized'),
    ],
)
def test__replace_word__is_not_case_sensitive(text, replace_from, replace_to, expected_result):
    assert replace_word(text, replace_from, replace_to) == expected_result

    
@pytest.mark.parametrize(
    'text, replace_from, replace_to',
    [
        ("Come here, let's talk", 'here', 'there'),
        ("I'm gonna go!", 'go', 'sleep'),
    ],
)
def test__replace_word__ignores_words_with_punctuation_marks(text, replace_from, replace_to):
    assert replace_word(text, replace_from, replace_to) == text


@pytest.mark.parametrize('text', [pytest.param('abc\ndef ghi', marks=pytest.mark.xfail)])
def test__replace_word__replaces_non_space_split_separators_by_spaces(text):
    text = 'abc\ndef ghi'
    assert replace_word(text, '', '') == text
