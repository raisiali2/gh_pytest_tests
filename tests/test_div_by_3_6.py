import pytest


it = pytest.mark.it
describe = pytest.mark.describe
parametrize = pytest.mark.parrametrize
skip = pytest.mark.skip


def test_divisible_by_3(input_value):
    assert input_value % 3 == 0

def test_divisible_by_6(input_value):
    assert input_value % 6 == 0

# note: that fixture has limitation that we can use within this test file and can not use out of this test file
# because of scope limitation
# if we want to use a fixture in multiple test file then we need to define it inside
# conftest.py file