
from typing import Generator, List

import pytest
from _pytest.fixtures import SubRequest

from hanoi.basics import Position

# -- Exercise 1 --
# Make test_fixture_sequence() pass. The test may only depend on 2 fixtures, but you can change the dependencies of the
# following fixtures.


@pytest.fixture
def b() -> Generator:
    yield []


@pytest.fixture
def v(b: List, e: None) -> None:
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
def g(b: List, rotate_3: None) -> None:
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


def test_fixture_sequence(b: List, rotate_1: None) -> None:  # This test may depend on just 2 fixtures.
    assert b == ["v", "a", "n", "t", "a", "g", "e"]


# -- Exercise 2 --
# What happens if a fixture with a larger scope, depends on a fixture with a smaller scope?
#
# -- Answer 2 --
# Pytest raises an error.
@pytest.fixture(scope="function")
def small_scope_fixture() -> Generator[str, None, None]:
    yield "a"


@pytest.fixture(scope="module")
def large_scope_fixture(small_scope_fixture: str) -> Generator[List[str], None, None]:
    yield [small_scope_fixture]


@pytest.mark.xfail(reason="Larger scoped fixture tries to access smaller scoped fixture.")
def test_scope_difference(large_scope_fixture: List[str]) -> None:
    assert large_scope_fixture == [a]


# -- Exercise 3 --
# It's possible to pass data from a test to a fixture, so the result of a fixture depends on data in the test. Let's
# create a fixture that returns the start position of the puzzle and use it in a test. The fixture depends on the size
# of the puzzle. Documentation https://docs.pytest.org/en/6.2.x/fixture.html#using-markers-to-pass-data-to-fixtures.
@pytest.fixture
def start_position(request: SubRequest) -> Generator[Position, None, None]:
    marker_data = request.node.get_closest_marker("number_of_disks")
    if marker_data is None:
        raise ValueError("Please mark the test with 'number_of_disks'(<n>)")
    else:
        yield Position(representation="a" * marker_data.args[0])


@pytest.mark.number_of_disks(3)
def test_start_position(start_position: Position) -> None:
    assert start_position.representation == "aaa"
