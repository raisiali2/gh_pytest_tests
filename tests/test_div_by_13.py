import pytest


it = pytest.mark.it
describe = pytest.mark.describe
parametrize = pytest.mark.parrametrize
skip = pytest.mark.skip



def test_divisible_by_13(input_value):
    assert input_value % 13 == 0

