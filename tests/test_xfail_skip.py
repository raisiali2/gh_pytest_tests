# a test is not relevant for some time due to some reason.
# a new feature is being implemented and we already added a test for that feature

# in this case:
# 1. xfail the test: pytest execute but will not considered as part failed or passed tests.
#    details of this test will not printed even if test fail.
#     @pytest.mark.xfail
# 2. skip the test: means test will not be executed 
    # @pytest.mark.skip

import pytest

@pytest.mark.xfail
@pytest.mark.great
def test_greater():
    num = 100
    assert num > 100

@pytest.mark.xfail
@pytest.mark.great
def test_greater_equal():
    num = 100
    assert num >= 100

@pytest.mark.skip
@pytest.mark.others
def test_less():
    num = 100
    assert num < 200
    