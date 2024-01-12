import typing
import pytest


@pytest.fixture
def good_and_bad_words() -> tuple[set, set]:
    good_words = {'pretty', 'good', 'fine', 'cool', 'thanks', 'damn'}
    bad_words = {'stupid', 'dumbass', 'lame', 'bad', 'piss off', 'damn'}
    return (good_words, bad_words)


@pytest.fixture
def stringify() -> typing.Callable:
    def cistomize_stringify_function(fraction_len: int) -> typing.Callable:
        return lambda x: f'{x:.{fraction_len}f}' if not x is None else None
    
    return cistomize_stringify_function
