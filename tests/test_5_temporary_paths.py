import pytest

from hanoi.basics import Position
from hanoi.graph import hanoi_graph
from hanoi.solve import move_is_valid


# -- Exercise 1 --
# The code in hanoi/graph.py generates the position-graphs. It's difficult to say from the code that the output is
# correct so let's use pytest to gain more confidence.
# Write a test that checks that the moves in the bottom of the graph are possible. Do this for multiple graphs.
@pytest.mark.parametrize("number_of_disks", [1, 2, 3])
def test_moves_on_bottom_are_valid(number_of_disks: int) -> None:
    graph = hanoi_graph(number_of_disks=number_of_disks)
    bottom_row = graph.split("\n")[-1]
    positions = [Position(x.strip()) for x in bottom_row.split("-")]
    for i in range(len(positions) - 1):
        disk_number = 1
        assert move_is_valid(position=positions[i], disk_number=disk_number, peg="a")

# -- Exercise 2* --
# Write a test that checks that the output of the printed graph with 2 disks, is exactly as expected.
# Use the fixture tmp_path to save the graph, so you can open it after the test has completed.


# -- Exercise 3 --
# Write a test that saves the printed graph for 1, ..., 4 disks in separate files and checks that the combined file size
# is smaller than 1Kb. Use the fixture tmp_path_factory.


# -- Exercise 4 --
# How is the solution visible in the graph? Use that information to write a test, to validate the output of the graph
# (from 1 to 5 disks).


# -- Exercise 5 --
# Rewrite the above tests with fixtures such that all the used graphs are just generated ones.
