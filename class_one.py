# Jun. 21, 2014 Sat.
# class_one.py
# See http://www.afterhoursprogramming.com/tutorial/Python/Introduction/
# Various tutorials: https://wiki.python.org/moin/BeginnersGuide/Programmers

""" define class to simulate a simple calculator """
class Calculator(object):
    def __init__(self):
        # Start with zero
        self.current = 0
    
    def add(self, amount):
        # add number to current
        self.current += amount
    
    def getCurrent(self):
        return self.current

# Use the class
from class_one import *
myBuddy = Calculator()
myBuddy.add(2)
sum1 = myBuddy.getCurrent()
# Why print 2 times?
print("sum = %i" % sum1)
#print(myBuddy.getCurrent())
