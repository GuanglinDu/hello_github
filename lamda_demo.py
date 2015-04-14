# Jun. 5, 2014 Sat.
# See Yet Another Lambda Tutorial, http://pythonconquerstheuniverse.wordpress.com/2011/08/29/lambda_tutorial/
# Basically, Python's lambda is a tool for building functions (or more precisely,
# function objects). That means that Python has two tools for building functions:
# def and lambda. Used to define a one line function.

import math

def square_root(x):
    return math.sqrt(x)
    
# or you can use lambda:

square_root2 = lambda x: math.sqrt(x)

# def sum(x,y):
#    return x + y
sum = lambda x, y:    x + y

def epic(c, s):
    oneLineFunc = lambda c, s: c+s
    print oneLineFunc(c, s)
     
x = 16.0
print "The root of %f is %f" % (x, square_root(x))
print "The root of %f is %f" % (x, square_root2(x))

x, y = 1.0, 2.0
print "%f + %f = %f" % (x, y, sum(x, y))

epic(4, 2)
