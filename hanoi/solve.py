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
    disk_is_on_top = position.representation[disk_number] not in position.representation[disk_number + 1:]
    disk_stays_on_top = peg not in position.representation[disk_number + 1:]
    return disk_is_on_top and disk_stays_on_top


def next_position(current_position: Position, unused_peg: str) -> Position:
    """Returns the only possible new Position, given the current Position and the unused peg.

    Given any Position and a peg that is not used for the next move. There is only one possible move left. Because
    one of the disks on top of the other two pins, is larger than the other.
    """
    other_pegs = list({"a", "b", "c"} - {unused_peg})
    disk_on_top_of = dict()
    for peg in other_pegs:
        disk_on_top_of[peg] = current_position.representation.rfind(peg)
    if disk_on_top_of[other_pegs[0]] < disk_on_top_of[other_pegs[1]]:  # weird because larger index means smaller disk.
        return move_disk(disk_number=disk_on_top_of[other_pegs[1]], position=current_position, peg=other_pegs[0])
    else:
        return move_disk(disk_number=disk_on_top_of[other_pegs[0]], position=current_position, peg=other_pegs[1])


def show_solution(number_of_disks: int) -> List[Position]:
    """Returns a list of Positions of the fastest route from the start Position 'aa...a' to the end Position 'cc...c'.

    Looking at the position graph from the slides, can you find the solution Path? What pattern can you find considering
    the unused peg for each step in the solution?
    """
    start_position = Position(number_of_disks * "a")
    solution = [start_position]
    if number_of_disks % 2 == 0:
        unused_peg = "c"
        next_unused_peg = {"a": "c", "b": "a", "c": "b"}
    else:
        unused_peg = "b"
        next_unused_peg = {"a": "b", "b": "c", "c": "a"}

    while solution[-1] != Position(number_of_disks * "c"):
        solution.append(next_position(current_position=solution[-1], unused_peg=unused_peg))
        unused_peg = next_unused_peg[unused_peg]
    return solution
