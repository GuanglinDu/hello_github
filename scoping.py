# A scoping demo
# Created on Dec. 9, 2017, Sat.

# Structuring, Testing, and Maintaining Python Programs
# https://intermediate-and-advanced-software-carpentry.readthedocs.io/en/latest/structuring-python.html

x = 1
def outer():
    x = 2

    def inner():
        global x # The outermost scope is used
        x = 3

    inner()

    print("x = %d" % x)

outer()             # 2
print("x = %d" % x) # 3


# A callback function that uppercases words
def replace(m):
    #match = m.group() # 'str' object has no attribute 'groups'
    match = m
    print('replace is processing: %s' % match)
    return match.upper()

s = "some string"

import re

str_list = s.split()
s2 = ""
for s1 in str_list:
    s2 = s2 + re.sub('\\S+', replace(s1), s1) + " "
print(s2)
