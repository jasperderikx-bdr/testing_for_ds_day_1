from hanoi.basics import Position
from typing import List


def move_disk(disk_number: int, position: Position, peg: str) -> Position:
    if move_is_valid(disk_number=disk_number, position=position, peg=peg):
        old_representation = position.representation
        new_representation = old_representation[:disk_number] + peg + old_representation[disk_number + 1:]
        return Position(new_representation)
    else:
        raise (ValueError, f"Invalid move. (Disk: {disk_number}, Position: {position}, peg: {peg}.")


def move_is_valid(disk_number: int, position: Position, peg: str) -> bool:
    return True


def next_position(current_position: Position, unused_peg: str) -> Position:
    return Position(representation="a")


def show_solution(number_of_disks: int) -> List[Position]:
    return []
