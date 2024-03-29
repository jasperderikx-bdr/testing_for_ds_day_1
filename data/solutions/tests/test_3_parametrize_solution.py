import pytest

from hanoi.basics import number_of_positions


# -- Exercise 1* --
# Test the output of def number_of_positions() from hanoi/basics.py, parametrizing over number_of_disks.
@pytest.mark.parametrize("number_of_disks, expected_number_of_positions", [(1, 3), (2, 9), (3, 27)])
def test_number_of_positions(number_of_disks: int, expected_number_of_positions: int) -> None:
    assert number_of_positions(number_of_disks=number_of_disks) == expected_number_of_positions


# -- Exercise 2 --
# What happens to the test_ids of parametrized tests? (Use ```pytest --collect-only```.)
# Find out what "ids" does, when used in pytest.mark.parametrize(... ids= ...).
@pytest.mark.parametrize("number_of_disks", [1, 2, 3], ids=["small", "medium", "large"])
def test_parameter_with_ids(number_of_disks: int) -> None:
    assert True


# -- Exercise 3* --
# Mark all tests in this file with a new mark: "parametrization_paragraph", using only one line of code. Make sure to
# register the mark.
pytestmark = pytest.mark.parametrization_paragraph


# -- Exercise 4 --
# Create a fixture and parametrize it with two values. Use this fixture to run every test in this paragraph twice
# -without- modifying the tests.
@pytest.fixture(autouse=True, params=["real_world", "parallel_universe"])
def dummy_fixture() -> None:
    pass
