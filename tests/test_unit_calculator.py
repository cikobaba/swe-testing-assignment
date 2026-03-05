import pytest
from quick_calc import calculator


def test_add_integers():
    assert calculator.add(5, 3) == 8


def test_subtract_integers():
    assert calculator.subtract(10, 4) == 6


def test_multiply_integers():
    assert calculator.multiply(6, 7) == 42


def test_divide_integers():
    assert calculator.divide(20, 4) == 5


def test_divide_by_zero_raises():
    with pytest.raises(calculator.DivisionByZeroError):
        calculator.divide(10, 0)


def test_negative_numbers_subtraction():
    assert calculator.subtract(-5, -2) == -3


def test_decimal_addition():
    assert calculator.add(0.1, 0.2) == pytest.approx(0.3)


def test_large_number_multiplication():
    assert calculator.multiply(10**12, 3) == 3 * 10**12