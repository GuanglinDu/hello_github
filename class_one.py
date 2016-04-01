# Jun. 21, 2014 Sat.
# class_one.py
# See http://www.afterhoursprogramming.com/tutorial/Python/Introduction/
# Various tutorials: https://wiki.python.org/moin/BeginnersGuide/Programmers

class Calculator(object):
	
    """Defines a class to simulate a simple calculator"""
    def __init__(self):
        """The constructor"""
        self.result = 0 # defines a variable
        self.greeting = "Hello, Python!"
    
    def add(self, amount):
        """Defines a method of the class"""
        # add number to result
        self.result += amount
    
    def get_result(self):
        """Returns the value of variable result"""
        return self.result

# Use the class in another file by importing it
#from class_one import * # No need to import in the same module(=file)

# Like function main() in C
if __name__ == "__main__":
    # Creates an object
    cal = Calculator()

    # Accesses the variables directly from the object
    print(cal.result)
    print(cal.greeting)

    # Calls method add
    cal.add(2)
    sum1 = cal.get_result()
    print("sum = %i" % sum1)

