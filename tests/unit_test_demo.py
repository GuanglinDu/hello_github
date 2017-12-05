# https://docs.python.org/3/library/unittest.html
# Run: python -m unittest unit_test_demo

import unittest

def fun(x):
    return x + 1
    
class MyTest(unittest.TestCase):
    def test_should_equal(self):
        self.assertEqual(fun(3), 4)

    def test_should_not_equal(self):
        self.assertEqual(fun(4), 10)

if __name__ == "__main__":
    unittest.main()
