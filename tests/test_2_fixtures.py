from typing import Iterator, List

import pandas as pd
import pytest


# -- Exercise 1* --
# If one fixture is (indirectly) requested multiple times for the same test, the value is cached. Make the test pass.
@pytest.fixture
def b() -> pd.DataFrame:
    yield pd.DataFrame(columns=["b"])


@pytest.fixture
def d(b: pd.DataFrame) -> None:
    b["d"] = []


@pytest.fixture
def r(b: pd.DataFrame) -> None:
    b["r"] = []


def test_bdr(b: pd.DataFrame, d: None, r: None) -> None:
    assert list(b.columns) == "?"


# -- Exercise 2 --
# What happens if a fixture with a broader scope, depends on a fixture with a narrower scope?


# -- Exercise 3* --
# It's possible to pass data from a test to a fixture, so the result of a fixture depends on data in the test. Let's
# create a fixture that returns the start position of the puzzle and use it in a test. The fixture depends on the size
# of the puzzle. Documentation https://docs.pytest.org/en/6.2.x/fixture.html#using-markers-to-pass-data-to-fixtures.


# -- Exercise 4 --
# Make test_vantage() pass. The test may only depend on 2 fixtures, but you can modify the dependencies of the other
# fixtures.
@pytest.fixture
def x() -> Iterator[List]:
    yield []


@pytest.fixture
def v(x: List) -> None:
    x.append("v")


@pytest.fixture
def a(x: List) -> None:
    x.append("a")


@pytest.fixture
def n(x: List) -> None:
    x.append("n")


@pytest.fixture
def t(x: List) -> None:
    x.append("t")


@pytest.fixture
def g(x: List) -> None:
    x.append("g")


@pytest.fixture
def e(x: List) -> None:
    x.append("e")


@pytest.fixture
def duplicate(x: List) -> None:
    for i in range(len(x)):
        x.append(x[i])


@pytest.fixture
def rotate_1(x: List) -> None:
    x.insert(0, x[-1])
    x.pop()


@pytest.fixture
def rotate_3(x: List) -> None:
    for i in range(3):
        x.insert(0, x[-1])
        x.pop()


def test_vantage(x: List) -> None:  # This test may depend on just 1 fixture, besides the fixture "x".
    assert x == ["v", "a", "n", "t", "a", "g", "e"]
