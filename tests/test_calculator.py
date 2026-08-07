import pytest

from calculator import Calculator


class TestCalculate:
    calc = Calculator()

    def test_summa(self):
        assert self.calc.summa(3, 0) == 3
        assert self.calc.summa(3, 3) == 6
        assert self.calc.summa(3, -3) == 0
        assert self.calc.summa(-3, -3) == -6
        assert self.calc.summa(2, 3) == 5

    def test_minus(self):
        assert self.calc.minus(3, 0) == 3
        assert self.calc.minus(3, 3) == 0
        assert self.calc.minus(3, -3) == 6
        assert self.calc.minus(-3, -3) == 0
        assert self.calc.minus(2, 3) == -1

    def test_minus_reverse(self):
        assert self.calc.minus(3, 0, True) == -3
        assert self.calc.minus(3, 3, True) == 0
        assert self.calc.minus(3, -3, True) == -6
        assert self.calc.minus(-3, -3, True) == 0
        assert self.calc.minus(2, 3, True) == 1
