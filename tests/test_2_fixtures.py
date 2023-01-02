from typing import Iterator, List

import pytest
from _pytest.fixtures import FixtureRequest

from hanoi.basics import Position

# -- Exercise 1 --
# Make test_fixture_sequence() pass. The test may only depend on 2 fixtures, but you can modify the dependencies of the
# following fixtures.


@pytest.fixture
def b() -> Iterator[List]:
    yield []


@pytest.fixture
def v(b: List, rotate_3: None) -> None:
    b.append("v")


@pytest.fixture
def a(b: List) -> None:
    b.append("a")


@pytest.fixture
def n(b: List, duplicate: None) -> None:
    b.append("n")


@pytest.fixture
def t(b: List, n: None) -> None:
    b.append("t")


@pytest.fixture
def g(b: List, rotate_1: None) -> None:
    b.append("g")


@pytest.fixture
def e(b: List, g: None) -> None:
    b.append("e")


@pytest.fixture
def duplicate(b: List, a: None) -> None:
    for i in range(len(b)):
        b.append(b[i])


@pytest.fixture
def rotate_1(b: List, v: None) -> None:
    b.insert(0, b[-1])
    b.pop()


@pytest.fixture
def rotate_3(b: List, t: None) -> None:
    for i in range(3):
        b.insert(0, b[-1])
        b.pop()


def test_fixture_sequence(b: List, e: None) -> None:  # This test may depend on just 1 fixture, besides the fixture "b".
    assert b == ["v", "a", "n", "t", "a", "g", "e"]


# -- Exercise 2 --
# What happens if a fixture with a broader scope, depends on a fixture with a narrower scope?
@pytest.fixture(scope="class")
def narrower_fixture() -> Iterator[str]:
    yield "narrow"


@pytest.fixture(scope="module")
def broader_fixture(narrower_fixture: str) -> Iterator[str]:
    yield f"broader depends on {narrower_fixture}"


@pytest.mark.xfail(reason="Broader fixture requests narrower fixture.", run=True, strict=True)
def test_fixture_scopes(broader_fixture: str) -> None:
    assert type(broader_fixture) == str


# -- Exercise 3 --
# It's possible to pass data from a test to a fixture, so the result of a fixture depends on data in the test. Let's
# create a fixture that returns the start position of the puzzle and use it in a test. The fixture depends on the size
# of the puzzle. Documentation https://docs.pytest.org/en/6.2.x/fixture.html#using-markers-to-pass-data-to-fixtures.
# Finally, make sure to register your mark.
@pytest.fixture()
def start_position(request: FixtureRequest) -> Position:
    number_of_disks = request.node.get_closest_marker("number_of_disks").args[0]
    return Position(number_of_disks * "a")


@pytest.mark.number_of_disks(3)
def test_start_position(start_position: Position) -> None:
    assert start_position == Position("aaa")
