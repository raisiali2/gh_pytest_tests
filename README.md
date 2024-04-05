# mark
mark is pytest plugin that has features like 
- @xfail
- @skip
- and we can give our own name to it
above features help us to run a `subset` of test such as
- `@pytest.mark.square`
- pytest -m `square` -v
in the above command -m means run as script
the square is the mark name given to the test_method
and -v mean verbose mode that show the details

# @pytest.fixture
- fixture are functions, write before each test function to which it is applied
- feed some data to the tests such as
  - database connections
  - urls 
  - and some sort of input data
- instead of the runing the same code for every test
  - attach fixture function to the tests
  - it will run and return the data to the test before executing each test
- function mark as fixture by
  - @pytest.fixture
- a test function can use fixture by mentioning the fixture name as an input parameter.
- 
```python
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
```