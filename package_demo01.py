# Created on Apr 12, 2015 Sun.
# http://www.learnpython.org/en/Modules_and_Packages
# http://www.tutorialspoint.com/python/python_modules.htm

# Imports module bar of package foo in either of 2 ways:
#import foo.bar # way 1
from foo import bar # way 2

# Calls the function in module bar in package foo (2 ways correspondingly)
#foo.bar.say_hi() # calls the function in way 1
bar.say_hi() # calls the function in way 2


# See also "Structuring, Testing, and Maintaining Python Programs":
# https://intermediate-and-advanced-software-carpentry.readthedocs.io/en/latest/structuring-python.html

# Packages
# For an example, look at this directory tree:
# package/
#  __init__.py        -- contains functions a(), b()
#  other.py           -- contains function c()
#  subdir/
#     __init__.py     -- contains function d()

# From this directory tree, you would be able to access the functions like so:
# import package
# package.a()
# package.b()

# import package.other # import a module in the package
# package.other.c()

# import package.subdir # import a sub-package (rarely-used)
# package.subdir.d()