# A pytest demo
# https://docs.pytest.org/en/latest/
# http://pythontesting.net/framework/pytest/pytest-introduction/
# Run:
#   python -m pytest pytest_demo.py

def func(x):
    return x + 1;

def test_answer():
    assert func(3) == 5
