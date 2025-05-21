import pytest

def calculate_discount(price, percentage):
    return price - price * (percentage / 100)

class TestDiscountCaculation:
    def test_ten_percent_discount(self):
        result = calculate_discount(100, 10)
        assert result == 90.0 # Assertion
