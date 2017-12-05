# A pytest demo
# https://docs.pytest.org/en/latest/
# http://pythontesting.net/framework/pytest/pytest-introduction/
# Run:
#   python -m pytest pytest_demo.py

def func(x):
    return x + 1;

def test_should_equal():
    assert func(3) == 4

def test_should_not_equal():
    assert func(3) == 5
