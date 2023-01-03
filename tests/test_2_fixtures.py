from typing import Iterator, List

import pytest

# -- Exercise 1 --
# Make test_fixture_sequence() pass. The test may only depend on 2 fixtures, but you can modify the dependencies of the
# following fixtures.


@pytest.fixture
def b() -> Iterator[List]:
    yield []


@pytest.fixture
def v(b: List) -> None:
    b.append("v")


@pytest.fixture
def a(b: List) -> None:
    b.append("a")


@pytest.fixture
def n(b: List) -> None:
    b.append("n")


@pytest.fixture
def t(b: List) -> None:
    b.append("t")


@pytest.fixture
def g(b: List) -> None:
    b.append("g")


@pytest.fixture
def e(b: List) -> None:
    b.append("e")


@pytest.fixture
def duplicate(b: List) -> None:
    for i in range(len(b)):
        b.append(b[i])


@pytest.fixture
def rotate_1(b: List) -> None:
    b.insert(0, b[-1])
    b.pop()


@pytest.fixture
def rotate_3(b: List) -> None:
    for i in range(3):
        b.insert(0, b[-1])
        b.pop()


def test_fixture_sequence(b: List) -> None:  # This test may depend on just 1 fixture, besides the fixture "b".
    assert b == ["v", "a", "n", "t", "a", "g", "e"]

# -- Exercise 2 --
# What happens if a fixture with a broader scope, depends on a fixture with a narrower scope?


# -- Exercise 3* --
# It's possible to pass data from a test to a fixture, so the result of a fixture depends on data in the test. Let's
# create a fixture that returns the start position of the puzzle and use it in a test. The fixture depends on the size
# of the puzzle. Documentation https://docs.pytest.org/en/6.2.x/fixture.html#using-markers-to-pass-data-to-fixtures.
