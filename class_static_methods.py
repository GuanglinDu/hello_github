# Class methods vs static methods vs instance methods
# http://stackoverflow.com/questions/136097/what-is-the-difference-between-staticmethod-and-classmethod-in-python

class MyClass(object):
    """Refer to example_google.py for the Google Style Python Docstrings"""
    def foo(self, x):
        """ An instance method (the common one)
        
        Args:
            x (str): the message provided
        """
        print "executing foo(%s, %s)" % (self, x)

    @classmethod
    def class_foo(cls, x):
        """ Compare with the class methods in Ruby """
        print "executing class_foo(%s, %s)" % (cls, x)

    @staticmethod
    def static_foo(x):
        """ The same as the static functions in C++ """
        print "executing static_foo(%s)" % x    

mc = MyClass()

# The usual way an object calls a method. The object, mc, is implicitly passed as the first argument.
mc.foo("Hello, instance method")

# With @classmethod, the object is implicitly passed as the first argument instead of self.
# You can also call class_foo using the class. In fact, if you define something to be a classmethod,
# it is probably because you intend to call it from the class rather than from a class instance.
# MyClass.foo(1) would have raised a TypeError, but MyClass.class_foo(1) works just fine.
mc.class_foo("Hello, class method") # call from the instance
MyClass.class_foo(1) # call from the class

# With @staticmethod, neither self (the object) nor  cls (the class) is implicitly passed as the first argument.
# They behave like plain functions except that you can call them from an instance or the class. The same as C++.
mc.static_foo(2) # call from the instance
# executing static_foo(2)

MyClass.static_foo('hi')# call from the class directly
# executing static_foo(hi)

# Staticmethods are used to group functions which have some logical connection with a class to the class.
