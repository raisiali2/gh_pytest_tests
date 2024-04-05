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
