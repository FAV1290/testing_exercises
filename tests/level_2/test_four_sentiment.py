import pytest


from functions.level_2.four_sentiment import check_tweet_sentiment


@pytest.mark.parametrize(
    'text, good_words, bad_words, expected_result',
    [
        pytest.param('', set(), set(), None, id='all_blank'),
        pytest.param('\n', {'wonderful'}, {'filthy'}, None, id='blank_text'),
        pytest.param('hello', set(), {'filthy'}, None, id='blank_good_words'),
        pytest.param('wonderful day', {'wonderful'}, set(), 'GOOD', id='blank_bad_words'),   
    ],
)
def test__check_tweet_sentiment__with_blank_args(text, good_words, bad_words, expected_result):
    assert check_tweet_sentiment(text, good_words, bad_words) == expected_result 


@pytest.mark.parametrize(
    'text, expected_result',
    [
        pytest.param("He's damn lucky", None, id='same_word_in_two_sets'),
        pytest.param('Pretty good lame dumbass', None, id='equality_of_good_and_bad_words'),
        pytest.param('Hello world', None, id='neither_good_nor_bad_words'),
        pytest.param('Very good advice, thanks', 'GOOD', id='no_bad_words'),
        pytest.param('You are stupid lame dumbass, piss off!', 'BAD', id='no_good_words'),
        pytest.param("Thanks for help with stupid laptop, it's fine", 'GOOD', id='more_good_words'),
        pytest.param('This dumbass is pretty bad at math', 'BAD', id='more_bad_words'),
    ],
)
def test__check_tweet_sentiment__works_for_different_good_to_bad_ratios(text, expected_result):
    good_words = set(['pretty', 'good', 'fine', 'cool', 'thanks', 'damn'])
    bad_words = set(['stupid', 'dumbass', 'lame', 'bad', 'piss off', 'damn'])
    assert check_tweet_sentiment(text, good_words, bad_words) == expected_result


@pytest.mark.parametrize('text', ['Good', 'Bad', 'good', 'bad'])
def test__check_tweet_sentiment__requires_lowered_set_elements(text):
    assert check_tweet_sentiment(text, set(['Good']), set(['Bad'])) is None


def test__check_tweet_sentiment__does_not_count_words_with_punctuation_marks():
    good_words = set(['fine'])
    bad_words = set(['lame', 'bad'])
    text = 'Framework is bad, but fine for lame developers'
    assert check_tweet_sentiment(text, good_words, bad_words) != 'Bad'
