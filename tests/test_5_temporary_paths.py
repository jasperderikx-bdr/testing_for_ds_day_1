# -- Exercise 1 --
# The code in hanoi.graph.py generates the position-graphs. It's difficult to say from the code that the output is
# correct so let's use pytest to feel more confident about the code.
# Write a test that checks the moves in the bottom of the graph are valid. Do this for multiple graphs.


# -- Exercise 2 --
# Write a test that checks that the output of the printed graph with 2 disks, is exactly as expected.
# Use the fixture tmp_path, to save the graph so you can open it after the test has completed.


# -- Exercise 3 --
# Write a test that checks that the combined file size is smaller than 1Kb, for the printed graph for 1, ..., 4 disks.
# Use the fixture tmp_path_factory.


# -- Exercise 4 --
# How is the solution visible in the graph? Use that information to write a test, to validate the output of the graph
# (from 1 to 5 disks).


# -- Exercise 5 --
# Rewrite the above tests with fixtures such that all the used graphs are just generated ones.
