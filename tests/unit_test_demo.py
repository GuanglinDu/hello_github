# https://docs.python.org/3/library/unittest.html
# python -m unit_test -h
# Run:
# 1. python unit_test_demo.py
# 2. python unit_test_demo.py -v
# 3. python -m unittest unit_test_demo
# 3. python -m unittest  -v unit_test_demo

# Test Discovery:
# python -m unittest discover -s project_directory -p "test_*.py" -v
# python -m unittest discover project_directory "test_*.py" -v

import unittest

def fun(x):
    return x + 1
    
class MyTest(unittest.TestCase):
    def test_should_equal(self):
        self.assertEqual(fun(3), 4)

    def test_should_not_equal(self):
        self.assertNotEqual(fun(4), 10)

if __name__ == "__main__":
    unittest.main()
