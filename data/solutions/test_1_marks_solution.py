import datetime
import multiprocessing

import pytest

from hanoi.basics import Position, number_of_positions, number_of_steps_of_solution


# -- Exercise 1 --
# How many positions does the Tower of Hanoi have for n disks? Implement your answer in number_of_positions() in
# hanoi/basics.py and make sure the following test passes.
def test_number_of_positions() -> None:
    number_of_disks = 1
    result = number_of_positions(number_of_disks=number_of_disks)
    expected_result = 3
    assert result == expected_result


# -- Exercise 2 --
# Write a test to find out what happens if you implement two tests with the same name.
#
# -- Answer 2 --
# You overwrite the test and only the last definition is executed.

# -- Exercise 3 --
# Write a test to find out whether code after the assert-line is executed.
# Does this depend on the outcome of the assertion?
#
# -- Answer 3 --
# The code continues after an assert-line, except when the assert-line raises an error.
# It's best practice to use exactly 1 assert-line per test.

# -- Exercise 4 --
# Implement number_of_steps_of_solution() in hanoi/basics.py, which returns the number of steps it takes to solve the
# Tower of Hanoi with n disks. Write a test with multiple asserts, that checks if your implementation is correct if the
# number of disks is 1, 2 or 3.
def test_number_of_steps_of_solution() -> None:
    assert number_of_steps_of_solution(1) == 1
    assert number_of_steps_of_solution(2) == 3
    assert number_of_steps_of_solution(3) == 7


# -- Exercise 5 --
# Write a test that checks whether the solution for 1000 disks takes more than 1000 steps. But use marks to skip it if
# the number of available cpus is less than 32.
@pytest.mark.skipif(condition=multiprocessing.cpu_count() < 32, reason="Not enough cpus.")
def test_over_1000() -> None:
    assert number_of_steps_of_solution(1000) > 1000


# -- Exercise 6 --
# If you call number_of_steps_of_solution() with a string as input, it probably raises an error. For now, we don't know
# how to handle this properly, so mark the test as a failure.
@pytest.mark.xfail(reason="String raises error", raises=TypeError, run=False, strict=False)
def test_wrong_input() -> None:
    number_of_steps_of_solution(number_of_disks="12")  # type: ignore


# -- Exercise 7 --
# The following test, raises a warning. Because we purposely want to test a long position, let pytest ignore the warning
# using pytest.marks.filterwarnings (https://docs.pytest.org/en/6.2.x/reference.html#pytest-mark-filterwarnings)
@pytest.mark.filterwarnings("ignore:.*challenge.*:")
def test_long_position() -> None:
    Position(101 * "a")


# -- Exercise 8 --
# According to a legend, the biggest version of this puzzle is situated in the Kashi Vishwanath Temple in India.
# Priests have started moving around the 64 golden disks in 1780 and once they are finished the earth will vanish.
# Write a test that warns us (so let the test fail) if the priests will finish within 100 years from now. Assume the
# priests can move 1 disk per second.
def test_legend() -> None:
    start_day = datetime.date(1780, 1, 1)
    today = datetime.date.today()
    seconds_in_100_years = 100 * 365 * 24 * 60 * 60
    boundary = (today - start_day).total_seconds() + seconds_in_100_years
    assert number_of_steps_of_solution(64) > boundary


# -- Exercise 9 --
# Mark all tests with a new mark: "mark_paragraph" in one go. Make sure to register the mark.
pytestmark = pytest.mark.mark_paragraph
