# Created on Aug. 8, 2015 Sat.
#  http://stackoverflow.com/questions/1301346/the-meaning-of-a-single-and-a-double-underscore-before-an-object-name-in-python
# ._variable is semiprivate and meant just for convention
# .__variable is considered superprivate and gets namemangled to prevent accidental access
# .__variable__ is typically reserved for builtin methods or variables
# You can still access .__superprivate variables if you desperately want to. The double 
# underscores just namemangles, or renames, the variable to something like instance._className__superprivate

class Test(object):
    def __init__(self):
        """Works as a constructor"""
        self.__a = 'a'
        self._b = 'b'

    def print_a(self):
        print("I'm %s" % self.__a)
        
    def print_b(self):
        print("I'm %s" % self._b)

# Accesses these variables from the outside (objects)
# ._b is accessible because it is only hidden by convention
t = Test()
print(t._b) # 'b'

# t.__a isn't found because it no longer exists due to namemangling
# t.__a
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'Test' object has no attribute '__a'

# By accessing instance._className__variable instead of just the superprivate name,
# you can access the hidden value
print(t._Test__a) # 'a'

# No problem to manipulate the variables internally
t.print_a()
t.print_b()

