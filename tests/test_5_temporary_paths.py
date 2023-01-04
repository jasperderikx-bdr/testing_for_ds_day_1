import os
from pathlib import PosixPath

import pytest
from _pytest.tmpdir import TempPathFactory

from hanoi.basics import Position
from hanoi.graph import hanoi_graph
from hanoi.solve import move_disk


# -- Exercise 1 --
# The code in hanoi/graph.py generates the position-graphs. It's difficult to say from the code that the output is
# correct so let's use pytest to gain more confidence.
# Write a test that checks that the moves in the bottom of the graph are possible. Do this for multiple graphs.
@pytest.mark.parametrize("number_of_disks", [1, 2, 3, 4])
def test_moves_on_bottom_are_possible(number_of_disks: int) -> None:
    graph = hanoi_graph(number_of_disks=number_of_disks)
    bottom_row = graph.split("\n")[-1]
    positions = [Position(x.strip()) for x in bottom_row.split("-") if x != ""]
    for i in range(len(positions) - 1):
        comparison = [x == y for (x, y) in zip(positions[i].representation, positions[i + 1].representation)]
        disk_number = comparison.index(False)
        peg = positions[i + 1].representation[disk_number]
        new_position = move_disk(position=positions[i], disk_number=disk_number, peg=peg)
        assert new_position == positions[i + 1]


# -- Exercise 2* --
# Write a test that checks that the output of the printed graph with 2 disks, is exactly as expected.
# Use the fixture tmp_path to save the graph, so you can open it after the test has completed.
def test_hanoi_graph_2(tmp_path: PosixPath) -> None:
    graph_2 = hanoi_graph(number_of_disks=2)
    with open(tmp_path / "hanoi_graph_2.txt", "w") as file:
        print(graph_2, file=file)
    assert graph_2 == "         aa          \n" \
                      "        /  \\         \n" \
                      "       /    \\        \n" \
                      "      ac----ab       \n" \
                      "     /        \\      \n" \
                      "    /          \\     \n" \
                      "   bc          cb    \n" \
                      "  /  \\        /  \\   \n" \
                      " /    \\      /    \\  \n" \
                      "bb----ba----ca----cc "


# -- Exercise 3 --
# Write a test that saves the printed graph for 1, ..., 4 disks in separate files and checks that the combined file size
# is smaller than 1Kb. Use the fixture tmp_path_factory.
def test_combined_file_size(tmp_path_factory: TempPathFactory) -> None:
    total = 0
    for number_of_disks in [1, 2, 3, 4]:
        path = tmp_path_factory.mktemp(f"file_size_{number_of_disks}") / "file.txt"
        with open(path, "w") as file:
            print(hanoi_graph(number_of_disks=number_of_disks), file=file)
        total += os.path.getsize(path)

    assert total < 2 ** 20  # == 1 MB


# -- Exercise 4 --
# How is the solution visible in the graph? Use that information to write a test, to validate the output of the graph
# (from 1 to 5 disks).
@pytest.mark.parametrize("number_of_disks", [1, 2, 3, 4, 5])
def test_solution_in_graph(number_of_disks: int) -> None:
    graph = hanoi_graph(number_of_disks=number_of_disks)
    print(graph)

# -- Exercise 5 --
# Rewrite the above tests with fixtures such that all the used graphs are just generated ones.
