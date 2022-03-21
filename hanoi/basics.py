import warnings


def number_of_positions(number_of_disks: int) -> int:
    pass


def number_of_steps_of_solution(number_of_disks: int) -> int:
    pass


class Position:
    def __init__(self, representation: str):
        self.representation = representation
        self._warn_ambitious_players()

    def _warn_ambitious_players(self) -> None:
        if len(self.representation) > 100:
            warnings.warn("Are you sure you want to get involved with such a challenge?")

    def __str__(self):
        return self.representation

    def __eq__(self, other):
        if isinstance(other, Position):
            return self.representation == other.representation
        return False
