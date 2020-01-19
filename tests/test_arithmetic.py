import pytest
import example_pkg.arithmetic as arithmetic


def test_add():
    assert arithmetic.add(2, 3) == 5


def test_subtract():
    assert arithmetic.subtract(2, 3) == -1


def test_multiply():
    assert arithmetic.multiply(4, 5) == 20


def test_divide():
    assert arithmetic.divide(4, 8) == pytest.approx(0.5)
