"""Tests for calculator module."""
import pytest
from src.calculator import add, subtract, multiply, divide


class TestAdd:
    def test_positive_numbers(self):
        assert add(2, 3) == 5

    def test_negative_numbers(self):
        assert add(-1, -1) == -2

    def test_mixed_numbers(self):
        assert add(-1, 1) == 0


class TestSubtract:
    def test_positive_numbers(self):
        assert subtract(5, 3) == 2

    def test_negative_result(self):
        assert subtract(3, 5) == -2


class TestMultiply:
    def test_positive_numbers(self):
        assert multiply(3, 4) == 12

    def test_by_zero(self):
        assert multiply(5, 0) == 0


class TestDivide:
    def test_positive_numbers(self):
        assert divide(10, 2) == 5.0

    def test_division_by_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)


from src.calculator import power


class TestPower:
    def test_positive_exponent(self):
        assert power(2, 3) == 8

    def test_zero_exponent(self):
        assert power(5, 0) == 1

    def test_negative_exponent(self):
        assert power(2, -1) == 0.5

    def test_float_result(self):
        assert power(4, 0.5) == 2.0

    def test_base_zero(self):
        assert power(0, 5) == 0

    def test_base_zero_negative_exponent(self):
        with pytest.raises(ValueError, match="Cannot raise 0 to a negative power"):
            power(0, -1)


from src.calculator import modulo


class TestModulo:
    def test_positive_numbers(self):
        assert modulo(10, 3) == 1

    def test_even_division(self):
        assert modulo(10, 5) == 0

    def test_negative_dividend(self):
        assert modulo(-10, 3) == 2  # Python modulo behavior

    def test_float_inputs(self):
        assert abs(modulo(5.5, 2.0) - 1.5) < 1e-9

    def test_divisor_zero(self):
        with pytest.raises(ValueError, match="Cannot compute modulo with divisor zero"):
            modulo(10, 0)
