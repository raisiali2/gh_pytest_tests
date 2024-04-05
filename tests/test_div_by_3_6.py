import pytest

@pytest.fixture
def input_value():
    input = 39
    return input
# above is fixture function named input_value, which supplies the input to the tests
# to access finxture function, the tests have to mention the fixture name as input parameter.
# pytest while the test is getting executed, will see the fixture name as input parameter.
# it then executes the fixture function and the returned value is stored to the input parameter, which can be used by the test

def test_divisible_by_3(input_value):
    assert input_value % 3 == 0

def test_divisible_by_6(input_value):
    assert input_value % 6 == 0

# note: that fixture has limitation that we can use within this test file and can not use out of this test file
# because of scope limitation
# if we want to use a fixture in multiple test file then we need to define it inside
# conftest.py file