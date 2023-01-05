import pytest

from hanoi.basics import Position
from hanoi.solve import move_disk, move_is_valid, next_position, show_solution


# -- Exercise 1* --
# Implement move_is_valid() in hanoi/solve.py to make the following test pass.
def test_move_is_valid() -> None:
    position = Position(representation="aba")
    assert not move_is_valid(disk_number=0, position=position, peg="c")


# -- Exercise 2 --
# If you parametrize 2 variables in 2 separate pytest.mark.parametrize lines. You get all possible combinations.
# Use this to test in multiple situations that you can always move the smallest disk.
@pytest.mark.parametrize("representation", ["aaa", "abcba", "acacac"])
@pytest.mark.parametrize("peg", ["a", "b", "c"])
def test_always_move_smallest_disk(representation: str, peg: str) -> None:
    last_disk_number = len(representation) - 1
    assert move_is_valid(disk_number=last_disk_number, position=Position(representation), peg=peg)


# -- Exercise 3* --
# Test that move_disk() informs the user what the disk, position and peg were when a move is invalid.
def test_informative_error_message() -> None:
    with pytest.raises(expected_exception=ValueError) as exception_info:
        move_disk(disk_number=0, position=Position(representation="aba"), peg="c")
    assert "0" in str(exception_info.value)
    assert "aba" in str(exception_info.value)
    assert "c" in str(exception_info.value)


# -- Exercise 4 --
# The class Position should validate the representation of the position, after an instance is created. It should raise a
# TypeError if the input is not a string, and a ValueError if the string contains characters other than "a", "b", or
# "c". Add this functionality to the class and write 2 tests, one for each error.
def test_position_with_wrong_type() -> None:
    with pytest.raises(expected_exception=TypeError):
        Position(1)  # type: ignore


def test_position_with_wrong_character() -> None:
    with pytest.raises(expected_exception=ValueError):
        Position("d")


# -- Exercise 5* --
# The class Position can warn the user. Test that the warning message contains "challenge".
# For documentation see: https://docs.pytest.org/en/6.2.x/warnings.html#warns.
def test_challenging_warning() -> None:
    with pytest.warns(UserWarning, match='challenge'):
        Position(101 * "a")


# -- Exercise 6 --
# Implement next_position() in hanoi/solve.py and write at least one test.
def test_next_position() -> None:
    assert next_position(current_position=Position("aaaaa"), unused_peg="b") == Position("aaaac")


# -- Exercise 7 --
# Implement show_solution() in hanoi/solve.py and write at least one test.
def test_show_solution() -> None:
    assert show_solution(number_of_disks=2) == [Position("aa"), Position("ab"), Position("cb"), Position("cc")]
