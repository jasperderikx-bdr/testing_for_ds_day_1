from typing import List

from hanoi.basics import Position


def move_disk(disk_number: int, position: Position, peg: str) -> Position:
    if move_is_valid(disk_number=disk_number, position=position, peg=peg):
        old_representation = position.representation
        new_representation = old_representation[:disk_number] + peg + old_representation[disk_number + 1:]
        return Position(new_representation)
    else:
        raise ValueError(f"Invalid move. (Disk: {disk_number}, Position: {position}, peg: {peg}.")


def move_is_valid(disk_number: int, position: Position, peg: str) -> bool:
    return True


def next_position(current_position: Position, unused_peg: str) -> Position:
    """Returns the only possible new Position, given the current Position and the unused peg.

    Given any Position and a peg that is not used for the next move. There is only one possible move left. Because
    one of the disks on top of the remaining two pins, is larger than the other.
    """
    return Position(representation="a")


def show_solution(number_of_disks: int) -> List[Position]:
    """Returns a list of Positions of the fastest route from the start Position 'aa...a' to the end Position 'cc...c'.

    Looking at the position graph from the slides, can you find the solution Path? What pattern can you find considering
    the unused peg for each step in the solution?
    """
    return []
