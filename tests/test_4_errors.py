import pytest

from src.math_functions import increment


def test_exercise_0() -> None:
    # Make this test pass, by changing the value of expected_result.
    x = 10
    result = increment(x)
    expected_result = 5
    assert result == expected_result


def test_exercise_1() -> None:
    # To avoid unexpected behaviour, we want the function increment to raise an error when the input is a boolean.
    # The test is written correctly. Make it pass, by changing the implementation of function increment.
    increment(True)
    with pytest.raises(expected_exception=TypeError):
        increment(True)
