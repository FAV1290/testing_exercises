import pytest

from functions.level_4.one_brackets import delete_remove_brackets_quotes


@pytest.mark.parametrize(
    'name, expected_result',
    [
        pytest.param('{ test }', 'test', id='simple case'),
        pytest.param('{test}', 'es', id='symbols near brackets will be removed too'),
        pytest.param('{test', 'e', id='only let bracket is required'),
        pytest.param('}test}', '}test}', id='right bracket is meaningless'),
        pytest.param('1', '1', id='one symbol name wont raise an exception'),
        pytest.param('{', '', id='even one left bracket wont raise an exception'),
        pytest.param('{{123}}', '123', id='double brackets will be deleted'),
        pytest.param('{{ 123 }}', ' 123 ', id='but spaces after double brackets will not'),
        pytest.param(' {test} ', ' {test} ', id='lstripped name required to remove brackets'),
    ],
)
def test__delete_remove_brackets_quotes__removes_brackets(name, expected_result):
    assert delete_remove_brackets_quotes(name) == expected_result


def test__delete_remove_brackets_quotes__raises_exception_for_blank_str():
    with pytest.raises(IndexError):
        assert delete_remove_brackets_quotes('')

