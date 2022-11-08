import calc


class TestCalc:

    def test_div_numbers(self):
        result = calc.div_numbers(10, 5)
        assert result == 2

    def test_mul_numbers(self):
        result = calc.mul_numbers(10, 5)
        assert result == 50

    def test_add_numbers(self):
        result = calc.add_numbers(10, 5)
        assert result == 14
