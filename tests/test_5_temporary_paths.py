from hanoi.graph import hanoi_graph

# -- Exercise 1 --
# The code in hanoi.graph.py generates the position graphs. It's difficult to say from the code that the output is
# correct so let's use pytest to gain more confidence.
# Write a test that checks that the moves in the bottom of the graph are valid. Do this for multiple graphs.


# -- Exercise 2 --
# This test checks that the output of the printed graph with 2 disks, is exactly as expected. Extend the test such that
# it saves the graph, so you can open it after the test has completed. Use the fixture tmp_path.
def test_graph_of_2_disks() -> None:
    graph = hanoi_graph(number_of_disks=2)
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


# -- Exercise 4 --
# How is the solution of the tower of Hanoi visible in the graph? Use that information to write a test, to validate the
# output of the graph (from 1 to 5 disks).


# -- Exercise 5 --
# Rewrite the above tests with fixtures such that all the used graphs are just generated ones. (In this case it won't
# save much time, but in general it is better to perform complex calculations just ones.)
