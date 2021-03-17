from g0_code.main_functions import sum_values


class TestCalculator:
    def test_addition(self):
        assert 4 == sum_values(2, 2), "Sum is not working right"
