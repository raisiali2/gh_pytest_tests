import pytest

it = pytest.mark.it
describe = pytest.mark.describe
parametrize = pytest.mark.parrametrize
skip = pytest.mark.skip

@pytest.fixture
def input_value():
    input = 39
    return input

# edit test_div_by_3_6.py

