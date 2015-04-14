# datatypes_demo.py
# 2013/08/23 13:58:27

import fractions


# 2.3.5 Numbers In A Boolean Context, Dive into Python 3
# Due to some legacy issues left over from Python 2, booleans can be treated as numbers. True is 1; False is 0. 
def is_it_true(anything):
    if anything:
        print("yes, it's true")
    else:
        print("no, it's false")


# In a boolean context, non-zero integers are true; 0 is false.
if __name__ == '__main__':
    is_it_true(1)
    is_it_true(-1)
    is_it_true(0)
    is_it_true(0.1)
    is_it_true(0.0)
    is_it_true(fractions.Fraction(1, 2))
    is_it_true(fractions.Fraction(0, 1))
