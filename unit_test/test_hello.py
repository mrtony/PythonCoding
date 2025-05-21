import pytest

def calculate_discount(price, percentage):
    return price - price * (percentage / 100)

def add(x, y):
    return x + y

@pytest.mark.parametrize("x, y, expected", [
    (2, 3, 5),
    (0, 0, 0),
    (1, 1, 2),
])

def test_add(x, y, expected):
    result = add(x, y)
    assert result == expected

@pytest.fixture
def sample_data():
    data = [1, 2, 3, 4, 5]
    return data

class TestDiscountCaculation:
    def test_ten_percent_discount(self):
        result = calculate_discount(100, 10)
        assert result == 90.0 # Assertion



def test_sum(sample_data):
    assert sum(sample_data) == 15