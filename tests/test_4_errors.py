from typing import Union

import pytest

from hanoi.basics import Position
from hanoi.solve import move_disk, move_is_valid, next_position, show_solution


# -- Exercise 1 --
# Implement move_is_valid() in hanoi/solve.py to make the following test pass.
def test_move_is_valid() -> None:
    position = Position(representation="aba")
    assert not move_is_valid(disk_number=0, position=position, peg="c")


# -- Exercise 2 --
# If you parametrize 2 variables in 2 separate pytest.mark.parametrize lines. You get all possible combinations.
# Use this to test in multiple situations that you can always move the smallest disk.
@pytest.mark.parametrize("position_representation", ["aaa", "abcabc", "b"])
@pytest.mark.parametrize("peg", ["a", "b", "c"])
def test_smallest_disk_can_always_be_moved(position_representation: str, peg: str) -> None:
    position = Position(representation=position_representation)
    disk_number_smallest_disk = len(position_representation) - 1
    assert move_is_valid(disk_number=disk_number_smallest_disk, position=position, peg=peg)


# -- Exercise 3 --
# Test that move_disk() informs the user what the disk, position and peg were when a move is invalid.
def test_move_disk_error_message() -> None:
    disk_number = 0
    position = Position(representation="aa")
    peg = "b"

    with pytest.raises(expected_exception=ValueError) as exception_info:
        move_disk(disk_number=disk_number, position=position, peg=peg)

    assert str(disk_number) in str(exception_info.value)
    assert position.representation in str(exception_info.value)
    assert peg in str(exception_info.value)


# -- Exercise 4 --
# The class Position should validate the representation of the position, after an instance is created. It should raise a
# TypeError if the input is not a string, and a ValueError if the string contains characters other than "a", "b", or
# "c". Add this functionality to the class and write 2 tests, one for each error.
@pytest.mark.parametrize("wrong_input", [True, 0, ("a", "b", "a")])
def test_position_raise_error_on_wrong_input_type(wrong_input: Union[bool, int, tuple]) -> None:
    with pytest.raises(expected_exception=TypeError):
        Position(representation=wrong_input)  # type: ignore


@pytest.mark.parametrize("wrong_input", ["123", "representation", "aaad"])
def test_position_raise_error_on_wrong_notation(wrong_input: str) -> None:
    with pytest.raises(expected_exception=ValueError):
        Position(representation=wrong_input)


# -- Exercise 5 --
# The class Position can warn the user. Test that the warning message contains "challenge".
# For documentation see: https://docs.pytest.org/en/6.2.x/warnings.html#warns.
def test_position_warn_on_large_representation() -> None:
    with pytest.warns(UserWarning, match=r"challenge"):
        Position(101 * "a")


# -- Exercise 6 --
# Moving a disk in the Tower of Hanoi always concerns two pegs, and leaves the third one unused. Looking at it from
# another angle: knowing which peg will be left untouched, there is actually only one valid move remaining. For example
# let's look at the Tower of Hanoi represented by "cbacb" (naming the pegs of disks 0, 1, 2, 3 and 4 in order), and the
# unused peg will be "c". Now, peg "a" contains disk 2 and peg "b" contains disk 1 and 4. Moving disk 2 from "a" to "b"
# is not allowed, because disk 2 is greater than disk 4. So, the only move that is left is moving disk 4 from "b" to "a"
# which results in: "cbaca".
# Implement next_position() in hanoi/solve.py and write at least one test.
def test_next_position() -> None:
    result = next_position(current_position=Position(representation="cbacb"), unused_peg="c")
    expected_result = Position(representation="cbaca")
    assert result == expected_result


# -- Exercise 7 --
# The graph of al possible positions is shown in the slides. The path from "aa...a" to "cc...c" shows the moves of the
# solution. As described in the previous exercise, each move can be described with the peg that is unused. Do you
# recognize a pattern in the sequence of unused pegs? Use that pattern to implement show_solution() in hanoi/solve.py
# and write at least one test.
def test_show_solution() -> None:
    result = show_solution(number_of_disks=3)
    expected_result = [Position(representation=r) for r in ["aaa", "aac", "abc", "abb", "cbb", "cba", "cca", "ccc"]]
    assert result == expected_result
