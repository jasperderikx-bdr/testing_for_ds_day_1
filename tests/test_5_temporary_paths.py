import os
import re
from pathlib import Path
from typing import Generator

import pytest
from _pytest.tmpdir import TempPathFactory

from hanoi.basics import Position
from hanoi.graph import hanoi_graph
from hanoi.solve import move_is_valid, show_solution


# -- Exercise 1 --
# The code in hanoi.graph.py generates the position-graphs. It's difficult to say from the code that the output is
# correct so let's use pytest to gain more confidence.
# Write a test that checks that the moves in the bottom of the graph are valid. Do this for multiple graphs.
@pytest.mark.parametrize("number_of_disks", [2, 3, 4])
def test_moves_bottom_of_graph_are_valid(number_of_disks: int) -> None:
    graph = hanoi_graph(number_of_disks=number_of_disks)
    bottom_of_graph = graph.splitlines()[-1].strip()
    positions = re.split(pattern="-+", string=bottom_of_graph)
    for i in range(len(positions) - 1):
        assert len(positions[i]) == len(positions[i + 1])  # Check if positions have the same number of disks.

        position_comparison = [x != y for (x, y) in zip(positions[i], positions[i + 1])]
        assert sum(position_comparison) == 1  # Check if positions are exactly one character apart.

        disk_number = position_comparison.index(True)
        assert move_is_valid(position=Position(representation=positions[i]),
                             disk_number=disk_number,
                             peg=positions[i + 1][disk_number])  # Check if move between positions is valid.


# -- Exercise 2 --
# Write a test that checks that the output of the printed graph with 2 disks, is exactly as expected.
# Use the fixture tmp_path to save the graph, so you can open it after the test has completed.
def test_graph_of_2_disks(tmp_path: Path) -> None:
    graph = hanoi_graph(number_of_disks=2)

    with open(os.path.join(tmp_path, "hanoi_graph_of_2_disks.txt"), "w") as file:
        file.write(graph)  # Save file for later inspection.

    assert graph == "         aa          \n" \
                    "        /  \         \n" \
                    "       /    \        \n" \
                    "      ac----ab       \n" \
                    "     /        \      \n" \
                    "    /          \     \n" \
                    "   bc          cb    \n" \
                    "  /  \        /  \   \n" \
                    " /    \      /    \  \n" \
                    "bb----ba----ca----cc "


# -- Exercise 3 --
# Write a test that saves the printed graph for 1, ..., 4 disks in separate files and checks that the combined file size
# is smaller than 1Mb. Use the fixture tmp_path_factory to save every graph in a different folder.
def test_combined_file_size(tmp_path_factory: TempPathFactory) -> None:
    total_size = 0
    for number_of_disks in [1, 2, 3, 4]:
        graph = hanoi_graph(number_of_disks=number_of_disks)
        path = os.path.join(tmp_path_factory.mktemp(f"graph_with_{number_of_disks}_disks"), "graph.txt")
        with open(path, "w") as file:
            file.write(graph)
        total_size += os.path.getsize(path)
    assert total_size < 2 ** 20


# -- Exercise 4 --
# How is the solution visible in the graph? Use that information to write a test, to validate the output of the graph
# (from 1 to 5 disks).
@pytest.mark.parametrize("number_of_disks", [1, 2, 3, 4, 5])
def test_solution_in_graph(number_of_disks: int) -> None:
    graph = hanoi_graph(number_of_disks=number_of_disks)
    graph_lines = graph.splitlines()
    positions_per_line = [re.findall(pattern="[abc]+", string=line) for line in graph_lines]
    most_right_positions = [positions[-1] for positions in positions_per_line if positions != []]
    most_right_positions = [Position(representation=r) for r in most_right_positions]

    solution = show_solution(number_of_disks=number_of_disks)

    assert most_right_positions == solution


# -- Exercise 5 --
# Rewrite the above tests with fixtures such that all the used graphs are just generated ones. (In this case it won't
# save much time, but in general it is better to perform complex calculations just ones.)
@pytest.fixture(scope="module", autouse=True)
def hanoi_graph_cache() -> Generator[dict, None, None]:
    yield {n: hanoi_graph(number_of_disks=n) for n in [1, 2, 3, 4, 5]}
# And now replace 'hanoi_graph(number_of_disks=number_of_disks)' with 'hanoi_graph_cache[number_of_disks]' in the tests.
# Mocking hanoi_graph() in addition is also possible, but we will come to that in the next day.
