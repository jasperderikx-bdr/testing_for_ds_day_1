from __future__ import annotations


def number_of_positions(number_of_disks: int) -> int:
    return 3 ** number_of_disks


def number_of_steps_of_solution(number_of_disks: int) -> int:
    return 2 ** number_of_disks - 1


pegs = {"a", "b", "c"}


def move_disk(disk_number: int, position: Position, peg: str) -> Position:
    if move_is_valid(disk_number=disk_number, position=position, peg=peg):
        old_representation = position.representation
        new_representation = old_representation[:disk_number] + peg + old_representation[disk_number + 1:]
        return Position(new_representation)
    else:
        raise (ValueError, f"Invalid move. (Disk: {disk_number}, Position: {position}, peg: {peg}.")


def move_is_valid(disk_number: int, position: Position, peg: str) -> bool:
    peg_of_disk = position.representation[disk_number]
    if disk_number == position.representation.rfind(peg_of_disk):  # Check if given disk is on top of pile.
        if disk_number > position.representation.rfind(peg):  # Check if disk may be placed on top of the pile of peg.
            return True
    return False


class Position:
    def __init__(self, representation: str):
        self.representation = representation
        self._is_valid()

    def _is_valid(self) -> None:
        if not isinstance(self.representation, str):
            raise (TypeError, "Representation of Position should be a string (consisting of 'a', 'b' and/or 'c').")
        if not set(self.representation).issubset(pegs):
            raise (ValueError, "Representation should solely consist of 'a', 'b' and 'c'.")

    def __str__(self):
        return self.representation

    def __eq__(self, other):
        if isinstance(other, Position):
            return self.representation == other.representation
        return False


def next_position(current_position: Position, unused_peg: str) -> Position:
    disk_on_top_of_peg_a = current_position.representation.rfind("a")
    disk_on_top_of_peg_b = current_position.representation.rfind("b")
    disk_on_top_of_peg_c = current_position.representation.rfind("c")
    if unused_peg == "a":
        if disk_on_top_of_peg_b < disk_on_top_of_peg_c:
            return move_disk(disk_on_top_of_peg_c, current_position, "b")
        else:
            return move_disk(disk_on_top_of_peg_b, current_position, "c")
    if unused_peg == "b":
        if disk_on_top_of_peg_a < disk_on_top_of_peg_c:
            return move_disk(disk_on_top_of_peg_c, current_position, "a")
        else:
            return move_disk(disk_on_top_of_peg_a, current_position, "c")
    if unused_peg == "c":
        if disk_on_top_of_peg_a < disk_on_top_of_peg_b:
            return move_disk(disk_on_top_of_peg_b, current_position, "a")
        else:
            return move_disk(disk_on_top_of_peg_a, current_position, "b")


def show_solution(number_of_disks: int):
    start_position = Position(number_of_disks * "a")
    end_position = Position(number_of_disks * "c")
    parity_n = number_of_disks % 2
    print(start_position)
    current_position = start_position

    if parity_n == 0:
        unused_peg, = "c"
        next_unused_peg = {"a": "c", "b": "a", "c": "b"}
    else:
        unused_peg, = "b"
        next_unused_peg = {"a": "b", "b": "c", "c": "a"}

    while current_position != end_position:
        current_position = next_position(current_position, unused_peg)
        unused_peg = next_unused_peg[unused_peg]
        print(current_position)