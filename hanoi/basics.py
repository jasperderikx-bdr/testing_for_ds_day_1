from __future__ import annotations


def number_of_positions(number_of_disks: int) -> int:
    return 3 ** number_of_disks


def number_of_steps_of_solution(number_of_disks: int) -> int:
    return 2 ** number_of_disks - 1


class Position:
    def __init__(self, representation: str):
        self.representation = representation
        self._is_valid()

    def _is_valid(self) -> None:
        if not isinstance(self.representation, str):
            raise (TypeError, "Representation of Position should be a string (consisting of 'a', 'b' and/or 'c').")
        if not set(self.representation).issubset("abc"):
            raise (ValueError, "Representation should solely consist of 'a', 'b' and 'c'.")

    def __str__(self):
        return self.representation

    def __eq__(self, other):
        if isinstance(other, Position):
            return self.representation == other.representation
        return False