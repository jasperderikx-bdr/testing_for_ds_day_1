from hanoi.basics import Position
from hanoi.solve import move_is_valid


# -- Exercise 1 --
# Implement move_is_valid() in hanoi/solve.py to make the following test pass.
def test_move_is_valid() -> None:
    position = Position(representation="aba")
    assert not move_is_valid(disk_number=0, position=position, peg="c")


# -- Exercise 2 --
# If you parametrize 2 variables in 2 separate pytest.mark.parametrize lines. You get all possible combinations.
# Use this to test in multiple situations that you can always move the smallest disk.


# -- Exercise 3* --
# Test that move_disk() informs the user what the disk, position and peg were when a move is invalid.


# -- Exercise 4 --
# The class Position should validate the representation of the position, after an instance is created. It should raise a
# TypeError if the input is not a string, and a ValueError if the string contains characters other than "a", "b", or
# "c". Add this functionality to the class and write 2 tests, one for each error.


# -- Exercise 5* --
# The class Position can warn the user. Test that the warning message contains "challenge".
# For documentation see: https://docs.pytest.org/en/6.2.x/warnings.html#warns.


# -- Exercise 6 --
# Implement next_position() in hanoi/solve.py and write at least one test.


# -- Exercise 7 --
# Implement show_solution() in hanoi/solve.py and write at least one test.
