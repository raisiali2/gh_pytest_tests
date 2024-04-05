# parametrizing is to run the test against multiple sets of inputs
# we cand do it using following
# @pytest.mark.parametrize

import pytest


it = pytest.mark.it
describe = pytest.mark.describe
parametrize = pytest.mark.parrametrize
skip = pytest.mark.skip

@pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,35),(4,44)])

def test_multiplication_11(num, output):
    assert 11*num == output

