import pytest


# -- Exercise 1 --
# Make test_fixture_sequence() pass. The test may only depend on 2 fixtures, but you can change the dependencies of the
# following fixtures.

@pytest.fixture
def b():
    yield []


@pytest.fixture
def v(b):
    b.append("v")


@pytest.fixture
def a(b):
    b.append("a")


@pytest.fixture
def n(b):
    b.append("n")


@pytest.fixture
def t(b):
    b.append("t")


@pytest.fixture
def g(b):
    b.append("g")


@pytest.fixture
def e(b):
    b.append("e")


@pytest.fixture
def duplicate(b):
    for i in range(len(b)):
        b.append(b[i])


@pytest.fixture
def rotate_1(b):
    b.insert(0, b[-1])
    b.pop()


@pytest.fixture
def rotate_3(b):
    for i in range(3):
        b.insert(0, b[-1])
        b.pop()


def test_fixture_sequence(b):  # This test may only depend on 2 fixtures, so "b" and only 1 other fixture.
    assert b == ["v", "a", "n", "t", "a", "g", "e"]


# -- Exercise 2 --
# What happens if a fixture with a larger scope, depends on a fixture with a smaller scope?


# -- Exercise 3 --
# It's possible to pass data from a test to a fixture, so the result of a fixture depends on data in the test. For
# example let's create a fixture that returns the start position of the puzzle. Off course this depends on the size of
# the puzzle. See documentation https://docs.pytest.org/en/6.2.x/fixture.html#using-markers-to-pass-data-to-fixtures.
