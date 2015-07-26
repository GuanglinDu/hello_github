# Class methods vs static methods vs instance methods
# http://stackoverflow.com/questions/136097/what-is-the-difference-between-staticmethod-and-classmethod-in-python

class MyClass(object):
    # An instance method
    def foo(self, x):
        print "executing foo(%s, %s)" % (self, x)

    @classmethod
    def class_foo(cls, x):
        print "executing class_foo(%s, %s)" % (cls, x)

    @staticmethod
    def static_foo(x):
        print "executing static_foo(%s)" % x    

a = MyClass()

# The usual way an object calls a method. The object, a, is implicitly passed as the first argument.
a.foo("Hello")

# With classmethods, the object is implicitly passed as the first argument instead of self.
# You can also call class_foo using the class. In fact, if you define something to be a classmethod,
# it is probably because you intend to call it from the class rather than from a class instance.
# A.foo(1) would have raised a TypeError, but A.class_foo(1) works just fine:
a.class_foo("Hello, class method")
MyClass.class_foo(1)

# With staticmethods, neither self (the object) nor  cls (the class) is implicitly passed as the first argument.
# They behave like plain functions except that you can call them from an instance or the class:
a.static_foo(1)
# executing static_foo(1)

MyClass.static_foo('hi')
# executing static_foo(hi)

# Staticmethods are used to group functions which have some logical connection with a class to the class.
