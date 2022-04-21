from typing import Generator

import pytest
from _pytest.fixtures import SubRequest

from hanoi.basics import Position, number_of_positions, number_of_steps_of_solution


# -- Exercise 1 --
# Test the output of def number_of_positions() from hanoi/basics.py, parametrizing over number_of_disks.
@pytest.mark.parametrize("number_of_disks, expected", [(1, 3), (2, 9), (3, 27)])
def test_number_of_positions(number_of_disks: int, expected: int) -> None:
    assert number_of_positions(number_of_disks) == expected


# -- Exercise 2 --
# What happens to the test_ids of parametrized tests? (Use ```pytest --collect-only```.)
# Find out what "ids" does, when used in pytest.mark.parametrize(... ids= ...).
#
# -- Answer 2 --
# When using parametrize, the test-ids are extended with the values of the parameters. You can explicitly change the
# test-ids yourself with the 'ids' parameter.
@pytest.mark.parametrize("number_of_disks, expected", [(1, 1), (2, 3), (3, 7)], ids=["case_1", "case_2", "case_3"])
def test_number_of_steps_of_solution(number_of_disks: int, expected: int) -> None:
    assert number_of_steps_of_solution(number_of_disks) == expected


# -- Exercise 3 --
# Again, create a fixture that returns the start position of the puzzle but now parametrize the fixture such that it
# covers test cases for the tower of Hanoi up to 5 discs.
# Test that the starting position only consists of "a".
@pytest.fixture(params=[1, 2, 3, 4, 5])
def start_position(request: SubRequest) -> Generator[Position, None, None]:
    yield Position(representation="a" * request.param)


def test_start_position(start_position: Position) -> None:
    assert set(start_position.representation) == {"a"}


# For more advanced parametrization examples see: https://docs.pytest.org/en/stable/example/parametrize.html.
