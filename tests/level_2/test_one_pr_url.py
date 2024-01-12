from pytest import mark, param

from functions.level_2.one_pr_url import is_github_pull_request_url


@mark.parametrize(
    'url, expected_result',
    [
        param('https://github.com/FAV1290/py_game_test/pull/2', True, id='correct_1'),
        param('https://github.com/learnpythonru/testing_exercises/pull/2', True, id='correct_2'),
        param('', False, id='blank_url'),
        param('github.com/FAV1290/py_game_test/pull/2', False, id='url_without_protocol'),
        param('https://github.com/learnpythonru/testing_exercises', False, id='wrong_subdir'),
        param('ftp://github.com/learnpythonru/exercises/pulls', False, id='wrong_protocol'),
        param('https://pornhub.com/learnpythonru/hello_world/pull/18', False, id='wrong_domain'),
    ],
)
def test__is_github_pull_request_url__passes_correct_and_denies_wrong_urls(url, expected_result):
    assert is_github_pull_request_url(url) == expected_result
