import pytest


from functions.level_2.two_square_equation import solve_square_equation


@pytest.mark.parametrize(
    'coefficients, expected_result',
    [
        pytest.param((2, 5.0, -3), ('-3.00', '0.50'), id='basic_case_one'),
        pytest.param((4, 21, 5), ('-5.00', '-0.25'), id='basic_case_two'),
        pytest.param((3, -10, 3), ('0.33', '3.00'), id='basic_case_three'),
        pytest.param((1, 2, 1), ('-1.00', '-1.00'), id='zero_discriminant'),
        pytest.param((1.5, 4.3, 1.9), ('-0.55', '-2.32'), id='coefs_with_fraction'),
        pytest.param((0, 1, 30.56), ('-30.56', None), id='square_nulled'),
        pytest.param((1, 0, -9), ('-3.00', '3.00'), id='linear_nulled'),
        pytest.param((1, 1, 0), ('-1.00', '0.00'), id='const_nulled'),
        pytest.param((0, 1, 0), ('0.00', None), id='square_and_const_nulled'),
        pytest.param((1, 0, 0), ('0.00', '0.00'), id='linear_and_const_nulled'),
        pytest.param((0, 0, 5), (None, None), id='square_and_linear_nulled'),
        pytest.param((1, 1, 1), (None, None), id='equal_coefficients'),
    ],
)
def test__solve_square_equation__works_for_elevated_discriminants_and_at_least_one_non_nulled_coef(
    coefficients,
    expected_result,
):
    stringify = lambda x: f'{x:.2f}' if not x is None else None
    stringified_solutions = tuple(map(stringify, solve_square_equation(*coefficients)))
    assert set(stringified_solutions) == set(expected_result)


def test__solve_square_equation__rounds_solutions_with_long_fraction():
    stringify = lambda x: f'{x:.18f}' if not x is None else None
    stringified_solutions = tuple(
        map(stringify, solve_square_equation(0, 2, 1.000000000000000088)))
    assert set(stringified_solutions) != set(['-0.500000000000000044', None])


@pytest.mark.parametrize('coefficients', [(1, -6, 34), (2, 4, 7.84)])
def test__solve_square_equation__returns_none_for_negative_discriminants(coefficients):
    assert solve_square_equation(*coefficients) == (None, None)


@pytest.mark.xfail(reason='we_get_none_instead_of_infinite_solutions')
def test__solve_square_equation__returns_none_in_infinite_solutions_cases():
    assert solve_square_equation(0, 0, 0) != (None, None)
