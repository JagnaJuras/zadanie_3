import factorial

class TestFactorial:

    def test_fact(self):
        result = factorial.fac_number(5)
        assert result == 120
        

